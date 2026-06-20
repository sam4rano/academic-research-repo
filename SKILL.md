---
name: academic-research-eval
description: |
  Custom skill for reproducing, studying, evaluating, analyzing, and initiating academic research projects, papers, benchmarks, datasets, evaluation pipelines, and research codebases. Use this skill when analyzing existing work or planning/initializing a new research project, formulating hypotheses, designing evaluation setups, and defining key research questions.
---

# Research Paper Analyst Skill

A comprehensive skill for deeply analysing existing research papers/repos AND planning new research.

---

## TASK ROUTING

Determine which mode the user needs:

| Signal | Mode |
|--------|------|
| URL to paper / repo / dataset | → **MODE A: Analyse Existing Research** |
| "I want to write a paper about X" | → **MODE B: Plan New Research** |
| "Compare X with Y" | → **MODE A** for both, then synthesise |
| "Help me design experiments" | → **MODE B, Phase 3** |
| "What metrics should I use for X" | → **MODE B, Phase 3.4** |

---

## MODE A: ANALYSE EXISTING RESEARCH

### Step 1 — Gather the Material

1. If a GitHub repo is given, fetch: README.md, main.py (or equivalent entry point), eval scripts, any JSON stats files, and paper references
2. If a paper URL/arXiv ID is given, fetch the full HTML version (prefer arXiv HTML over PDF for parsing)
3. If a HuggingFace dataset is given, fetch the dataset card (README.md)

**Fetch order of priority:**
```
arXiv HTML   →   README.md   →   eval scripts   →   data schemas   →   config files
```

### Step 2 — Fill the Analysis Template

Use the `Research_Paper_Analysis_Template.md` structure. Work through ALL sections in order:

1. **Paper Identity** — title, authors, venue, year, domain, license, repo, dataset
2. **Problem Statement** — gap, motivation, prior limitations, research questions
3. **Key Contributions** — precise, numbered list
4. **Method/System Design** — pipeline steps as Input→Transform→Output table
5. **Dataset** — schema, size, collection, quality control, statistics
6. **Experiments** — models, variables, compute, metrics
7. **Results** — main table + per-finding evidence
8. **Analysis** — sub-analyses, figures, counterintuitive results
9. **Strengths/Weaknesses** — honest assessment
10. **Relevance** — how it connects to the user's own work

### Step 3 — Extract the Data Schema(s)

For every JSON, CSV, or structured file in the repo:
- Document all fields with types and descriptions
- Identify what each field tracks and why
- Note any derived/computed fields vs raw collected data

Example pattern (from `audio_prompts_statistics.json` in DOWIS):
```json
{
  "language": "de",
  "num_male_speakers": 2,
  "num_female_speakers": 2,
  "speaker_avg_duration_min": 8,
  "total_duration_min": 33
}
```

### Step 4 — Map the Evaluation Pipeline

Build a metrics table covering every task in the paper:

| Task | Metric | Tool | Direction | Human Correlation? |
|------|--------|------|-----------|-------------------|
| | | | ↑/↓ | |

### Step 5 — Identify Research Gaps

After analysis, always surface:
1. What the paper explicitly lists as future work
2. What the paper doesn't address (your read)
3. What could be extended / replicated / applied elsewhere

### Step 6 — Produce Deliverables

Generate the following for the user:

- **Deep Dive .md** — Complete end-to-end breakdown (follow `DOWIS_Research_Deep_Dive.md` as format reference)
- **Filled Analysis Template** — `Research_Paper_Analysis_Template.md` pre-populated
- **Research Skill** (if requested) — a `SKILL.md` capturing the methodology for re-use

---

## MODE B: PLAN NEW RESEARCH

Follow the phases in `New_Research_Paper_Planning_Guide.md`:

| Phase | Focus | Key Output |
|-------|-------|-----------|
| 0 | Problem discovery | Gap statement + RQs |
| 1 | Contribution design | Contribution statement |
| 2 | Dataset/system design | Collection protocol |
| 3 | Experiment design | Hypothesis matrix + metrics table |
| 4 | Implementation | Repo structure + stats schema |
| 5 | Analysis | Figure plan + table plan |
| 6 | Paper writing | Abstract draft + **venue-specific** structure |
| 7 | Submission/release | Dataset card + code README |

When the user describes their idea, always:
1. First check if it's truly novel (ask them to do a literature search if needed)
2. Help them sharpen the contribution statement before anything else
3. Design the evaluation before designing the method (metric-first thinking) — see **Phase 3.4** of `New_Research_Paper_Planning_Guide.md` for the full metric-selection procedure
4. **Ask which venue they're targeting** — this determines page limits, mandatory sections, citation style, and LaTeX template (see Phase 6 of the planning guide)

---

## UNIVERSAL QUALITY STANDARDS

Apply these across both modes:

### Evaluation Metric Selection Principles
- Prefer metrics that correlate with human judgement (cite the correlation study)
- Prefer reference-free metrics when references aren't available (e.g., CometKiwi > BLEU for MT)
- For generation tasks: use at least one automatic metric + note human eval limitations
- Always report metric direction (↑ / ↓) and what range is "good"

### Common NLP/Speech Metrics Quick Reference

| Task | Standard Metric | Tool | Notes |
|------|----------------|------|-------|
| ASR | WER ↓ | jiwer | Word Error Rate |
| MT / ST | CometKiwi ↑ | unbabel-comet | Reference-free, human-correlated |
| MT / ST (legacy) | BLEU ↑ | sacrebleu | Requires references; known limitations |
| Summarisation | BERTScore ↑ | bert-score | Semantic similarity; use `deberta-xlarge-mnli` |
| Summarisation | ROUGE ↑ | rouge-score | N-gram overlap; less semantic |
| QA | F1 / EM ↑ | squad-style | Exact match + token overlap |
| Text gen (quality) | Perplexity ↓ | LM eval | — |
| Speech quality | UTMOS ↑ | UTMOS | Mean Opinion Score proxy |
| Speech quality | PESQ ↑ | pesq | Reference-based |
| Segmentation | Collar-F1 ↑ (±3s) | pyannote.metrics | Boundary accuracy with tolerance |
| NER / parsing | F1 ↑ | seqeval | Entity/token classification |
| Classification | Accuracy / F1 | sklearn | Use macro-F1 for imbalanced |

### Reproducibility Non-Negotiables

Every research project MUST document:
1. Random seed(s) used
2. All library versions (requirements.txt or pyproject.toml)
3. Model name + version + source (HuggingFace ID or DOI)
4. Hardware spec (GPU model + VRAM)
5. Preprocessing parameters (with exact values, not just tool names)
6. How to reproduce results with one command

### Dataset Design Principles (from DOWIS)

| Principle | Description |
|-----------|-------------|
| Decouple prompts from data | Keep instructions separate from task inputs — enables reuse with any benchmark |
| Parallel modalities | If comparing conditions, have exact parallel versions (same content, different form) |
| Multiple styles/variants | At least 5–10 variants per condition to avoid single-phrasing bias |
| Native speakers for multilingual | Avoid machine translation for prompt wording; use native speaker adaptation |
| Human recording > synthesis | For audio data, human recording is more realistic than TTS |
| Document VAD parameters | Silence trimming thresholds, window size, padding — all must be reproducible |
| Per-split statistics | Always report per-split stats (not just total); include demographics |

---

## DELIVERABLE TEMPLATES

Three documents are part of this skill suite:

| File | Purpose | When to Use |
|------|---------|-------------|
| `DOWIS_Research_Deep_Dive.md` | Reference example of a complete paper breakdown | Study template; shows what depth looks like |
| `Research_Paper_Analysis_Template.md` | Blank template to fill for any paper | MODE A — fill this for every paper analysed |
| `New_Research_Paper_Planning_Guide.md` | Phase-by-phase research planning guide | MODE B — follow phases when planning new work |
| `Multi_Paper_Comparison_Tracker.md` | Comparison tracker for surveying multiple papers and tracking active experiment runs side-by-side | Use to track experiment runs, ablations, prompt styling metrics, and submissions |

---

## COMMON PITFALLS TO FLAG

Warn the user if you detect any of the following:

| Pitfall | Signal | Advice |
|---------|--------|--------|
| Single-metric evaluation | Paper reports only one metric | Suggest at least 2 metrics from different families |
| Closed dataset | Data not publicly available | Flag reproducibility risk |
| No baseline | No comparison to prior work | Suggest adding competitive baselines |
| Only aggregate results | No per-subgroup breakdown | Suggest per-language / per-style / per-domain breakdown |
| Informal = bad (undiagnosed) | Informal prompts underperform without acknowledgement | This is a known issue (DOWIS finding) — cite it |
| Text-only evaluation of speech model | Evaluating SLLM with only text prompts | Direct citation: DOWIS shows this overestimates performance |
| Single prompt per task | Only one wording tested | Use 5–10 variants to check prompt sensitivity |
| Wrong citation style for venue | Using `\citet`/`\citep` in IEEE venue, or numbered `[1]` in ACL venue | Check venue-specific citation style in Phase 6 of planning guide |
| Missing mandatory sections | No "Limitations" section in ACL submission, no "Broader Impact" in NeurIPS | Cross-check Phase 6.7 mandatory sections checklist before submission |
| arXiv cited when published version exists | `@misc` used for a paper that was published at a conference/journal | Always cite the published version; update your `.bib` file before submission |
| Page limit violation | Paper exceeds venue page limit | Check Phase 6.4 — INTERSPEECH is 4 pages, ICASSP is 4+1, ACL long is 8, etc. |

---

## REFERENCE PAPERS

Key papers to cite when relevant:

| Topic | Paper | Notes |
|-------|-------|-------|
| Spoken prompt evaluation | DOWIS (Züfle et al., 2026) arXiv:2603.09881 | First multilingual spoken prompt dataset |
| MT evaluation | CometKiwi (Rei et al., 2023) | Reference-free MT quality estimation; EACL 2023 best paper |
| Semantic similarity | BERTScore (Zhang et al., 2020) | Better than ROUGE for generation; use `deberta-xlarge-mnli` model |
| Speech quality | UTMOS (Saeki et al., 2022) | Automatic MOS prediction |
| ASR evaluation | jiwer library | WER computation |
| Audio segmentation | pyannote.metrics / Collar-F1 | Boundary evaluation |
| Multilingual speech data | FLEURS (Conneau et al., 2022) | 102-language speech dataset |
| Prompt diversity | MCIF (various) | Multilingual conversational IF |
