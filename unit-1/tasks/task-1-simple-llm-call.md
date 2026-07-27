# Task 1: Simple LLM API Call (Python)

**Objective:** Write a simple Python script to interact with a Large Language Model programmatically via an API.

**Instructions for Students:**
1. Choose an LLM provider that offers a free tier or trial API key (e.g., Google Gemini, Groq, or OpenAI if you have credits).
2. Install the necessary Python library (e.g., `pip install google-generativeai`, `pip install groq`, or `pip install openai`).
3. Write a short Python script that:
   - Sets up the API key securely (preferably using environment variables).
   - Sends a simple prompt to the model (e.g., "What are the three main types of Machine Learning?").
   - Prints the model's response to the console.

**Example structure (using the Google Gemini API):**
```python
import google.generativeai as genai
import os

# Set your API key in your environment variables first!
# In your terminal: export GEMINI_API_KEY="your_api_key_here"

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What are the three main types of Machine Learning?")
print(response.text)
```

4. **Deliverable:** Submit your `.py` script file and a screenshot of your terminal showing the successful output.
