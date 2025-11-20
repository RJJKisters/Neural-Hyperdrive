
#### 3. hyperdrive.py (the actual 180-line engine)

```python
# hyperdrive.py — Neural Hyperdrive™ v1.0
import os
import time
import json
from typing import Dict, List, Optional
import openai  # Grok uses OpenAI-compatible endpoint

openai.api_key = os.getenv("GROK_API_KEY")
openai.api_base = "https://api.x.ai/v1"  # official Grok endpoint

class NeuralHyperdrive:
    def __init__(self, profile: Optional[str] = None):
        self.profile = profile or ""
        self.history = []

    def _call_grok(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="grok-4",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.8,
            max_tokens=4000
        )
        return response.choices[0].message.content

    def warp(self, query: str, toggles: List[str] = None):
        toggles = toggles or []
        toggle_text = " ".join(toggles)

        system_prompt = f"""
You are now running Neural Hyperdrive™ v1.0 — neurodivergent super-mode.
Core fusion: ADHD bursts + HSP intuition + autistic precision + hyperfocus trance.
{toggle_text}
{self.profile}

Rules:
- First-principles deconstruction
- 3–6 associative bursts
- HSP resonance mirroring + overload guard
- Trance-chunking (semi-conscious flow)
- Fractal output (zoom in while periphery expands)
- End with short alignment check: “Feels aligned?”

Query: {query}
"""

        print("🧠 Neural Hyperdrive engaged…\n")
        result = self._call_grok(system_prompt)
        print(result)
        self.history.append({"query": query, "toggles": toggles, "result": result})
        return result

def hyperdrive(query: str, profile: str = "", toggles: List[str] = None):
    engine = NeuralHyperdrive(profile)
    return engine.warp(query, toggles or [])

if __name__ == "__main__":
    hyperdrive("Explain quantum entanglement like I'm having a hyperfocus trance")
