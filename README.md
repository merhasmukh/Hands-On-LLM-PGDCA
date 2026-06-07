# Hands-On LLM PGDCA

Welcome to the **Hands-On Large Language Models: Concepts, APIs & Application Development** course repository. This repository contains the complete curriculum, step-by-step practical Jupyter Notebooks, datasets, and standalone Python CLI applications designed to teach computer application students the foundational concepts and practical integrations of Large Language Models (LLMs).

---

## 📂 Repository Structure

The course is structured into four core units, mapping from basic Python setup to advanced frameworks, local execution, and multimodal pipelines:

### 📘 [Unit 1: LLM Foundations: Architecture & Evolution](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-1/)
Focuses on establishing virtual environments, Python programming basics, API calls, conversation history arrays, tokenizer systems, prompt engineering, and building personal assistants.
* **Topics**: `venv` / `pip` setups, list/dict mappings, standard SDK adapters (`openai`, `anthropic`, `google-generativeai`), conversation memory architectures, tokens estimations, zero/few-shot prompts, and JSON outputs.
* **Notebooks**: `01_python_environment_setup.ipynb` through `08_personal_ai_assistant_project.ipynb`
* **Standalone Tool**: [personal_assistant.py](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-1/personal_assistant.py) (Console-based interactive assistant supporting teacher/chef/recruiter personas).

### 📗 [Unit 2: LLM APIs: Advanced Usage & Performance Optimisation](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-2/)
Focuses on parameter adjustments, async programming concurrency, rate limits handling, and cost monitoring.
* **Topics**: Temperature & Top-p configs, streaming generators time-to-first-token (TTFT), Python `asyncio` & `asyncio.gather()`, batching product reviews, exponential retry decorators, and invoice extraction function schemas.
* **Notebooks**: `09_parameter_tuning_experiments.ipynb` through `16_unit_2_consolidation_smart_client.ipynb`
* **Standalone Tool**: [smart_client.py](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-2/smart_client.py) (Advanced client encapsulating retries, token pricing calculators, and structured formats).

### 📙 [Unit 3: LLM Frameworks for Application Development](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-3/)
Focuses on building retrieval pipelines and conversational bots using orchestration frameworks.
* **Topics**: LangChain Expression Language (LCEL), summary chatbot memory, Pydantic JSON validation parsing, vector math cosine similarity embeddings, SimpleDirectoryReader index builders, and Colab HuggingFace pipelines.
* **Notebooks**: `17_install_langchain_first_pipeline.ipynb` through `24_unit_3_project_rag_chatbot.ipynb`
* **Standalone Tool**: [rag_chatbot.py](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-3/rag_chatbot.py) (Interactive console application linking LlamaIndex query engines to local text files).

### 📕 [Unit 4: Local LLMs, Multimodal AI & End-to-End Project](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-4/)
Focuses on running open-source models offline, OCR vision prompt layouts, and system capstone planning.
* **Topics**: Ollama local servers config, LM Studio GGUF benchmark parameters (latency & RAM), base64 image OCR OCR models context strings, hybrid routing algorithms, and presentation guidelines.
* **Notebooks**: `25_setup_ollama_and_local_llm.ipynb` through `30_mini_project_completion_and_demo.ipynb`
* **Standalone Tool**: [hybrid_router.py](file:///Users/galaxyofai/Desktop/Github/Hands-On-LLM-PGDCA/unit-4/hybrid_router.py) (Saves cloud tokens by routing simple requests to local models).

---

## 🛠️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/merhasmukh/Hands-On-LLM-PGDCA.git
cd Hands-On-LLM-PGDCA
```

### 2. Set up a Virtual Environment
Create and activate an isolated environment:
```bash
# Mac/Linux
python3 -m venv llm_env
source llm_env/bin/activate

# Windows
python -m venv llm_env
llm_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install openai anthropic google-generativeai python-dotenv pandas pydantic tabulate tqdm
```

### 4. Configure Environment Variables
Create a `.env` file in the root folder and add your key details:
```env
OPENAI_API_KEY=your-api-key-here
```

### 5. Executing Scripts
To run the interactive console tools:
```bash
# Start Unit 1 Personal Assistant
python unit-1/personal_assistant.py

# Start Unit 3 RAG Doc Search
python unit-3/rag_chatbot.py
```