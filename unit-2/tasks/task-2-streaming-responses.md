# Task 2: Streaming Responses & TTFT

**Objective:** Implement a streaming API call to improve perceived latency (Time-To-First-Token).

**Instructions:**
1. Write a Python script to send a prompt that requires a long response. Example: *"Write a 5-paragraph essay on the history of the Roman Empire."*
2. **Part A (Synchronous):** Make a standard (non-streaming) API call. Use Python's `time` module to measure how long it takes from sending the request to printing the final output.
3. **Part B (Streaming):** Make the same API call, but enable streaming (`stream=True` in OpenAI, or equivalent in other SDKs).
4. Iterate over the stream chunk by chunk, printing the characters to the console as they arrive (`print(chunk, end="", flush=True)`).
5. Measure and print the **Time-To-First-Token (TTFT)** — the time it takes to receive the very first chunk.

**Deliverable:**
Submit your `.py` script. Include a comment at the top of your script listing the total generation time (Part A) versus the Time-To-First-Token (Part B).
