# Evaluation Directory

Place metric computation scripts and output analytics files here.
Outputs written by `runner.py` land in `evaluation/outputs/` (git-ignored).

---

## Recommended Libraries

| Task | Library | Install | Notes |
|------|---------|---------|-------|
| ASR | `jiwer` | `pip install jiwer` | WER, CER, MER |
| MT / ST (best) | `unbabel-comet` | `pip install unbabel-comet` | CometKiwi — reference-free, human-correlated |
| MT / ST (legacy) | `sacrebleu` | `pip install sacrebleu` | BLEU — requires references |
| Summarisation | `bert-score` | `pip install bert-score` | Use `deberta-xlarge-mnli` model |
| Summarisation (legacy) | `rouge-score` | `pip install rouge-score` | N-gram overlap |
| Speech quality (MOS) | `utmos` | manual install | See [UTMOS22 repo](https://github.com/sarulab-speech/UTMOS22) |
| Speech quality | `pesq` | `pip install pesq` | Reference-based PESQ |
| Diarisation / segmentation | `pyannote.metrics` | `pip install pyannote.metrics` | Collar-F1 (±3s) |

---

## Structure

```
evaluation/
├── outputs/          # Auto-created by runner.py (git-ignored)
│   ├── predictions.json
│   └── metrics.json
├── eval_asr.py       # Example: WER computation script
├── eval_mt.py        # Example: CometKiwi / BLEU computation
└── README.md         # This file
```

---

## Reporting Standards

- Always report metric **direction** (↑ / ↓) in tables.
- Report **mean ± std** across seeds when running multiple seeds.
- For classification tasks with imbalanced classes, report **macro-F1**, not accuracy.
- Include a **per-subgroup breakdown** (e.g. per language, per domain) wherever possible.
