#!/usr/bin/env python3
"""Genera un file "maxi" .md per ogni cartella principale del progetto.

Per ogni cartella di primo livello nella root del progetto (esclusi .git,
.obsidian e la cartella di questo script), crea in questa stessa cartella
un file "<NomeCartella>_maxi.md" che contiene, uno dopo l'altro, i
contenuti di tutti i file .md trovati ricorsivamente in quella cartella.

Oltre alle cartelle principali, genera un maxi anche per le cartelle
elencate in EXTRA_TARGETS (es. una sottocartella specifica come SLCC),
anche se il suo contenuto è già incluso nel maxi della cartella principale.
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
OUTPUT_DIR = SCRIPT_DIR

EXCLUDE_DIRS = {".git", ".obsidian", SCRIPT_DIR.name}

# Nomi di sottocartelle da escludere ovunque vengano trovate (a qualsiasi
# livello) all'interno di una cartella principale, es. "website" in HCE.
EXCLUDE_SUBDIRS = {"website"}

# Sottocartelle specifiche (relative a ROOT_DIR) per cui generare un maxi
# dedicato, in aggiunta al maxi della rispettiva cartella principale.
EXTRA_TARGETS = [
    ROOT_DIR / "Human Connection Enginering (HCE)" / "Corso Persuasione" / "SLCC",
]


def find_md_files(folder: Path):
    md_files = []
    for md_file in folder.rglob("*.md"):
        rel_parts = md_file.relative_to(folder).parts[:-1]
        if any(part in EXCLUDE_SUBDIRS for part in rel_parts):
            continue
        md_files.append(md_file)
    return sorted(md_files)


def generate_maxi(folder: Path):
    md_files = find_md_files(folder)
    if not md_files:
        print(f"[SKIP] {folder.name}: nessun file .md trovato")
        return

    output_path = OUTPUT_DIR / f"{folder.name}_maxi.md"
    with output_path.open("w", encoding="utf-8") as out:
        for md_file in md_files:
            rel_path = md_file.relative_to(folder)
            title = md_file.stem
            out.write(f"\n\n---\n\n<!-- {rel_path} -->\n\n# {title}\n\n")
            out.write(md_file.read_text(encoding="utf-8", errors="replace"))

    print(f"[OK] {folder.name}: {len(md_files)} file -> {output_path.name}")


def main():
    main_folders = sorted(
        p for p in ROOT_DIR.iterdir()
        if p.is_dir() and p.name not in EXCLUDE_DIRS
    )

    for folder in main_folders:
        generate_maxi(folder)

    for folder in EXTRA_TARGETS:
        if folder.is_dir():
            generate_maxi(folder)
        else:
            print(f"[SKIP] {folder.name}: cartella non trovata ({folder})")


if __name__ == "__main__":
    main()
