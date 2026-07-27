# 60-Hour Practical Course Breakdown (20 Practicals)

This folder contains the practical syllabus mapped across four units, totaling exactly 60 hours. 

---

## Unit 1: LLM Foundations (14 hrs — 5 practicals)

| Practical # | Task | Hrs | Notebook Ref |
| :---: | :--- | :---: | :---: |
| **1** | Set up virtual environment, install SDKs (openai, anthropic, google-generativeai), configure API keys, make first API call | 2 | 01–02 |
| **2** | Explore standard SDK adapters — send prompts across OpenAI/Anthropic/Gemini, compare response formats | 3 | 03 |
| **3** | Build conversation memory using list/dict structures — multi-turn chatbot with history array | 3 | 04–05 |
| **4** | Tokenizer & token estimation; zero-shot vs few-shot prompting; force JSON-structured output | 3 | 06–07 |
| **5** | Mini-project: Personal AI Assistant supporting teacher/chef/recruiter personas | 3 | 08 |

---

## Unit 2: Advanced API Usage & Optimisation (16 hrs — 5 practicals)

| Practical # | Task | Hrs | Notebook Ref |
| :---: | :--- | :---: | :---: |
| **6** | Parameter tuning experiments — temperature & top-p variations on same prompt | 3 | 09 |
| **7** | Streaming responses — implement generator, measure time-to-first-token (TTFT) | 3 | 10–11 |
| **8** | Async programming with asyncio & `asyncio.gather()` — concurrent API calls | 3 | 12 |
| **9** | Rate-limit handling — exponential backoff retry decorator + batch processing (product reviews) | 4 | 13–14 |
| **10** | Mini-project: Smart Client — cost/token calculator + function-calling schema for invoice extraction | 3 | 15–16 |

---

## Unit 3: LLM Frameworks for Application Development (16 hrs — 5 practicals)

| Practical # | Task | Hrs | Notebook Ref |
| :---: | :--- | :---: | :---: |
| **11** | Install LangChain, build first pipeline using LCEL | 3 | 17–18 |
| **12** | Conversational chatbot with summary memory | 3 | 19 |
| **13** | Pydantic-based structured output — JSON schema validation & parsing | 3 | 20 |
| **14** | Vector embeddings — compute cosine similarity, build simple semantic search | 3 | 21–22 |
| **15** | Mini-project: RAG chatbot — SimpleDirectoryReader index + LlamaIndex/HuggingFace query engine | 4 | 23–24 |

---

## Unit 4: Local LLMs, Multimodal AI & Capstone (14 hrs — 5 practicals)

| Practical # | Task | Hrs | Notebook Ref |
| :---: | :--- | :---: | :---: |
| **16** | Set up Ollama, pull and run a local LLM, test via API/CLI | 3 | 25 |
| **17** | LM Studio — benchmark GGUF models on latency & RAM usage | 3 | 26 |
| **18** | Multimodal OCR — base64 image encoding, vision prompt + context string extraction | 3 | 27–28 |
| **19** | Hybrid routing algorithm — route simple queries to local model, complex ones to cloud API | 2 | 29 |
| **20** | Capstone: End-to-end mini project completion + demo presentation | 3 | 30 |

---

### **Total: 60 hrs / 20 practicals**

### Notes on Structure:
* Each unit ends with its "consolidation" practical using the standalone tool (`personal_assistant.py`, `smart_client.py`, `rag_chatbot.py`, `hybrid_router.py`) as the capstone for that unit.
* Units 2 and 3 get slightly more time (16 hrs each) since async/retry logic and RAG pipelines typically need more debugging time in a lab setting than Unit 1/4 topics.
* If your lab sessions are fixed-length (e.g., 3-hour blocks), you can merge #9 into two 2-hour sessions, or split #15 similarly (these can be rebalanced if the actual slot length is different).
