# Task 3: Asynchronous API Calls

**Objective:** Learn how to make concurrent API calls using Python's `asyncio` to drastically speed up processing times.

**Instructions:**
1. Create a list of 5 different prompts. For example, asking for the summaries of 5 different historical events or the capitals of 5 different countries.
2. **Synchronous approach:** Write a simple `for` loop that calls the API for each prompt one by one. Measure the total time taken.
3. **Asynchronous approach:** 
   - Use the `asyncio` library.
   - Use the async version of your chosen LLM client (e.g., `AsyncOpenAI`).
   - Define an `async def get_response(prompt):` function.
   - Use `asyncio.gather()` to run all 5 requests concurrently.
4. Measure the total time taken for the asynchronous approach.

**Deliverable:**
Submit your `.py` script showing both the synchronous and asynchronous approaches. The script should print the total time taken by each method.
