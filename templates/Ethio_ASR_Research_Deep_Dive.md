# Ethio-ASR Research Deep Dive (Reference Guide)

This document serves as a complete paper analysis and reproducibility checklist for the Ethio-ASR (Abdullah et al., 2026) paper.

---

## Paper & Repository Metadata
*   **Paper Title**: Ethio-ASR: Joint Multilingual Speech Recognition and Language Identification for Ethiopian Languages
*   **Authors**: Badr M. Abdullah, Israel Abebe Azime, Atnafu Lambebo Tonja, Jesujoba O. Alabi, Abel Mulat Alemu, Eyob G. Hagos, Bontu Fufa Balcha, Mulubrhan A. Nerea, Debela Desalegn Yadeta, Dagnachew Mekonnen Marilign, Amanuel Temesgen Fentahun, Tadesse Kebede, Israel D. Gebru, Michael Melese Woldeyohannis, Walelign Tewabe Sewunetie, Bernd Möbius, Dietrich Klakow
*   **Conference/Journal**: arXiv Preprint (under review)
*   **Venue Type**: Speech conference format (ISCA-style `keywords` block, numbered references `[1]`)
*   **Citation Style**: Numbered references `[1]` (ISCA / IEEE style — NOT natbib author-year)
*   **arXiv ID / Link**: [arxiv.org/abs/2603.23654](https://arxiv.org/abs/2603.23654)
*   **GitHub Repository**: [github.com/badrex/Ethio-ASR](https://github.com/badrex/Ethio-ASR)
*   **Hugging Face Models**: [huggingface.co/collections/badrex/ethio-asr](https://huggingface.co/collections/badrex/ethio-asr)
*   **Paper License**: CC BY-NC-ND 4.0 · **Corpus License (WAXAL)**: CC-BY-SA-4.0

---

## 1. Abstract & Core Contribution
*   **Problem Statement**: Five major Ethiopian languages (Amharic, Tigrinya, Oromo, Sidaama, Wolaytta — Semitic, Cushitic, and Omotic branches of Afroasiatic) are severely underrepresented in speech technology. No publicly available, high-quality ASR models exist for them; large multilingual models (Whisper, SeamlessM4T) offer little/no support.
*   **Core Contribution/Solution**:
    1.  **Ethio-ASR**: A suite of multilingual CTC-based models that perform **joint ASR + language identification (LID)** across the five languages via a `[LANG]` token prepended to the grapheme target sequence (no separate LID head or loss).
    2.  **Benchmarking**: Outperforms all baselines, including OmniASR CTC/LLM variants up to 7B parameters, using models between 94M–1B parameters.
    3.  **Analysis suite**: Gender bias, vowel length / consonant gemination error contribution, and multilingual CTC training dynamics.
    4.  **Open release** of models and codebase.
*   **Key Findings**:
    *   Best model, `Ethio-ASR (w2v-bert-2.0)` (600M), reaches **avg. WER 30.48%** on WAXAL test, beating `omniASR-llm-7b-v2` (32.21%) with >10× fewer parameters.
    *   Monolingual per-language SFT (5×600M) is only **0.48 pp better** (30.00%) than the single multilingual model — one shared model suffices.
    *   All models reach **>99.8% LID accuracy** with the CTC objective alone; removing the LID token changes WER by <0.7 pp (not significant, p > 0.45).
    *   Normalizing vowel length + gemination cuts WER by **~10–13 pp absolute (~35–40% relative)** in Latin-script languages — these contrasts are a dominant error source that scaling does not fix.

---

## 2. Languages & Linguistic Challenges (Section 2 of paper)

| Language | ISO | Branch | % of Population | Script | ASR-relevant Features |
|---|---|---|---|---|---|
| Amharic | AMH | Ethio-Semitic | ~29.3% (L1) | Ethiopic (Ge'ez) | Ejectives /pʼ, tʼ, kʼ, t͡ʃʼ, sʼ/, central vowels /ɨ, ä/, gemination unmarked in script |
| Oromo | ORM | Cushitic | ~34% | Latin (Qubee) | Ejectives /tʼ, kʼ/, implosive /ɗ/, contrastive vowel length + gemination (letter doubling) |
| Tigrinya | TIR | Ethio-Semitic | ~6% | Ethiopic (Ge'ez) | Pharyngeals /ħ, ʕ/, uvular ejective fricative /xʼ/, phonemic gemination |
| Sidaama | SID | Cushitic | ~4% | Latin | 5 vowel qualities short/long, phonemic gemination, glottal stop /ʔ/, all words vowel-final |
| Wolaytta | WAL | Omotic | ~2.2% | Latin | Vowel length + gemination phonemic, ejectives, no pharyngeals |

*   **Challenges identified**: (1) ejectives/pharyngeals/implosives underrepresented in pre-training data; (2) length contrasts (gemination, vowel length) under variable speaking rates; (3) large Ge'ez grapheme inventory with long-tail frequency (384 Unicode code points); (4) rich morphology → high OOV rates.
*   **Lexical evidence (Section 3.2)**: TTR at 800k tokens — Wolaytta 0.146, Sidaama ~0.14, Tigrinya 0.134 vs. English 0.043 (>3× higher); much steeper vocabulary growth curves than English/French (Multilingual LibriSpeech).

---

## 3. Dataset & Data Pipeline
*   **Dataset**: Ethiopian subset of the **WAXAL corpus** (21 African languages, CC-BY-SA-4.0). Largest public Ethiopian speech corpus to date.
    *   *Size*: **~1,106 hours** total; train balanced at **181–197 h per language**; 60.9% of training samples are Latin-script.
    *   *HF dataset used by codebase*: `badrex/waxalNLP-ethiopic-final` (197,634 rows).
    *   *Modalities*: scripted (read transcriptions of image descriptions) + unscripted (spontaneous, expert, prompted); 4 prosodic styles (free, emphatic, expressive, interrogative).
    *   *QC workflow*: collectors → transcribers → validators; ≥2 validators per recording checking image–audio–transcript alignment, noise, and silence.
*   **Known imbalance**: gender skew per split (e.g., Wolaytta test = **0.00 h male** / 12.40 h female; Sidaama train = 64.70 h male / 127.53 h female) → drives the gender-bias analysis.
*   **Audio duration by language & split (hours, Table 2)**:

| Split | AMH | ORM | TIR | SID | WAL |
|---|---|---|---|---|---|
| Train | 189.71 | 189.89 | 181.87 | 192.23 | 197.32 |
| Validation | 13.97 | 14.46 | 16.79 | 15.34 | 9.60 |
| Test | 16.24 | 18.24 | 20.26 | 17.80 | 12.40 |

---

## 4. Method: Joint ASR + LID Modeling
*   **Architecture**: pre-trained speech encoder + linear projection to shared vocabulary; CTC decoding (single forward pass, no autoregression).
*   **Target sequence**: `y = <[LANG], G_1, G_2, …, G_N>` with `[LANG] ∈ {[AMH], [TIR], [ORM], [SID], [WAL]}` — the LID token is an ordinary CTC output symbol (no LID loss, no loss-weighting hyperparameter).
*   **Vocabulary**: grapheme-based, **409 symbols** total = 326 core Ge'ez graphemes + 29 Ethiopic punctuation/numerals + 26 Latin letters + 25 Latin punctuation/numerals + 5 LID tokens/specials.
*   **Objective**: standard CTC negative log-likelihood `L = −log P_CTC(y|x)`.

---

## 5. Evaluated Models & Training Configuration
*   **Fine-tuned encoders (this work)**:
    *   `AfriHuBERT` — 94M, African-language pre-training, CC-BY-NC-SA 4.0 (trained in float32)
    *   `MMS-300M` / `MMS-1B` — 1,000+ language pre-training, CC-BY-NC 4.0
    *   `w2v-BERT-2.0` — 600M Conformer, 4.6M h multilingual speech, MIT license
*   **Baselines**: Whisper small/medium/large-v3, SeamlessM4T-v2-large, `mms-1b-all`, OmniASR CTC + LLM variants (300M–7B). Note: OmniASR trained on a pre-release WAXAL subset (July 2025) → possible test-set overlap.
*   **Training hyperparameters (paper Section 5.1)**:
    *   7 epochs, effective batch size 32 → ~36.8k steps; AdamW; LR swept over {3e-5, 7e-5, 3e-4, 7e-4}; linear warmup 10%.
    *   Convolutional feature extractor frozen; bfloat16 mixed precision (float32 for AfriHuBERT).
    *   Eval every 800 steps; checkpoint selection by `0.5×WER + 0.5×CER`.
*   **Post-processing before scoring**: punctuation removal + Ge'ez homophone normalization (Ethiopic NLP best practice).

---

## 6. Runner Logic & Repo Structure (github.com/badrex/Ethio-ASR)
*   **Main entry point**: `scripts/train_model.py --config config_files/<experiment>.yaml`
*   **Repo layout**: `bash_scripts/` (launchers), `config_files/` (YAML experiment configs), `json_outputs/`, `learning_dynamics/` (Section 6.3 probing), `post_processing/` (normalization), `scripts/`, `src/`, `Dockerfile`, `run.sub` (HTCondor).
*   **Pipeline walkthrough**:
    1.  `.env` supplies `WANDB_API_KEY`, `HF_API_KEY`, cache dirs (`HF_HOME`, `NUMBA_CACHE_DIR`, `LIBROSA_CACHE_DIR`, `MPLCONFIGDIR`).
    2.  YAML config sets `pretrained_model` (e.g. `facebook/w2v-bert-2.0`), `seed: 42`, `freeze_feature_encoder: true`, `add_language_tokens: true`, explicit `character_set` (full Ge'ez + Latin inventory), dataset `badrex/waxalNLP-ethiopic-final`, `language: "all"`.
    3.  Bash script exports caches, logs `nvidia-smi`, launches training.
    4.  `run.sub` submits to HTCondor: Docker image `badrnlp/hf-gpu-asr:0.2`, 12 CPUs, 50G RAM, 1 GPU.
    5.  Logging via Weights & Biases (project `Ethio-ASR`).
*   **Config nuances**: `add_final_layer_adapter: true` for w2v-BERT-2.0 but `false` for MMS-300M; LR 3e-5 (w2v-BERT) vs 5e-4 (MMS-300M); `fp16: true`, `gradient_checkpointing: true`, `save_total_limit: 2`.

---

## 7. Metric Functions & Results

| Task | Metric | Tool | Direction | Notes |
|---|---|---|---|---|
| ASR | WER | jiwer-style WER | ↓ | Micro-averaged; 95% bootstrap CIs for ablation |
| ASR (checkpointing) | 0.5×WER + 0.5×CER | — | ↓ | Model selection criterion |
| LID | Accuracy | token match | ↑ | Decoded `[LANG]` token vs. gold |

*   **Main WAXAL test results (avg. WER % ↓)**: whisper-large-v3 148.60 · seamless-m4t-v2 100.75 · mms-1b-all 62.28 · omniASR-ctc-7b-v2 37.26 · omniASR-llm-7b-v2 32.21 · **Ethio-ASR afrihubert 35.08 · mms-300 33.99 · mms-1b 31.20 · w2v-bert-2.0 30.48** · monolingual SFT (5×600M) 30.00.
*   **Per-language best (w2v-bert-2.0)**: AMH 22.92 · TIR 35.22 · ORM 24.44 · WAL 38.19 · SID 31.65.
*   **FLEURS zero-shot OOD (WER %)**: Ethio-ASR (w2v-bert-2.0) AMH **19.17** (vs. omniASR-llm-7b 12.77, which saw FLEURS in training); ORM 70.47 for Ethio-ASR — but human eval found **36.1% of FLEURS Oromo audio unintelligible**, and for Amharic evaluators preferred the model transcript over the FLEURS reference in 43.4% of cases (reference preferred 55.1%) → FLEURS quality issues confound OOD comparison.
*   **LID accuracy**: afrihubert 99.92 · mms-300m 99.92 · mms-1b 99.91 · w2v-bert-2.0 99.83.

---

## 8. Model Analysis Findings (Section 6)
*   **LID ablation (6.1)**: training with vs. without `[LANG]` token → WER deltas <0.7 pp, overlapping CIs, paired bootstrap n=1000, p > 0.45. Joint LID is "free"; released models keep it for deployment utility.
*   **Gender bias (6.2)** (Wolaytta excluded — no male test audio): **Tigrinya male WER ≈ +18–19 pp worse than female across all 4 models** (e.g. w2v-bert-2.0: M 50.62 vs F 31.98); AMH/ORM gaps +1.7–3.8 pp; **Sidaama reversed** (female slightly worse, −1.4 to −4.6 pp). Attributed to female-skewed training hours.
*   **Training dynamics (6.3)** (1 epoch ≈ 6.2k steps, eval every 100): three phases — (1) LID accuracy saturates in first ~4–5% of steps while WER still high; (2) rapid WER drop at ~5–10% of steps, Latin WER falls earlier/steeper than Ge'ez for MMS-1B; (3) gradual refinement thereafter. LID emerges **before** transcription ability.
*   **Vowel length & gemination (6.4)**: post-hoc normalization on ORM/SID/WAL (collapse `aa→a`, `dd→d`) — vowel length dominates errors in Oromo & Wolaytta, gemination in Sidaama; combined normalization → **~10–13 pp absolute / ~35–40% relative WER reduction**, holding even for OmniASR-LLM-7B → not fixable by scale or autoregressive decoding.

---

## 9. Synthesis, Gaps & Next Steps

| Dimension | Detail |
|---|---|
| **Limitations identified by paper** | No standalone Limitations section; implicitly: gender-imbalanced corpus drives WER disparities (data problem, not modeling); length-contrast errors unresolved by current end-to-end adaptation; FLEURS Oromo too noisy for reliable OOD evaluation; possible OmniASR train/test overlap with WAXAL. |
| **Open gaps (your read)** | No streaming/real-time evaluation; no code-switching (Amharic–English) tests; no LM fusion / shallow-fusion decoding experiments; hardware specs & training cost not reported; only Ethiopian WAXAL subset used (16 other WAXAL languages untouched); no explicit length-contrast modeling attempted (only diagnosed). |
| **Actionable next steps** | (1) Add duration-aware or phoneme-aware modeling (e.g. explicit long-phone units) to attack the 35–40% error mass from length contrasts; (2) rebalance or augment male Tigrinya speech (speed/pitch perturbation) to close the 18 pp gender gap; (3) extend joint `[LANG]`-token CTC recipe to the remaining WAXAL languages; (4) benchmark inference latency CTC vs. OmniASR-LLM to quantify the claimed efficiency edge. |

---

## 10. Reproducibility Checklist

| Item | Status | Notes |
|---|---|---|
| Code publicly available | ✅ | [github.com/badrex/Ethio-ASR](https://github.com/badrex/Ethio-ASR) (Python 98.6%, Dockerfile, HTCondor `run.sub`) |
| Dataset publicly available | ✅ | WAXAL (CC-BY-SA-4.0); HF: `badrex/waxalNLP-ethiopic-final` |
| Pre-trained model weights | ✅ | [huggingface.co/collections/badrex/ethio-asr](https://huggingface.co/collections/badrex/ethio-asr) |
| Random seed reported | ✅ | `seed: 42` in YAML config |
| All hyperparameters reported | ✅ | Epochs, batch size, LR sweep, warmup, precision, checkpoint criterion |
| Hardware / compute budget reported | ⚠️ | No GPU model/VRAM in paper; repo shows 1-GPU HTCondor jobs, Docker `badrnlp/hf-gpu-asr:0.2`; NHR compute acknowledged |
| Evaluation scripts provided | ✅ | `post_processing/` normalization + eval in repo |
| Statistical significance testing | ✅ | Paired bootstrap (n=1000) with 95% CIs for LID ablation |

---

## 11. BibTeX Citation

> **Venue note**: The preprint uses ISCA-style formatting (keywords block, numbered
> references `[1]`), suggesting a speech venue (INTERSPEECH/ICASSP) target. If citing
> in an IEEE/ISCA venue use numbered style; in ACL/NeurIPS use natbib `\citep`.
> Update to the published version once it appears (see Common Pitfalls in SKILL.md).

**Before official publication** (cite as arXiv preprint):
```bibtex
@misc{abdullah2026ethioasr,
  title         = {{Ethio-ASR}: Joint Multilingual Speech Recognition and Language
                   Identification for Ethiopian Languages},
  author        = {Abdullah, Badr M. and Azime, Israel Abebe and Tonja, Atnafu Lambebo
                   and Alabi, Jesujoba O. and Alemu, Abel Mulat and Hagos, Eyob G.
                   and Balcha, Bontu Fufa and Nerea, Mulubrhan A. and Yadeta, Debela Desalegn
                   and Marilign, Dagnachew Mekonnen and Fentahun, Amanuel Temesgen
                   and Kebede, Tadesse and Gebru, Israel D. and Woldeyohannis, Michael Melese
                   and Sewunetie, Walelign Tewabe and M{\"o}bius, Bernd and Klakow, Dietrich},
  year          = {2026},
  eprint        = {2603.23654},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
```

**For INTERSPEECH / ISCA venues** (if accepted there):
```bibtex
@inproceedings{abdullah2026ethioasr,
  author    = {Abdullah, Badr M. and Azime, Israel Abebe and Tonja, Atnafu Lambebo
               and Alabi, Jesujoba O. and Alemu, Abel Mulat and Hagos, Eyob G.
               and Balcha, Bontu Fufa and Nerea, Mulubrhan A. and Yadeta, Debela Desalegn
               and Marilign, Dagnachew Mekonnen and Fentahun, Amanuel Temesgen
               and Kebede, Tadesse and Gebru, Israel D. and Woldeyohannis, Michael Melese
               and Sewunetie, Walelign Tewabe and M{\"o}bius, Bernd and Klakow, Dietrich},
  title     = {{Ethio-ASR}: Joint Multilingual Speech Recognition and Language
               Identification for Ethiopian Languages},
  booktitle = {Proc. INTERSPEECH 2026},
  year      = {2026},
  url       = {https://arxiv.org/abs/2603.23654}
}
```

**For ACL / NeurIPS venues** (natbib, author-year):
```bibtex
@inproceedings{abdullah2026ethioasr,
  title     = {{Ethio-ASR}: Joint Multilingual Speech Recognition and Language
               Identification for Ethiopian Languages},
  author    = {Abdullah, Badr M. and Azime, Israel Abebe and Tonja, Atnafu Lambebo
               and Alabi, Jesujoba O. and Alemu, Abel Mulat and Hagos, Eyob G.
               and Balcha, Bontu Fufa and Nerea, Mulubrhan A. and Yadeta, Debela Desalegn
               and Marilign, Dagnachew Mekonnen and Fentahun, Amanuel Temesgen
               and Kebede, Tadesse and Gebru, Israel D. and Woldeyohannis, Michael Melese
               and Sewunetie, Walelign Tewabe and M{\"o}bius, Bernd and Klakow, Dietrich},
  booktitle = {Proceedings of INTERSPEECH 2026},
  year      = {2026},
  url       = {https://arxiv.org/abs/2603.23654}
}
```
