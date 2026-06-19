# Configs Directory

Store experiment configuration files here (YAML or JSON format).
Use config files to avoid hardcoding hyperparameters in source code.

## Example config structure (experiment_default.yaml)

```yaml
model:
  id: "Unbabel/wmt22-cometkiwi-da"
  device: "cuda"
  torch_dtype: "float16"

data:
  dataset: "maikezu/dowis"
  split: "test"
  max_samples: null    # null = full split; integer = dry-run subset

training:
  seed: 42
  batch_size: 8
  max_new_tokens: 256
  temperature: 0       # 0 = greedy decoding

output:
  output_dir: "evaluation/outputs"
  save_predictions: true
  save_metrics: true
```

## Convention
- One YAML file per experiment variant.
- Name files descriptively: `exp01_baseline_greedy.yaml`, `exp02_ablation_no_vad.yaml`.
- Pass the config path to `runner.py` with `--config configs/exp01_baseline_greedy.yaml`.
