# 2.1 API Keys, Authentication & Request-Response Lifecycle

## Introduction to LLM APIs

Application Programming Interfaces (APIs) allow developers to integrate Large Language Models (like OpenAI's GPT, Anthropic's Claude, or Google's Gemini) directly into their applications without having to train or host the models themselves.

## API Keys and Authentication

To use an LLM API, you must authenticate yourself. This is almost universally done using an **API Key**.

* **What is an API Key?** It is a unique, secret string of characters (like a highly complex password) provided by the LLM vendor.
* **How is it used?** It is passed in the "Headers" of the HTTP request you send to the provider. 

### Security Best Practices for API Keys:
1. **Never hardcode them** directly in your source code.
2. **Use Environment Variables** (e.g., `.env` files) to store them locally.
3. **Do not commit** `.env` files to public repositories like GitHub. Add `.env` to your `.gitignore` file.
4. **Rotate your keys** if you suspect they have been compromised.

## The Request-Response Lifecycle

When you interact with an LLM via API, the interaction follows a standard HTTP Request-Response pattern:

### 1. The Request (Client to Server)
Your application sends an HTTP POST request to the provider's endpoint (e.g., `https://api.openai.com/v1/chat/completions`). 
The request contains:
* **Headers:** Including your Authentication (Bearer Token) and Content-Type (`application/json`).
* **Body (Payload):** The actual data you are sending, typically in JSON format. This includes the model name, your prompt, and optional generation parameters.

### 2. Processing (Server-side)
The provider's servers receive the request, validate your API key, and pass your prompt to the LLM. The LLM processes the input and generates tokens sequentially.

### 3. The Response (Server to Client)
The server sends back an HTTP response containing:
* **Status Code:** (e.g., `200 OK` for success, `401 Unauthorized` for bad API keys, `429 Too Many Requests` for rate limits).
* **Body:** A JSON object containing the model's generated text, usage statistics (how many tokens were used), and a finish reason (e.g., `stop`, `length`).

---

[Next Topic: Parameters: Temperature, Top-p, Stop Sequences, Max Tokens](./02-parameters-temperature-top-p.md)
