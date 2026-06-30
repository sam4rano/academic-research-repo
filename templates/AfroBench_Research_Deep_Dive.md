# AfroBench: How Good are Large Language Models on African Languages? — Deep Dive

## PAPER IDENTITY

| Field | Value |
|-------|-------|
| **Title** | AfroBench: How Good are Large Language Models on African Languages? |
| **Authors** | Jessica Ojo, Odunayo Ogundepo, Akintunde Oladipo, Kelechi Ogueji, Jimmy Lin, Pontus Stenetorp, David Ifeoluwa Adelani |
| **Venue / ArXiv** | ACL 2025 (Findings) |
| **Venue Type** | NLP conf |
| **Year** | 2023 (v1), updated 2025 (v5, accepted) |
| **Domain** | NLP — Multilingual LLM Evaluation |
| **License** | CC BY 4.0 |
| **Code Repo** | https://github.com/McGill-NLP/AfroBench |
| **Dataset** | 22 existing datasets + new AfriADR dataset |
| **My Reading Date** | 2026-06-30 |
| **Relevance to My Work** | High — comprehensive evaluation methodology for African languages; directly informs benchmark design and multilingual eval best practices |

---

## 1. PROBLEM STATEMENT

### 1.1 The Core Problem
Large-scale multilingual LLM evaluations (e.g., MEGA, Megaverse) include only a handful of African languages due to scarcity of high-quality evaluation data and poor discoverability of existing African datasets. This under-representation means we lack a comprehensive understanding of how LLMs perform across the diverse set of African languages and tasks.

### 1.2 Why Now?
The rapid release of new multilingual LLMs (GPT-4o, Gemini 1.5, LLaMA 3, Gemma 2) requires continuous evaluation, but no existing benchmark covers African languages at breadth (64 languages) and depth (15 tasks). Many African NLP datasets had already been created but were scattered across different repositories — the authors consolidated them.

### 1.3 Prior Work Limitations

| Prior Work | Limitation |
|------------|-----------|
| MEGA / Megaverse | Only 11–16 African languages; limited to POS, NER, XQA tasks |
| ChatGPT-MT | Only MT task; no NLU or reasoning evaluation |
| SIB-200 | Single task (topic classification) |
| Belebele | Only reading comprehension |
| IrokoBench | Only 3 tasks, 16 languages |
| Uhura | Only QA, 6 languages |

### 1.4 Research Questions
1. RQ1: How do current LLMs (proprietary and open) perform across a diverse set of African languages and NLP tasks?
2. RQ2: How does the performance gap between English and African languages compare between proprietary vs. open models?
3. RQ3: How do prompting-based LLM evaluations compare against fine-tuned encoder/encoder-decoder baselines?

---

## 2. KEY CONTRIBUTIONS

1. **AfroBench** — First comprehensive multi-task benchmark spanning **64 African languages**, **15 tasks**, and **22 datasets** (across NLU, QA, knowledge, reasoning, and text generation).
2. **AfriADR** — A new dataset for automatic diacritics restoration across 5 African languages (Ghomálá', Fon, Igbo, Wolof, Yorùbá).
3. **AfroBench-Lite** — A cost-effective subset (14 languages, 7 tasks) for rapid evaluation of new LLMs on the leaderboard.
4. **Extensive empirical evaluation** — 12 LLMs (10 open + 2 proprietary) compared against fine-tuned AfroXLMR, AfriTeVa V2, mT5, and NLLB baselines across all tasks.

---

## 3. METHOD / SYSTEM DESIGN

### 3.1 High-Level Approach
AfroBench is a curated evaluation benchmark, not a new model. The authors aggregated 22 existing datasets covering African languages, added one new dataset (AfriADR), standardized evaluation as text-generation tasks with prompt-based LLM inference, and created a leaderboard using Eleuther LM Evaluation Harness.

### 3.2 Step-by-Step Pipeline

| Step | Input | Transformation | Output |
|------|-------|----------------|--------|
| 1 | Scattered African NLP datasets | Curate, deduplicate, standardize formats | 22 harmonized datasets |
| 2 | Existing MT data (MAFAND) | Strip diacritics → create source/target pairs | AfriADR dataset (5 langs) |
| 3 | Task definitions + prompts | Design 3–5 prompt templates per task | Prompt bank (Appendix H) |
| 4 | Open LLMs | Run via Eleuther LM Eval Harness | Predictions + metrics |
| 5 | Proprietary LLMs (GPT-4o, Gemini) | Custom API prompting framework | Predictions + metrics |
| 6 | Fine-tuned baselines | Train AfroXLMR (NLU), AfriTeVa V2 (gen) | Baseline scores |

### 3.3 Key Design Decisions & Justifications

| Decision | Rationale |
|----------|-----------|
| All tasks as text generation | Unified evaluation framework; avoids task-specific heads |
| 3–5 prompts per task, report best | Mitigates prompt sensitivity; NLU more sensitive than generation |
| AfroBench-Lite subset | Reduces evaluation cost for new models on leaderboard |
| 5-shot (8-shot for Math) | Standard few-shot setting; balances cost vs. performance |
| Fine-tuned baselines | Provides lower-bound comparison vs. specialized models |

---

## 4. DATASET

### 4.1 Dataset Overview

| Dimension | Value |
|-----------|-------|
| **Total datasets** | 22 (9 NLU, 6 text gen, 6 QA/knowledge, 1 reasoning) |
| **Languages** | 64 African languages from 7 language families |
| **New dataset** | AfriADR (5 languages, 7,567 samples) |
| **Splits** | Existing splits from each source dataset |

### 4.2 Task Categories & Datasets

| Category | Tasks | Datasets |
|----------|-------|----------|
| Text Classification | SA, TC, Intent, Hate, NLI | AfriSenti, NollySenti, SIB-200, MasakhaNEWS, Injongo-Intent, AfriHate, AfriXNLI |
| Token Classification | POS, NER | MasakhaPOS, MasakhaNER-X |
| Reasoning | Math | AfriMGSM |
| QA | XQA, RC, Knowledge | AfriQA, Belebele, NaijaRC, Uhura-Arc-Easy, AfriMMLU, MMMLU |
| Text Generation | MT, Summ, ADR | Flores-200, MAFAND, NTREX, SALT, XLSum, AfriADR |

---

## 5. EXPERIMENTS

### 5.1 Models Evaluated

| Model | Type | Size | Category |
|-------|------|------|----------|
| GPT-4o (Aug) | Decoder-only | — | Proprietary |
| Gemini 1.5 Pro 002 | Decoder-only | — | Proprietary |
| LLaMA 2 7B Chat | Decoder-only | 7B | Open |
| LLaMA 3 8B Instruct | Decoder-only | 8B | Open |
| LLaMA 3.1 8B/70B Instruct | Decoder-only | 8B/70B | Open |
| LLaMAX 8B | Decoder-only | 8B | Open |
| AfroLLaMA V1 8B | Decoder-only | 8B | Open |
| Gemma 1.1 7B IT | Decoder-only | 7B | Open |
| Gemma 2 9B/27B IT | Decoder-only | 9B/27B | Open |
| Aya-101 13B | Encoder-decoder (mT5) | 13B | Open |
| AfroXLMR (base) | Encoder-only | ~278M | Fine-tuned baseline |
| AfriTeVa V2 Large | Encoder-decoder (T5) | ~1B | Fine-tuned baseline |
| mT5 Large | Encoder-decoder | ~1B | Fine-tuned baseline |
| NLLB 3.3B | Encoder-decoder | 3.3B | Fine-tuned baseline |

### 5.2 Evaluation Setup

| Variable | Type | Values |
|----------|------|--------|
| Language | independent | 64 African + English + French + Portuguese + Arabic |
| Model | independent | 12 LLMs + 4 fine-tuned baselines |
| Prompt template | independent | 3–5 per task |
| Few-shot examples | independent | 0-shot / 5-shot (8-shot for Math) |
| Performance | dependent | Accuracy, F1, ChrF, BERTScore, EM |

### 5.3 Evaluation Metrics

| Task | Metric | Direction |
|------|--------|-----------|
| POS | Accuracy | ↑ |
| NER | F1 | ↑ |
| SA | F1 | ↑ |
| TC | Accuracy | ↑ |
| Intent | Accuracy | ↑ |
| Hate Speech | F1 | ↑ |
| NLI | Accuracy | ↑ |
| XQA | F1 | ↑ |
| RC | F1 | ↑ |
| Arc-E / MMLU | Accuracy | ↑ |
| Math | Exact Match (EM) | ↑ |
| MT | ChrF | ↑ |
| Summarization | BERTScore | ↑ |
| ADR | ChrF | ↑ |

---

## 6. RESULTS

### 6.1 Main Findings

1. **Proprietary models dominate**: GPT-4o (59.6 avg) and Gemini 1.5 Pro (58.5 avg) outperform best open model (Gemma 2 27B at 48.3) by ~11 points.
2. **Large English vs. African language gap**: GPT-4o scores +25 points higher on English than African languages; Gemma 2 27B gap is even wider at +40+.
3. **Fine-tuned models still beat prompting**: AfroXLMR (NLU avg 70.4) significantly outperforms all prompted LLMs on NLU tasks; NLLB 3.3B (MT avg 40.4) beats most LLMs on translation.
4. **Performance varies by language resource level**: Languages with more monolingual data (Swahili, Yoruba, Hausa) tend to perform better than extremely low-resource languages.

### 6.2 Ablation: AfroBench-Lite

| Finding | Detail |
|---------|--------|
| Strong correlation | AfroBench-Lite scores correlate well with full AfroBench (r > 0.95) |
| Cost reduction | ~5x cheaper to evaluate on Lite vs. full benchmark |

### 6.3 Prompt Sensitivity

NLU tasks show high prompt sensitivity (variation of 5–15 points across prompts), while text generation tasks are more robust.

---

## 7. STRENGTHS

1. **Breadth**: Unprecedented coverage — 64 languages, 15 tasks, 22 datasets — the most comprehensive African language LLM benchmark to date.
2. **Standardization**: All tasks unified under text-generation format with integrated Eleuther LM Eval Harness support.
3. **Cost-effective subset**: AfroBench-Lite enables rapid iteration.
4. **Reproducibility**: Open-source code, leaderboard, and prompt templates.

---

## 8. WEAKNESSES & LIMITATIONS

1. **Cross-contamination risk**: Some LLMs may have been trained on the evaluation datasets (especially popular ones like Belebele, Flores).
2. **Uneven language coverage**: Not all 64 languages are covered in all 15 tasks; per-language granularity varies.
3. **Only text modality**: No speech or multimodal evaluation despite many African languages being primarily spoken.
4. **Single best prompt reporting**: Reporting only the best prompt overestimates practical performance.
5. **English-centric MT**: All MT directions are from English (or French), not language-pair direct translation.

---

## 9. RELEVANCE TO MY RESEARCH

### 9.1 Direct Applicability
- AfroBench's evaluation methodology can be used to benchmark any new LLM for African language capabilities.
- The unified text-generation evaluation paradigm is a template for building multilingual benchmarks.

### 9.2 Inspirations
- AfroBench-Lite concept (sub-setting benchmarks for cost efficiency) is applicable to any large-scale evaluation.
- The approach of consolidating scattered datasets into a unified benchmark could be replicated for other under-represented language groups.

### 9.3 Citations to Follow Up
- Megaverse (Ahuja et al., 2024) — most similar prior work
- IrokoBench (Adelani et al., 2024b) — complementary 3-task African benchmark
- Eleuther LM Evaluation Harness (Gao et al., 2024) — framework used

---

## 10. REPRODUCIBILITY CHECKLIST

| Item | Status | Notes |
|------|--------|-------|
| Code publicly available | ✅ | https://github.com/McGill-NLP/AfroBench |
| Dataset publicly available | ✅ | All 22 datasets on HuggingFace |
| All hyperparameters reported | ✅ | Prompt templates, few-shot counts, model versions in appendix |
| Hardware reported | ✅ | GPU details for fine-tuned baselines |
| Random seeds reported | ⚠️ | Not explicitly mentioned |
| Evaluation scripts provided | ✅ | Eleuther LM Eval Harness integration |
| Pre-trained model weights | N/A | Benchmark, not a model |

---

## 11. HOW TO CITE

```bibtex
@inproceedings{ojo2025afrobench,
  title     = {AfroBench: How Good are Large Language Models on African Languages?},
  author    = {Ojo, Jessica and Ogundepo, Odunayo and Oladipo, Akintunde and
               Ogueji, Kelechi and Lin, Jimmy and Stenetorp, Pontus and
               Adelani, David Ifeoluwa},
  booktitle = {Proceedings of ACL 2025 (Findings)},
  year      = {2025}
}
```

---

## 12. OVERALL RATING

| Dimension | Score (1–5) | Comment |
|-----------|-------------|---------|
| Novelty | 4 | First to consolidate this breadth; AfriADR is new; concept not entirely novel |
| Technical Rigour | 5 | Comprehensive evaluation with multiple prompts, multiple models, cost-effective subset |
| Clarity of Writing | 4 | Well-structured; rich tables |
| Reproducibility | 5 | Fully open-source code, datasets, and prompts |
| Practical Impact | 5 | Immediate utility for anyone evaluating LLMs on African languages |
| **Overall** | **4.6** | Essential benchmark for African NLP |
