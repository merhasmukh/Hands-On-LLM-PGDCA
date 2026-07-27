# Task 1: Parameter Tuning Experiments

**Objective:** Understand how generation parameters (`temperature` and `top_p`) affect the output of an LLM.

**Instructions:**
1. Write a Python script using your preferred LLM API (e.g., OpenAI, Gemini, or Claude).
2. Create a creative prompt, for example: *"Write a short, two-sentence story about a robot discovering a flower."*
3. Create a loop that calls the API multiple times with the exact same prompt, but with varying `temperature` settings: `0.0`, `0.5`, `1.0`, and `1.5` (if supported by your model).
4. Print the output for each temperature setting side-by-side.
5. Repeat the experiment, keeping temperature at a default value (e.g., `1.0`), but varying `top_p`: `0.1`, `0.5`, `0.9`.

**Deliverable:**
Submit your `.py` script and a short markdown document (`results.md`) comparing the outputs. Specifically, note the predictability/randomness differences between Temperature 0.0 and Temperature 1.5.
