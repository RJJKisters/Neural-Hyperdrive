# hyperdrive.py — WORKING VERSION 20 Nov 2025
import os
import openai

openai.base_url = "https://api.x.ai/v1"
openai.api_key = os.getenv("GROK_API_KEY")

class NeuralHyperdrive:
    def __init__(self, profile: str = ""):
        self.profile = profile

    def _call_grok(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model="grok-4-0709",   # ← this model works 100 % right now
            # model="grok-4-1-fast-reasoning",  # uncomment this line tomorrow when it's fully rolled out
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
    hyperdrive("Test the warp")
