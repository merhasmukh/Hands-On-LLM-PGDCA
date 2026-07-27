# 2.3 System Prompts, Roles & Context Window Management

Modern LLM APIs (especially chat-based models like GPT-4 or Claude 3) use a structured format to handle conversations. This structure relies on "Roles."

## Roles in Chat Completions

A typical conversation payload is structured as an array (or list) of message objects, where each message has a specific role:

1. **System Role (`system`):**
   * Acts as the core instruction set or "persona" for the model. 
   * It dictates the overall behavior, tone, rules, and constraints for the entire conversation. 
   * Example: *"You are a helpful, senior Python developer. Always provide code with extensive comments and avoid using external libraries unless explicitly asked."*
2. **User Role (`user`):**
   * Represents the human interacting with the model. This contains the prompt, question, or task.
3. **Assistant Role (`assistant`):**
   * Represents the model's previous responses. 
   * By passing previous assistant messages back to the API, you give the model "memory" of the conversation history.

## Context Window Management

The **Context Window** is the maximum number of tokens (input + output) a model can process in a single request. 

### Why it matters:
* If your conversation history grows too large, you will exceed the context window and the API will throw an error.
* Even if you don't exceed the limit, sending large amounts of text costs more money and increases latency.

### Strategies for managing context:
1. **Truncation:** The simplest method. Simply drop the oldest messages in the conversation array (except the System Prompt) when the token count reaches a certain threshold.
2. **Summarization:** Periodically use a separate LLM call to summarize the conversation history, then replace the long history with the short summary.
3. **Retrieval Augmented Generation (RAG):** Instead of stuffing the prompt with massive documents, store documents in a database, search for only the relevant chunks based on the user's query, and inject only those chunks into the context window.

---

[Next Topic: Streaming & Asynchronous API Calls](./04-streaming-and-async.md)
