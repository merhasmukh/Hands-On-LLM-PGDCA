# hybrid_router.py - Smart Query Router
class HybridAIRouter:
    def __init__(self, threshold_words=20):
        self.threshold = threshold_words
        self.local_count = 0
        self.cloud_count = 0
        
    def route_query(self, prompt):
        word_length = len(prompt.split())
        if word_length > self.threshold or 'summarize' in prompt.lower() or 'analyze' in prompt.lower():
            self.cloud_count += 1
            reply = f"[Resolved by Cloud Model (GPT-4o)]: Processed complex request '{prompt}'"
            route = 'CLOUD'
        else:
            self.local_count += 1
            reply = f"[Resolved by Local Model (Llama 3.2)]: Processed simple request '{prompt}'"
            route = 'LOCAL'
            
        return reply, route
