# Task 4: Rate-Limit Handling & Batch Processing

**Objective:** Build resilience into your LLM scripts by handling API rate limits gracefully.

**Instructions:**
1. **The Retry Decorator:** Write a custom Python decorator (or use a library like `tenacity` or `backoff`) that implements **Exponential Backoff**. If an API call fails with a Rate Limit Error (`429 Too Many Requests`), the decorator should catch the error, sleep for 1 second, and retry. If it fails again, sleep for 2 seconds, then 4, etc.
2. **Simulate a Rate Limit:** Write a script that fires off 20 asynchronous requests simultaneously (using the skills from Task 3) to intentionally trigger a rate limit error from your API provider. 
3. Apply your decorator to the API calling function and watch it successfully handle the `429` errors and eventually complete all 20 requests without crashing the script.

**Deliverable:**
Submit your `.py` script demonstrating the working exponential backoff logic.
