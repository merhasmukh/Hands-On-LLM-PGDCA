# Task 5: Capstone Mini-Project — Smart Client

**Objective:** Combine parameter usage, cost calculation, and structured outputs into a single, cohesive terminal application.

**The Scenario:**
You are building an automated invoice processing tool for a company. The tool needs to read raw, messy text from an email and extract the invoice details into a clean JSON structure, while strictly monitoring API costs.

**Requirements:**
1. **System Prompt & Roles:** Create a robust system prompt instructing the model to act as a data extraction assistant. It should ONLY output valid JSON.
2. **Cost Calculation:** Using the `tiktoken` library (or equivalent), calculate the number of input tokens *before* sending the request. When the response arrives, capture the output tokens from the API response object. Print the total estimated cost of the transaction (look up the current pricing per 1M tokens for the model you are using).
3. **Structured Output (JSON):** 
   - Write a raw string containing a mock invoice (e.g., "Hi, here is my bill for plumbing work on Oct 5. Labor was $200, parts were $50. Total $250. - John Doe").
   - Force the model to output a JSON object containing keys: `vendor_name`, `date`, `labor_cost`, `parts_cost`, `total_cost`. (You can use the API's `response_format={ "type": "json_object" }` if supported).

**Deliverable:**
Submit your complete `smart_client.py` script. The script should:
1. Print the raw input.
2. Print the parsed JSON output.
3. Print the token usage and calculated cost for the API call.
