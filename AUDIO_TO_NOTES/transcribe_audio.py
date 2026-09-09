#!/usr/bin/env python3
"""Trascrive tutti i file .mp3 della cartella corrente in file .txt
usando faster-whisper (modello "small").

Uso (con la venv dove è installato faster-whisper):
    ~/.venvs/whisper/bin/python transcribe_audio.py
"""

from pathlib import Path

from faster_whisper import WhisperModel

MODEL_SIZE = "small"
LANGUAGE = "it"

base = Path(__file__).parent
mp3_files = sorted(base.glob("*.mp3"))

if not mp3_files:
    print("Nessun file .mp3 trovato.")
    raise SystemExit(0)

print(f"Carico modello {MODEL_SIZE!r}...")
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

for mp3 in mp3_files:
    txt_path = mp3.with_suffix(".txt")
    print(f"\n=== {mp3.name} -> {txt_path.name} ===")
    segments, info = model.transcribe(
        str(mp3),
        language=LANGUAGE,
        beam_size=5,
        vad_filter=True,
    )
    print(f"Lingua rilevata: {info.language} (probabilità {info.language_probability:.2f})")
    lines = []
    for seg in segments:
        line = seg.text.strip()
        print(f"[{seg.start:7.1f}s] {line}")
        lines.append(line)
    txt_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Salvato: {txt_path}")

print("\nFatto.")
