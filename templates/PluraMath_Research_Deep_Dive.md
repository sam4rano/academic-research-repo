# PluraMath Research Deep Dive (Reference Guide)

This document serves as a complete paper analysis and reproducibility checklist for the PluraMath (Dementieva et al., 2026) paper.

---

## Paper & Repository Metadata
*   **Paper Title**: PluraMath: Extending Mathematical Reasoning Evaluation Beyond High-Resource Languages
*   **Authors**: Daryna Dementieva, Nikolay Babakov, Kathy Hämmerl, Ilseyar Alimova, Jindřich Libovický, Shu Okabe, Miras Baisbay, Lukas Edman, Abrorkhon Inomkhujaev, Antonia Karamolegkou, Mateusz Lango, Volkan Özer, Nikola Selic, Subhankar Swain, Tsedeniya Kinfe Temesgen, Galit Bary Weisberg, Alexander Fraser
*   **Conference/Journal**: arXiv Preprint (July 2026)
*   **Venue Type**: NLP / CL Conference format
*   **arXiv ID / Link**: [arxiv.org/abs/2607.05992](https://arxiv.org/abs/2607.05992)
*   **GitHub Repository**: [github.com/TUM-NLP/pluramath](https://github.com/TUM-NLP/pluramath)
*   **Hugging Face Dataset**: [huggingface.co/datasets/tum-nlp/PluraMath](https://huggingface.co/datasets/tum-nlp/PluraMath)
*   **Project Page**: [tum-nlp.github.io/pluramath](https://tum-nlp.github.io/pluramath/)
*   **Paper License**: CC BY-SA 4.0 · **Code/Dataset License**: Apache 2.0

---

## 1. Abstract & Core Contribution
*   **Problem Statement**: Existing mathematical reasoning benchmarks (including PolyMath's 18 languages) are heavily biased toward high-resource languages — English and Chinese dominate both pre-training and evaluation. Underrepresented language communities are locked out of benchmarking the reasoning capabilities of LLMs in their own languages.
*   **Core Contribution/Solution**:
    1.  **PluraMath benchmark**: Extends PolyMath to **18 additional underrepresented languages** spanning **6 language families** — from mid-resource (Hindi, Turkish) to extreme low-resource (<15k L1 speakers: Upper/Lower Sorbian). 500 problems per language, 4 difficulty levels (low → top), 9,000 human-validated translations total.
    2.  **Human-curated pipeline**: Three-stage (first-draft translation → native-speaker verification → LaTeX/format QC), fully open-sourced so any community can extend to their language.
    3.  **Large-scale benchmarking**: 27 reasoning LLMs across 4 scales (small ≤4B, mid-size, large open-weight, closed-source) evaluated with difficulty-weighted accuracy (DW-Acc).
    4.  **Translation–reasoning correlation analysis**: chrF++ translation quality correlated with math accuracy (+0.45), instruction-following (+0.35), and output length (-0.16) using FLORES+ dev set and LLMs with Limited Resources shared task translations.
*   **Key Findings**:
    *   Persistent **+2.15 DW-Acc gap** between high-resource and target languages (Spearman ρ = 0.646, p = 0.0038); reaching **+4.86** for Chuvash and Amharic; Greek/Polish nearly on par (+0.67).
    *   **Claude-Haiku-4.5 dominates** (28.7 HR avg / 26.4 target avg), far ahead of all open-weight models. Best open-weight: `gpt-oss-120b` at 22.7 / 16.3.
    *   **Longer reasoning ≠ better reasoning** (r = −0.16): best models produce correct answers with significantly shorter traces.
    *   **Prompting tricks don't close the gap**: English chain-of-thought and back-translation prompting yield limited improvements — the gap reflects capability, not prompt design.
    *   **Translation helps weakly**: chrF++ correlates moderately with math accuracy (+0.45) and instruction-following (+0.35), but not with En-CoT gains (+0.11, p = 0.21) or answer-language choice (rpb = +0.07, p = 0.36).

---

## 2. Dataset Structure & Languages

### 2.1 Benchmark Construction
*   **Base**: PolyMath (Wang et al., 2025) — 4 high-resource source languages: English, German, Russian, Spanish.
*   **Difficulty levels**: `low` (K-12 word problems), `medium` (HS/university exams), `high` (mid-high difficulty competitions), `top` (Olympiad & frontier math). Weights for DW-Acc: `{low: 1, medium: 2, high: 4, top: 8}`.
*   **Size**: 125 problems per level → 500 per language → **9,000 human-validated translations** total.
*   **Format**: Problem statement in target language + gold answer in `\boxed{}` notation (LaTeX).

### 2.2 Languages by Resource Class (18 total + 4 source = 22 eval languages)

| Class | L1 Speakers | Count | Languages (code, family) |
|---|---|---|---|
| PolyMath base (HR reference) | — | 4 | English `en`, German `de`, Russian `ru`, Spanish `es` |
| High-resource | >100M | 2 | Hindi `hi` (IE-Indo-Aryan), Turkish `tr` (Turkic) |
| Mid-resource | 10–100M | 3 | Polish `pl`, Ukrainian `uk` (IE-Slavic), Uzbek `uz` (Turkic) |
| Low-resource | 1–10M | 10 | Odia `or`, Amharic `am` (AA-Semitic), Greek `el`, Kazakh `kk`, Czech `cs`, Hebrew `he` (AA-Semitic), Serbian `sr`, Tatar `tt`, Slovak `sk`, Catalan `ca` |
| Extreme low-resource | <1M (<15k for hsb/dsb) | 3 | Chuvash `cv` (Turkic), Upper Sorbian `hsb`, Lower Sorbian `dsb` (IE-Slavic) |

### 2.3 Data Collection Pipeline
1.  **Stage 1 — Automatic first draft**: Strongest available MT system per language (DeepL, Gemini, Sarvamai, SalamandraTA, TartuNLP) from English/Russian/German/Spanish source.
2.  **Stage 2 — Native-speaker verification**: 18 native-speaker validators thoroughly correct every translation; written instructions, informed about project goals.
3.  **Stage 3 — Quality control**: Automated + manual LaTeX integrity checks; final error analysis.
*   Pipeline is fully open-sourced (scripts, annotation interface, guidelines).

### 2.4 Back-Translation Source Mapping
Used for the `bt` prompting strategy; translates problems back to a PolyMath source language via NLLB, then prompts in the source language:
| Target language | Source language | | Target language | Source language |
|---|---|---|---|---|
| uk, tt, kk, cv | `ru` (Russian) | | hsb, dsb, cs | `de` (German) |
| ca | `es` (Spanish) | | sk, am, el, tr, uz, he, pl, sr, hi, or | `en` (English) |
### 2.5 Language-Specific `\boxed{}` Instructions (from `instructions_prompts.py`)
Each target language has a native-language instruction suffix appended to the problem:

| Code | Language | Instruction |
|---|---|---|
| `am` | Amharic | ማስታወሻ፡ እባክዎ የመጨረሻውን መልስ በ$\boxed{}$ ውስጥ ያስገቡ። |
| `ca` | Catalan | Nota: Si us plau, poseu la resposta final dins de $\boxed{}$. |
| `cs` | Czech | Poznámka: Prosím vložte konečnou odpověď do $\boxed{}$. |
| `cv` | Chuvash | Асӑрхаттару: Юлашки хуравăрăн $\boxed{}$ ӑшне лартăр. |
| `de` | German | Hinweis: Bitte setzen Sie die endgültige Antwort in $\boxed{}$. |
| `dsb` | Lower Sorbian | Glědajśo: Pšosym stajśo kóńcnu wótegrono do $\boxed{}$. |
| `el` | Greek | Σημείωση: Παρακαλώ βάλτε την τελική απάντηση μέσα στο $\boxed{}$. |
| `en` | English | Note: Please put the final answer in the $\boxed{}$. |
| `es` | Spanish | Nota: Por favor, coloque la respuesta final en $\boxed{}$. |
| `he` | Hebrew | הערה: נא לשים את התשובה הסופית בתוך $\boxed{}$. |
| `hi` | Hindi | नोट: कृपया अंतिम उत्तर को $\boxed{}$ में रखें। |
| `hsb` | Upper Sorbian | Kedźbu: Prošu stajće kónčnu wotmołwu do $\boxed{}$. |
| `kk` | Kazakh | Ескерту: Соңғы жауапты $\boxed{}$ ішіне жазыңыз. |
| `or` | Odia | ଟିପ୍ପଣୀ: ଦୟାକରି ଶେଷ ଉତ୍ତରକୁ $\boxed{}$ ଭିତରେ ରଖନ୍ତୁ। |
| `pl` | Polish | Uwaga: Proszę umieścić końcową odpowiedź w $\boxed{}$. |
| `ru` | Russian | Примечание: Пожалуйста, поместите окончательный ответ в $\boxed{}$. |
| `sk` | Slovak | Poznámka: Prosím vložte konečnú odpoveď do $\boxed{}$. |
| `sr` | Serbian | Напомена: Молимо ставите коначан одговор у $\boxed{}$. |
| `tr` | Turkish | Not: Lütfen son cevabı $\boxed{}$ içine yazın. |
| `tt` | Tatar | Искәрмә: Зинһар, соңгы җавапны $\boxed{}$ эченә куегыз. |
| `uk` | Ukrainian | Примітка: Будь ласка, помістіть остаточну відповідь у $\boxed{}$. |
| `uz` | Uzbek | Eslatma: Iltimos, yakuniy javobni $\boxed{}$ ichiga yozing. |

### 2.6 Dataset File Layout (HF Hub)
Each language is a subset containing 4 Parquet files — one per difficulty level:
```
tum-nlp/PluraMath/
├── am/  {low,medium,high,top}-00000-of-00001.parquet   (~28–44 KB each)
├── ca/  ...
├── ...
└── uz/
```
Each row: `id`, `question` (translated), `answer` (gold, `\boxed{}` notation).
Loaded via: `load_dataset("TUM-NLP/PluraMath", "am", split="test")`.

---


## 3. Evaluated Models & Inference Configuration

### 3.1 Model Categories (27 total)
| Scale | Count | Models |
|---|---|---|
| **Small (≤4B)** | 9 | Qwen3.5-0.8B, LFM2.5-1.2B, Ouro-1.4B, R1-Distill-Qwen-1.5B, Qwen3.5-2B, Ouro-2.6B, Ministral-3-3B, Gemma-3-4B, Qwen3.5-4B |
| **Mid-size** | 9 | OLMo-3-7B-Think, R1-0528-Qwen3-8B, Ministral-3-8B, Qwen3.5-9B, Ministral-3-14B, gpt-oss-20b, Nemotron3-Nano-30B, Gemma-4-31B, Qwen3.5-35B-A3B |
| **Large open-weight** | 6 | R1-Distill-Llama-70B, gpt-oss-120b, Qwen3.5-122B-A10B, Qwen3-235B-A22B, DeepSeek-V3.2, Kimi-K2.5 |
| **Closed-source** | 3 | Claude-Haiku-4.5, Gemini-2.5-Flash, GPT-5.4 |

### 3.2 Three Prompting Strategies from the Runner

Each prompt is constructed as: `{question}\n\n{INSTRUCTION[lang]}` (from `run_inference.py:build_user_prompt`):

| Strategy | System Prompt | User Prompt | Question Column |
|---|---|---|---|
| **`base`** | *None* | `{translated_question}\n\n<lang-specific boxed instruction>` | `questions_translated` |
| **`base_encot`** | `"You are solving a mathematical problem. Reason step by step in English, then write the final answer in $\boxed{}$"` | Same as `base` | `questions_translated` |
| **`bt`** (Back-translation) | *None* | `{back_translated_nllb}\n\n<source-lang boxed instruction>` | `questions_back_translated_nllb` |

**Inference constants** (from `run_inference.py`):
- `MAX_COMPLETION_TOKENS = 2000`
- `TEMPERATURE = 0.1`
- `TIMEOUT_SEC = 500`
- `BEDROCK_OPENAI_BASE_URL = "https://bedrock-runtime.eu-west-1.amazonaws.com/openai/v1"`
- Chuvash filename alias: `chv` → instruction key `cv`

**Five providers** with their env-vars / auth:
| Provider | Key Flag | Auth | Notes |
|---|---|---|---|
| `deepinfra` | `--provider deepinfra` | `DEEPINFRA_API_KEY` | OpenAI-compat, base=`api.deepinfra.com/v1/openai` |
| `bedrock` | `--provider bedrock` | `AWS_BEARER_TOKEN_BEDROCK` | OpenAI-compat, eu-west-1 |
| `bedrock_boto3` | `--provider bedrock_boto3` | IAM / `AWS_REGION` | Native boto3 (Nova models) |
| `vllm_remote` | `--provider vllm_remote --url <URL>` | `api_key="EMPTY"` | Docker vLLM v0.20.0 |
| `transformers` | `--provider transformers` | `HF_TOKEN` (optional gated) | Local, `device_map=auto`, bfloat16 |

### 3.3 CSV Output Columns
Each inference output CSV includes:
- `user_prompt`, `system_prompt`, `prompting_strategy` — prompt metadata
- `response` — model's final output (contains `\boxed{...}`)
- `internal_reasoning` — chain-of-thought / think tags

Resumability: checkpoint CSVs written after each batch; runner skips rows already having `response` or `internal_reasoning`.

---

## 4. Runner Logic & Repo Structure (github.com/TUM-NLP/pluramath)

### 4.1 Repo Layout
```
├── run_inference.py                    # Main entry point (single model/provider)
├── inference_class/                    # Provider wrappers (OpenAI-compat, Bedrock boto3, HF Transformers)
├── pluramath_evaluation.py             # Scoring pipeline (→ pluramath_pipeline.py in README)
├── instructions_prompts.py             # Language-specific \boxed{} instruction suffixes
├── backtranslation_preprocessing/
│   └── language_to_source_language_map.json
├── final_data/                         # PluraMath workbooks (.xlsx), base + En-CoT
├── final_data_back_translated/         # Workbooks with NLLB back-translations
├── check_latex.ipynb                   # LaTeX integrity checking
├── run_main_experiment_api.sh          # API launcher (deepinfra, Bedrock)
├── run_main_experiment_vllm.sh         # vLLM remote launcher
├── run_main_experiment_transformers.sh  # Detached local Transformers launcher
├── run_main_experiment_transformers_foreground.sh  # Foreground (Slurm-compatible)
├── run_sbatch_transformers.sh          # Example Slurm/A40 submission
├── requirements.txt
└── Dockerfile? (Docker via vLLM v0.20.0)
```

### 4.2 Direct Runner Usage
```bash
# API-backed (deepinfra)
python run_inference.py --model_name_full openai/gpt-oss-120b --model_name_short gpt-oss-120b \
  --provider deepinfra --dataset_paths final_data/pluramath_en.xlsx --prompting_strategy base \
  --reasoning_effort medium --temperature 0.1 --batch_size 10

# vLLM remote
python run_inference.py --model_name_full Qwen/Qwen2.5-7B-Instruct --model_name_short qwen2.5-7b-instruct \
  --provider vllm_remote --url http://host:port/v1 --dataset_paths final_data/pluramath_en.xlsx

# Local Transformers
python run_inference.py --model_name_full Qwen/Qwen2.5-7B-Instruct --model_name_short qwen2.5-7b-instruct \
  --provider transformers --prompting_strategy base --batch_size 1 --transformers_device_map auto
```

### 4.3 Output and Resumability
*   Output: `experiment_output/<strategy>/<lang>/<model_short>.csv`
*   Checkpoints: `.../<model_short>.checkpoint.csv` (resumable, skips completed rows)
*   Logs: `logs/` directory
*   Stops dataset if ≥5% rows fail

---

## 5. Metric Functions & Evaluation Pipeline

`pluramath_pipeline.py` (a.k.a. `pluramath_evaluation.py`) is a self-contained module:

```bash
# Score one results folder → per-language xlsx (per-level + DW-ACC) + optional JSON
python pluramath_pipeline.py score RESULTS_DIR -o scores_out/ [--json] [--fraction]

# Combine prompt conditions into comparison workbook
python pluramath_pipeline.py combine STRATEGY_ROOT -o combined.xlsx --conditions base base_encot bt

# Extra: boxed-format compliance, output language (langdetect), token-lengths
python pluramath_pipeline.py extra RESULTS_DIR -o extra_out/ [--tokenizer Qwen/Qwen3-4B]

# Length stats workbook + LaTeX table
python pluramath_pipeline.py lengths RESULTS_DIR -o lengths_out/ [--part total|reasoning|answer]
```

### Metrics Summary

| Metric | Definition | Tool / Notes |
|---|---|---|
| **DW-Acc** (Difficulty-Weighted Accuracy) | Exact match of last `\boxed{...}` (brace-balanced) vs. gold, weighted {low:1, med:2, high:4, top:8}. | LaTeX-aware normalization + numeric fallback |
| Per-level accuracy | Unweighted accuracy per difficulty level | — |
| Boxed-format compliance % | Whether model output contains valid `\boxed{...}` | — |
| Output language | Dominant language of reasoning/answer (target `tl` vs. English `en`) | `langdetect`; optional |
| Generation length | Mean ± std of answer/reasoning length in **tokens** | LLM tokenizer (default: `Qwen/Qwen3-4B`) |
| chrF++ | Translation quality (FLORES+ `dev` split) | Correlated with math accuracy r = +0.45 |

---

## 6. Top Results Snapshot (Base Prompting, DW-Acc %)

| Model | HR Avg | Target Avg | Gap | Notes |
|---|---|---|---|---|
| **Claude-Haiku-4.5** | **28.7** | **26.4** | **+2.3** | Dominant across all languages; short output (848/934 tok) |
| gpt-oss-120b | 22.7 | 16.3 | +6.4 | Best open-weight; much longer output (2590/2328 tok) |
| GPT-5.4 | 16.2 | 15.7 | +0.5 | Most stable (gap <1); shortest output (317/371 tok) |
| DeepSeek-V3.2 | 10.1 | 9.5 | +0.6 | Very stable; all-tl output |
| Ministral-3-8B | 10.0 | 7.5 | +2.5 | — |
| Gemma-3-4B | 10.6 | 6.8 | +3.8 | Best small model |

*   **Worst-performing languages**: Upper/Lower Sorbian, Chuvash, Amharic (many models near 0% DW-Acc).
*   **Nearly at parity**: Greek (+0.67 gap), Polish (+0.67), Czech.
*   **Only Qwen3.5-4B beats 0% on all 22 languages** among small models; many models get 0.0–0.1% on Chuvash/Sorbian.

---

## 7. Translation–Reasoning Correlation Analysis

Case study using FLORES+ `dev` translations and LLMs with Limited Resources shared task:

| Metric pair | r / rpb | p-value | Interpretation |
|---|---|---|---|
| chrF++ vs Math accuracy | **+0.45** | <10⁻⁸ | Moderate — translation helps task reliability |
| chrF++ vs Instruction following | **+0.35** | <10⁻⁴ | Moderate — reliable models are reliable across-tasks |
| chrF++ vs Output length | **−0.16** | <0.01 | Weak negative — longer traces don't help |
| chrF++ vs En-CoT gains | +0.11 | 0.21 | None — En-CoT doesn't depend on MT quality |
| chrF++ vs Answer in English vs target | +0.07 | 0.36 | None — answer-language choice not MT-driven |
| chrF++ vs Language resource class | +0.08 | 0.36 | None — MT quality class-independent |

**Key insight**: Translation ability is a proxy for general task reliability, not a direct mechanism for multilingual reasoning. Other cross-lingual reasoning mechanisms play a larger role.

---

## 8. Key Findings: Qualitative Dimensions
*   **Reasoning quality degrades in underrepresented languages**: Human eval across 6 criteria shows frequent mid-reasoning switches to English, less coherent derivations, and unfinished reasoning within token budget.
*   **Format compliance varies widely**: Some models rarely produce `\boxed{}` in low-resource languages (LFM2.5-1.2B: 0% on many); Claude-Haiku-4.5 maintains near-perfect compliance.
*   **Prompting interventions have limited effect**: En-CoT and back-translation yield only marginal gains for most models — the gap is a capability issue, not a prompt-design issue.

---

## 9. Synthesis, Gaps & Next Steps

| Dimension | Detail |
|---|---|
| **Limitations identified by paper** | Dataset may contain overlooked errors (PRs welcome); human eval across 6 criteria reveals reasoning degradation in low-resource langs; 4 base source languages constrain what can be back-translated; En-CoT and bt prompting don't close the gap. |
| **Open gaps (your read)** | No multi-turn or tool-augmented reasoning evaluation; no native-speaker evaluation of model outputs (only translations verified); translation engines limited to strongest-available per language (some may be weak); no African language outside the AA-Semitic pair (Amharic, Hebrew) and no Nilo-Saharan/Niger-Congo representation at all; no code generation / proof verification tasks. |
| **Actionable next steps** | (1) Extend to African language families (Swahili, Zulu, Hausa, Yoruba) using the open-sourced pipeline; (2) Add native-speaker quality ratings of model-generated reasoning (not just translation quality); (3) Test whether En-CoT + stronger translation (GPT-5.4-level) closes the gap where baseline MT is weak; (4) Study whether language-specific tokenizer coverage correlates with reasoning degradation. |

---

## 10. Reproducibility Checklist

| Item | Status | Notes |
|---|---|---|
| Code publicly available | ✅ | [github.com/TUM-NLP/pluramath](https://github.com/TUM-NLP/pluramath) (Python 98.6%, Jupyter 1.1%, Shell 0.3%) |
| Dataset publicly available | ✅ | [tum-nlp/PluraMath](https://huggingface.co/datasets/tum-nlp/PluraMath) (Apache 2.0, 9k rows, 18 subsets, Parquet) |
| Pre-trained model weights | ✅ | All 27 models are public HF checkpoints or API-based |
| Random seed reported | ✅ | `temperature: 0.1` for evaluation; explicit `seed` not in runner args? (check `run_inference.py`) |
| All hyperparameters reported | ✅ | `reasoning_effort: medium`, `temperature: 0.1`, `batch_size: 1–15`, `torch_dtype: auto/bfloat16` per launcher |
| Hardware / compute budget reported | ⚠️ | A40 GPU mentioned in Slurm script; API costs in paper appendix (not in the web resources captured) |
| Evaluation scripts provided | ✅ | `pluramath_evaluation.py` + `check_latex.ipynb` |
| Statistical significance testing | ✅ | Spearman ρ with p-values for language resource class correlation; Pearson r + p-values for all chrF++ correlations |
| Human annotation details reported | ✅ | 18 native-speaker validators named; written instructions; pipeline fully described |

---

## 11. BibTeX Citation

**For arXiv preprint (current status):**
```bibtex
@misc{dementieva2026pluramath,
  title         = {{PluraMath}: Extending Mathematical Reasoning Evaluation
                   Beyond High-Resource Languages},
  author        = {Dementieva, Daryna and Babakov, Nikolay and H{\"a}mmerl, Kathy
                   and Alimova, Ilseyar and Libovick{\'y}, Jind{\v{r}}ich and
                   Okabe, Shu and Baisbay, Miras and Edman, Lukas and
                   Inomkhujaev, Abrorkhon and Karamolegkou, Antonia and
                   Lango, Mateusz and {\"O}zer, Volkan and Selic, Nikola and
                   Swain, Subhankar and Temesgen, Tsedeniya Kinfe and
                   Weisberg, Galit Bary and Fraser, Alexander},
  year          = {2026},
  eprint        = {2607.05992},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi           = {10.48550/arXiv.2607.05992},
}
```

**For ACL / NAACL venues** (natbib, author-year):
```bibtex
@inproceedings{dementieva2026pluramath,
  title     = {{PluraMath}: Extending Mathematical Reasoning Evaluation
               Beyond High-Resource Languages},
  author    = {Dementieva, Daryna and Babakov, Nikolay and H{\"a}mmerl, Kathy
               and Alimova, Ilseyar and Libovick{\'y}, Jind{\v{r}}ich and
               Okabe, Shu and Baisbay, Miras and Edman, Lukas and
               Inomkhujaev, Abrorkhon and Karamolegkou, Antonia and
               Lango, Mateusz and {\"O}zer, Volkan and Selic, Nikola and
               Swain, Subhankar and Temesgen, Tsedeniya Kinfe and
               Weisberg, Galit Bary and Fraser, Alexander},
  year      = {2026},
  url       = {https://arxiv.org/abs/2607.05992}
}
```
