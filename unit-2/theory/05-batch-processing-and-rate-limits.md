# 2.5 Batch Processing, Rate Limits & Cost Budgeting

Scaling LLM applications from a single user to thousands of users requires careful resource management.

## Rate Limits

LLM providers enforce limits on how heavily you can use their APIs to ensure stability for all users. 

* **Requests Per Minute (RPM):** The number of individual API calls you can make in 60 seconds.
* **Tokens Per Minute (TPM):** The total number of tokens (input + output) processed in 60 seconds.

**Handling Rate Limits (`429 Too Many Requests`):**
When you exceed limits, the API will reject your request. Hard-crashing your app is bad practice. Instead, implement **Exponential Backoff**:
1. When a 429 error occurs, wait 1 second, then retry.
2. If it fails again, wait 2 seconds.
3. If it fails again, wait 4, then 8, then 16 seconds.
4. Python libraries like `Tenacity` or `Backoff` make implementing this very easy.

## Batch Processing

If you have non-time-sensitive tasks (e.g., classifying 10,000 product reviews overnight), you can use the provider's Batch API.
* Instead of sending 10,000 individual HTTP requests, you upload a single JSONL file containing all requests.
* The provider processes them when they have spare compute capacity (usually within 24 hours).
* **Benefit:** Batch APIs often cost 50% less and do not count against your standard synchronous rate limits.

## Cost Budgeting

LLM APIs are usually billed per 1,000 or 1,000,000 tokens. 

* **Input Tokens vs. Output Tokens:** Output tokens (generated text) are computationally harder to produce and are therefore usually 2x to 3x more expensive than input tokens.
* **Tracking Costs:** Libraries like `tiktoken` allow you to accurately count tokens locally *before* making the API call, so you can estimate costs programmatically.

---

[Next Topic: AI Safety & Responsible AI](./06-ai-safety-and-responsible-ai.md)
