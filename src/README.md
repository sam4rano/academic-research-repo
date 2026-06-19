# Source Code (src) Directory

Core preprocessing logic, feature extractors, and helper utilities.
**No model calls or metric computation here** — keep `src/` dependency-free from
`models/` and `evaluation/` to make testing and mocking easy.

---

## Planned Modules

| File | Purpose |
|------|---------|
| `preprocessing.py` | Text normalization, tokenization, audio resampling (16kHz), image resizing |
| `vad.py` | Voice Activity Detection — silence trimming with configurable window/padding |
| `data_loader.py` | Unified loader that returns `{"id", "input", "target"}` dicts from any source |
| `utils.py` | General helpers: path handling, JSON I/O, progress bars |

---

## VAD Parameters (must be logged for reproducibility)

When implementing `vad.py`, always log and document:

| Parameter | Example Value | What it controls |
|-----------|--------------|-----------------|
| `threshold_db` | `-40` | Silence cutoff in decibels |
| `frame_duration_ms` | `30` | VAD analysis window size |
| `padding_duration_ms` | `300` | Silence kept before/after speech |
| `sample_rate` | `16000` | Target sample rate (Hz) |

---

## Preprocessing Conventions

- **Audio**: Resample to 16 kHz, convert to float32, normalize loudness to −23 LUFS.
- **Text**: Strip leading/trailing whitespace; lowercase only if required by the model.
- **Tokenization**: Do not tokenize in `src/` — pass raw strings to model wrappers in `models/`.
- **Reproducibility**: Any stochastic preprocessing step (e.g. data augmentation)
  must respect the global seed set by `runner.py`.
