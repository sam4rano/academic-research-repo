# Data Storage Directory

Store all raw, intermediate, cached, and split datasets here.
**This directory is excluded from version control** (see `.gitignore`).

---

## Structure

```
data_storage/
├── raw/          # Unmodified downloaded datasets (never edit these)
├── processed/    # After normalization, tokenization, or noise filtering
└── splits/       # Final evaluation splits: train.json, dev.json, test.json
```

## Conventions

- **Never overwrite** files in `raw/`. Always derive `processed/` from `raw/`.
- Keep a **`data_stats.json`** in `splits/` with per-split statistics:
  ```json
  {
    "train": {"n_samples": 0, "languages": [], "duration_min": 0},
    "dev":   {"n_samples": 0, "languages": [], "duration_min": 0},
    "test":  {"n_samples": 0, "languages": [], "duration_min": 0}
  }
  ```
- Document the **source URL or HuggingFace dataset ID** for all raw files in a
  `raw/SOURCES.md` file.
- Log all preprocessing steps (sample rate, VAD thresholds, etc.) in `src/README.md`
  or as config files in `configs/`.

## .gitkeep Files

Each subdirectory contains a `.gitkeep` file so the empty folder structure is
tracked by git. Delete `.gitkeep` files as you add real data files.
