#!/usr/bin/env python3
"""
Generatore di domande per HCE Questions.

Scansiona tutti i file .md nella cartella genitore (Human Connection Enginering)
e nelle sue sottocartelle, esclusa la cartella in cui risiede questo script,
e produce un file questions.json con domande a risposta multipla.

Uso:
    python3 generate_questions.py
"""

import os
import json
import re
import random
from pathlib import Path

# Cartella di lavoro: genitore della cartella che contiene questo script
SCRIPT_DIR = Path(__file__).resolve().parent
BASE = SCRIPT_DIR.parent
OUTPUT = SCRIPT_DIR / 'questions.json'

# Concetti/heading troppo generici da usare come risposta
GENERIC_NAMES = {
    '', 'hce', 'definizione', 'funzione', 'sintesi', 'applicazioni pratiche',
    'errori comuni', 'introduzione', 'conclusione', 'note', 'esempi',
    'intelligenze', 'modello hce', 'human connection enginering (hce)',
    '1', '2', '3', '4', '5'
}


def is_generic(name):
    if not name:
        return True
    n = name.strip().lower()
    if n in GENERIC_NAMES:
        return True
    if len(n) < 3:
        return True
    if re.match(r'^\d+\s*-', n):
        return True
    return False


def find_md_files():
    files = []
    for root, dirs, filenames in os.walk(BASE):
        # Salta la cartella che contiene questo script
        dirs[:] = [d for d in dirs if (Path(root) / d).resolve() != SCRIPT_DIR.resolve()]
        for f in filenames:
            if f.endswith('.md'):
                files.append(Path(root) / f)
    return files


def clean_markdown(text):
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            text = parts[2]
    text = re.sub(r'\[\[(.*?)\]\]', r'\1', text)
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'`', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text.strip()


def extract_concept(path, text):
    stem = path.stem.strip()

    m = re.match(r'^\d+\s*-\s*(.+)', stem)
    if m:
        after = m.group(1).strip()
        if not is_generic(after):
            return after

    if not is_generic(stem):
        return stem

    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        m = re.match(r'^#{1,6}\s*\[\[(.*?)\]\]', line)
        if m:
            candidate = m.group(1).strip()
            if not is_generic(candidate):
                return candidate
        m = re.match(r'^#{1,6}\s*(.+)', line)
        if m:
            candidate = m.group(1).strip()
            if not is_generic(candidate):
                return candidate
        m = re.search(r'\[\[(.*?)\]\]', line)
        if m:
            candidate = m.group(1).strip()
            if not is_generic(candidate):
                return candidate

    m = re.match(r'^\d+\s*-\s*(.+)', stem)
    if m:
        return m.group(1).strip()

    return stem


def starts_with_concept(p, concept):
    c = concept.lower()
    patterns = [
        rf'^\s*{re.escape(c)}\s+(è|sono|è\s+un|è\s+una|riguarda|studia|descrive)',
        rf'^\s*(il|la|lo|le|gli|i)\s+{re.escape(c)}\s+(è|sono|è\s+un|è\s+una|riguarda|studia|descrive)',
    ]
    for pat in patterns:
        if re.search(pat, p, re.IGNORECASE):
            return True
    return False


def is_substantial_definition(p):
    p = p.strip()
    if len(p) < 50:
        return False
    if re.match(r'^#{1,6}\s*\w+\s*$', p):
        return False
    if '\n' not in p and len(p.split()) <= 5:
        return False
    return True


def extract_definition(text, concept):
    paragraphs = re.split(r'\n\s*\n', text.strip())
    candidates = []

    for raw in paragraphs:
        raw = raw.strip()
        if not raw:
            continue
        p = re.sub(r'^#{1,6}\s*', '', raw)
        p = clean_markdown(p)
        if not is_substantial_definition(p):
            continue
        if starts_with_concept(p, concept):
            candidates.insert(0, p)
        else:
            candidates.append(p)

    if candidates:
        return candidates[0]

    for raw in paragraphs:
        raw = raw.strip()
        if not raw:
            continue
        p = re.sub(r'^#{1,6}\s*', '', raw)
        p = clean_markdown(p)
        if len(p) >= 40:
            return p

    return None


def mask_concept(definition, concept):
    patterns = [
        (rf'\b{re.escape(concept)}\b', '______'),
        (rf'\b(le|gli|i|la|lo)\s+{re.escape(concept)}\b', r'\1 ______'),
    ]
    for pat, repl in patterns:
        new_def, count = re.subn(pat, repl, definition, count=1, flags=re.IGNORECASE)
        if count > 0:
            return new_def
    words = concept.split()
    if len(words) > 1:
        for w in words:
            if len(w) > 3:
                new_def, count = re.subn(rf'\b{re.escape(w)}\b', '______', definition, count=1, flags=re.IGNORECASE)
                if count > 0:
                    return new_def
    return definition


def get_area(folder):
    parts = folder.split('/')
    if len(parts) >= 2:
        return '/'.join(parts[:2])
    return folder


def main():
    files = find_md_files()
    entries = []
    for f in files:
        try:
            raw = f.read_text(encoding='utf-8')
            cleaned = clean_markdown(raw)
            concept = extract_concept(f, cleaned)
            if not concept or is_generic(concept):
                print(f"Saltato {f}: concetto non identificabile ({concept})")
                continue
            definition = extract_definition(raw, concept)
            if not definition:
                print(f"Saltato {f}: definizione non trovata")
                continue
            rel_path = f.relative_to(BASE)
            folder = str(rel_path.parent)
            entries.append({
                'file': str(rel_path),
                'concept': concept,
                'definition': definition,
                'folder': folder,
                'area': get_area(folder)
            })
        except Exception as e:
            print(f"Errore su {f}: {e}")

    by_folder = {}
    by_area = {}
    for e in entries:
        by_folder.setdefault(e['folder'], []).append(e)
        by_area.setdefault(e['area'], []).append(e)

    questions = []
    for e in entries:
        used_concepts = {e['concept'].lower()}
        used_files = {e['file']}
        distractors = []

        def add_candidates(candidates):
            for c in candidates:
                if c['file'] in used_files:
                    continue
                if c['concept'].lower() in used_concepts:
                    continue
                if is_generic(c['concept']):
                    continue
                distractors.append(c)
                used_files.add(c['file'])
                used_concepts.add(c['concept'].lower())

        add_candidates(by_folder.get(e['folder'], []))
        if len(distractors) < 3:
            add_candidates(by_area.get(e['area'], []))
        if len(distractors) < 3:
            add_candidates(entries)

        if len(distractors) < 3:
            print(f"Saltato {e['file']}: troppi pochi distrattori")
            continue

        chosen = random.sample(distractors, 3)
        options = [e['concept']] + [d['concept'] for d in chosen]
        random.shuffle(options)
        correct = options.index(e['concept'])

        masked_definition = mask_concept(e['definition'], e['concept'])
        questions.append({
            'question': f"Quale concetto è descritto da: \"{masked_definition}\"?",
            'options': options,
            'correct': correct,
            'source': e['file']
        })

    random.shuffle(questions)
    OUTPUT.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Generato {len(questions)} domande in {OUTPUT}")


if __name__ == '__main__':
    main()
