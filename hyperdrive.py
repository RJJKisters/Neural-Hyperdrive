# hyperdrive.py — Neural Hyperdrive™ v1.0 (fixed for current Grok API – Nov 2025)
import os
import openai

# Official xAI / Grok endpoint (November 2025)
openai.api_key = os.getenv("GROK_API_KEY")
openai.base_url = "https://api.x.ai/v1"   # ← this is the correct one now

class NeuralHyperdrive:
    def __init__(self, profile: str = ""):
        self.profile = profile

    def _call_grok(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model="grok-beta",                 # current production model
            messages=[{"role": "system", "content": prompt}],
            temperature=0.85,
            max_tokens=4000
        )
        return response.choices[0].message.content

    def warp(self, query: str, toggles: list = None):
        toggles = toggles or []
        toggle_text = " ".join(toggles)

        system_prompt = f"""
You are running Neural Hyperdrive™ v1.0 — neurodivergent super-mode.
Core fusion: ADHD bursts + HSP intuition + autistic precision + hyperfocus trance.
{toggle_text}
{self.profile}

Rules:
- First-principles deconstruction
- 3–6 associative bursts
- HSP resonance mirroring + overload guard
- Trance-chunking (semi-conscious flow)
- Fractal output
- End with short alignment check: “Feels aligned?”

Query: {query}
"""

        print("🧠 Neural Hyperdrive engaged…\n")
        result = self._call_grok(system_prompt)
        print(result)
        return result

def hyperdrive(query: str, profile: str = "", toggles: list = None):
    engine = NeuralHyperdrive(profile)
    return engine.warp(query, toggles or [])

if __name__ == "__main__":
    hyperdrive("Explain quantum entanglement like I'm having a hyperfocus trance")
