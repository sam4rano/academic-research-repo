# DOWIS Research Deep Dive (Reference Guide)

This document serves as a reference example of a complete paper breakdown using the DOWIS (Züfle et al., 2026) paper.

---

## Paper & Repository Metadata
*   **Paper Title**: Do What I Say: A Spoken Prompt Dataset for Instruction-Following
*   **Authors**: Maike Züfle, Sara Papi, Fabian Retkowski, Szymon Mazurek, Marek Kasztelnik, Alexander Waibel, Luisa Bentivogli, Jan Niehues
*   **Conference/Journal**: INTERSPEECH 2026
*   **Venue Type**: Speech conference (ISCA)
*   **Citation Style**: Numbered references `[1]` (ISCA / INTERSPEECH format — NOT natbib author-year)
*   **Page Limit**: 4 pages (references included) — forces extremely concise writing
*   **arXiv ID / Link**: [arxiv.org/abs/2603.09881](https://arxiv.org/abs/2603.09881)
*   **GitHub Repository**: [github.com/MaikeZuefle/DOWIS](https://github.com/MaikeZuefle/DOWIS)
*   **Hugging Face Dataset**: [maikezu/dowis](https://huggingface.co/datasets/maikezu/dowis)

---

## 1. Abstract & Core Contribution
*   **Problem Statement**: Speech Large Language Models (SLLMs) are currently evaluated using text-based prompts, failing to test the model's actual ability to follow instructions when prompts are spoken aloud.
*   **Core Contribution/Solution**: The authors introduce **DOWIS (DoWhatISay)**, the first multilingual speech instruction-following benchmark featuring parallel human-recorded spoken instructions and written equivalents.
*   **Key Findings**: Text prompting consistently beats speech prompting, especially for low-resource languages. The performance gap only closes for tasks that produce speech output.

---

## 2. Dataset & Data Loader Pipeline
*   **Dataset Schema**:
    *   *Inputs / Modalities*: Parallel Speech (human recorded audio) and Text prompts.
    *   *Output Target / Labels*: Downstream dataset targets (e.g. translation text, transcriptions).
    *   *Languages*: 12 languages (cs, de, en, es, fr, hu, it, nl, pt, ru, sq, sv).
    *   *Tasks Supported*: ASR, TTS, MT, S2ST, SLU, SQA, SSUM, ST, TSUM, ACHAP, LIPREAD.
*   **Data Adapters**:
    *   *Files containing data logic*: `data/asr.py`, `data/mt.py`, `data/tts.py`
    *   *External datasets mapped/loaded*: `google/fleurs` for ASR/ST, custom loaders for others.
    *   *Data size / duration / analytics*: 1,320 rows of parallel prompts. Audio prompts statistics in `audio_prompts_statistics.json` total 3h 16m 20s.

---

## 3. Evaluated Models & Inference Configuration
*   **Model Baselines**:
    *   `phi_multimodal`
    *   `qwen_omni`
*   **Model Preprocessing**:
    *   Audio sample rates normalized to 16kHz, float16 precision.
    *   Loudness-based Voice Activity Detection (VAD) to trim silences.
*   **Generation Parameters**:
    *   Set seed = 42 for reproducibility.
    *   Greedy decoding (temperature = 0) used for comparative metrics.

---

## 4. Inference Execution & Runner logic
*   **Main Runner File**: `main.py`
*   **Pipeline Walkthrough**:
    1.  Load the designated SLLM (Qwen-Omni or Phi-Multimodal).
    2.  Load the downstream target dataset (e.g., Fleurs test split).
    3.  Load corresponding parallel written and spoken prompts from `maikezu/dowis`.
    4.  Run loop over prompt styles (Basic, Short, Detailed, Formal, Informal).
    5.  Cache outputs to `/outputs/` partition.

---

## 5. Metric Functions & Statistical Analysis
*   **Evaluation Metrics**:
    *   ASR: Word Error Rate (WER ↓) via `jiwer`
    *   MT / ST: CometKiwi ↑ and BLEU ↑
    *   Summarisation: BERTScore ↑ and ROUGE ↑
*   **Analytics Code**:
    *   `prompts/audio_prompts_statistics.json` tracks duration statistics per language.

---

## 6. Synthesis, Gaps & Next Steps

| Dimension | Detail |
|-----------|--------|
| **Limitations identified by paper** | High WER degradation on low-resource languages with speech prompts; cross-lingual mismatch between prompt and task language not studied |
| **Open gaps (your read)** | No multi-turn conversational spoken instructions; no noise-augmented prompt variants; only 2 SLLMs evaluated |
| **Actionable next steps** | (1) Test robust audio encoders / noise injection during training; (2) Expand to conversational multi-turn prompts; (3) Add more SLLMs (e.g. Gemini, AudioPaLM) |

---

## 7. Reproducibility Checklist

| Item | Status |
|------|--------|
| Code publicly available | ✅ ([github.com/MaikeZuefle/DOWIS](https://github.com/MaikeZuefle/DOWIS)) |
| Dataset publicly available | ✅ ([maikezu/dowis](https://huggingface.co/datasets/maikezu/dowis)) |
| Random seed reported | ✅ (seed = 42) |
| Hardware / compute budget reported | ⚠️ (float16 mentioned; full GPU spec not in paper) |
| Evaluation scripts provided | ✅ |
| Pre-trained model weights | ✅ (HF model IDs given) |
| All hyperparameters reported | ✅ (greedy decoding, temperature = 0) |

---

## 8. BibTeX Citation

> **Venue note**: INTERSPEECH uses ISCA format with numbered references `[1]`.
> The `booktitle` follows the pattern `Proc. INTERSPEECH {Year}` (not the full
> "Proceedings of the ..." style used by ACL). If citing this paper in an ACL
> or NeurIPS submission, use `\citep{zufle2026dowis}` (natbib). If citing in
> an IEEE venue (ICASSP, SLT), use `IEEEtran.bst` and the numbered `[1]` format.

**For INTERSPEECH / ISCA venues:**
```bibtex
@inproceedings{zufle2026dowis,
  author    = {Z{\"u}fle, Maike and Papi, Sara and Retkowski, Fabian and Mazurek, Szymon
               and Kasztelnik, Marek and Waibel, Alexander and Bentivogli, Luisa
               and Niehues, Jan},
  title     = {Do What I Say: A Spoken Prompt Dataset for Instruction-Following},
  booktitle = {Proc. INTERSPEECH 2026},
  year      = {2026},
  pages     = {},
  url       = {https://arxiv.org/abs/2603.09881}
}
```

**For ACL / NeurIPS venues** (natbib, author-year):
```bibtex
@inproceedings{zufle2026dowis,
  title     = {Do What I Say: A Spoken Prompt Dataset for Instruction-Following},
  author    = {Z{\"u}fle, Maike and Papi, Sara and Retkowski, Fabian and Mazurek, Szymon
               and Kasztelnik, Marek and Waibel, Alexander and Bentivogli, Luisa
               and Niehues, Jan},
  booktitle = {Proceedings of INTERSPEECH 2026},
  year      = {2026},
  url       = {https://arxiv.org/abs/2603.09881}
}
```

**Before official publication** (cite as arXiv preprint):
```bibtex
@misc{zufle2026dowis,
  title         = {Do What I Say: A Spoken Prompt Dataset for Instruction-Following},
  author        = {Z{\"u}fle, Maike and Papi, Sara and Retkowski, Fabian and Mazurek, Szymon
                   and Kasztelnik, Marek and Waibel, Alexander and Bentivogli, Luisa
                   and Niehues, Jan},
  year          = {2026},
  eprint        = {2603.09881},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
```
