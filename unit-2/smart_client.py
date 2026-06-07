# smart_client.py - Reusable Advanced LLM Client
import time
import random
import json

class SmartAIClient:
    def __init__(self, api_key, model='gpt-4o', cost_input=0.0015, cost_output=0.0020):
        self.api_key = api_key
        self.model = model
        self.cost_input_1k = cost_input
        self.cost_output_1k = cost_output
        self.total_cost = 0.0
        self.total_tokens = 0
        
    def _calculate_cost(self, prompt, reply):
        prompt_tokens = len(prompt.split()) * 2
        completion_tokens = len(reply.split()) * 2
        cost = (prompt_tokens / 1000.0) * self.cost_input_1k + (completion_tokens / 1000.0) * self.cost_output_1k
        self.total_cost += cost
        self.total_tokens += (prompt_tokens + completion_tokens)
        return cost, prompt_tokens + completion_tokens
        
    def call_with_retry(self, prompt, max_retries=3):
        wait = 1
        for attempt in range(max_retries):
            try:
                # Simulating request execution
                time.sleep(0.1)
                reply = f"[Resolved by SmartClient]: Output answering prompt '{prompt}'"
                cost, tokens = self._calculate_cost(prompt, reply)
                return {
                    'response': reply,
                    'metrics': {'cost_usd': cost, 'tokens': tokens}
                }
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(wait)
                wait *= 2
