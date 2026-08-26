#!/usr/bin/env python3
"""Genera Algoritmi_Linguistici_maxi.md per il topic "Algoritmi Linguistici".

Unisce in un unico file:
- il file radice Human Connection Enginering (HCE)/Algoritmi Linguistici.md
- tutti i file .md contenuti nelle cartelle omonime (es.
  Corso Persuasione/Algoritmi Linguistici/ e le sue sottocartelle)

Il file di output viene scritto nella stessa cartella di questo script.
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
OUTPUT_DIR = SCRIPT_DIR

HCE_DIR = ROOT_DIR / "Human Connection Enginering (HCE)"
BASE_NAME = "Algoritmi Linguistici"
BASE_FILE = HCE_DIR / f"{BASE_NAME}.md"

# Sottocartelle da escludere ovunque vengano trovate.
EXCLUDE_SUBDIRS = {"website"}


def find_matching_folders(base_dir: Path, name: str):
    """Restituisce tutte le cartelle in base_dir (ricorsivo) chiamate `name`."""
    return sorted(p for p in base_dir.rglob("*") if p.is_dir() and p.name == name)


def collect_md_files():
    """Raccoglie il file radice e i .md dalle cartelle omonime, senza duplicati."""
    seen = set()
    files = []

    def add_file(path: Path):
        if not path.is_file():
            return
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            files.append(path)

    # 1. File radice
    add_file(BASE_FILE)

    # 2. Cartelle omonime all'interno di HCE
    for folder in find_matching_folders(HCE_DIR, BASE_NAME):
        for md_file in sorted(folder.rglob("*.md")):
            rel_parts = md_file.relative_to(folder).parts[:-1]
            if any(part in EXCLUDE_SUBDIRS for part in rel_parts):
                continue
            add_file(md_file)

    return files


def generate_maxi():
    md_files = collect_md_files()
    if not md_files:
        print(f"[SKIP] {BASE_NAME}: nessun file .md trovato")
        return

    output_path = OUTPUT_DIR / f"{BASE_NAME.replace(' ', '_')}_maxi.md"
    with output_path.open("w", encoding="utf-8") as out:
        for md_file in md_files:
            rel_path = md_file.relative_to(ROOT_DIR)
            title = md_file.stem
            out.write(f"\n\n---\n\n<!-- {rel_path} -->\n\n# {title}\n\n")
            out.write(md_file.read_text(encoding="utf-8", errors="replace"))

    print(f"[OK] {BASE_NAME}: {len(md_files)} file -> {output_path.name}")


if __name__ == "__main__":
    generate_maxi()
