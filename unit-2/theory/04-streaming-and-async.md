# 2.4 Streaming & Asynchronous API Calls

As LLM applications grow more complex, performance and user experience become critical. Two key concepts for improving these are Streaming and Asynchrony.

## Streaming

Standard LLM API calls are **synchronous blocking calls**. Your application sends a request, waits in silence for the entire output to be generated (which can take 10-30 seconds for long responses), and then receives the full payload.

**Streaming** solves this UI bottleneck. 
* Similar to how ChatGPT types out text word-by-word, streaming APIs use Server-Sent Events (SSE) to send back tokens as soon as they are generated.
* **Metric:** Time-To-First-Token (TTFT). Streaming drastically reduces TTFT, making the application feel much faster and more responsive to the user, even if the total generation time is exactly the same.
* **Implementation:** In Python SDKs, this is often done by setting `stream=True` in the API call and iterating over the response object.

## Asynchronous API Calls

If your application needs to make multiple API calls (e.g., summarizing 5 different articles), doing them sequentially (one after the other) is very slow. 

**Asynchronous Programming (Async)** allows your application to execute multiple tasks concurrently.
* Instead of waiting for API Call A to finish before starting API Call B, your application fires off A, immediately fires off B, and then waits for both to return.
* In Python, this is achieved using the `asyncio` library and specialized async clients provided by LLM vendors (e.g., `AsyncOpenAI`).
* **Warning:** While Async makes your application faster, it drastically increases the rate at which you hit the provider's API limits. 

---

[Next Topic: Batch Processing, Rate Limits & Cost Budgeting](./05-batch-processing-and-rate-limits.md)
