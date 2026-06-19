# Models Directory

Place model-specific wrappers, API connection handlers, and inference helpers here.

---

## Interface Convention

All model wrappers **must implement** the following common interface so you can
swap models without touching the main runner or evaluation loop:

```python
class BaseModelWrapper:
    """Abstract interface every model wrapper must implement."""

    def __init__(self, model_id: str, device: str = "cuda", **kwargs):
        """Load and initialise the model.

        Args:
            model_id: Hugging Face model ID, local path, or API endpoint.
            device:   'cuda', 'cpu', or 'mps' (Apple Silicon).
            **kwargs: Additional model-specific config (e.g. torch_dtype,
                      trust_remote_code, quantization_config).
        """
        raise NotImplementedError

    def generate(self, prompt: str | list, context: dict | None = None, **kwargs) -> str | list:
        """Run inference and return a prediction.

        Args:
            prompt:  A text string, audio array, or list thereof.
            context: Optional dict carrying additional inputs (e.g. audio waveform,
                     image tensor, reference text).
            **kwargs: Generation params (max_new_tokens, temperature, etc.).

        Returns:
            A string prediction, or a list of strings if prompt is batched.
        """
        raise NotImplementedError
```

---

## Naming & Structure

```
models/
├── base_wrapper.py       # Abstract BaseModelWrapper (interface above)
├── hf_causal_lm.py       # Wrapper for any HuggingFace CausalLM
├── hf_speech_encoder.py  # Wrapper for speech-to-text models (Whisper, etc.)
├── api_wrapper.py        # Wrapper for API-based models (OpenAI, Gemini, etc.)
└── README.md             # This file
```

---

## Guidelines

- **Document weight sources**: record the Hugging Face model ID (e.g.
  `Unbabel/wmt22-cometkiwi-da`) or the exact DOI / URL for every checkpoint.
- **Log generation parameters** (temperature, top-p, max tokens, seed) in
  `evaluation/outputs/metrics.json` alongside metric scores.
- **Never hardcode API keys** in model files — use environment variables or a
  `.env` file (which is git-ignored).
