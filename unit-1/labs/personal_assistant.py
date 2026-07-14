# personal_assistant.py - Console-based AI Assistant
import os
import sys
from dotenv import load_dotenv

class AIConsoleAssistant:
    def __init__(self, persona_instruction):
        self.history = [{'role': 'system', 'content': persona_instruction}]
        self.total_tokens = 0

    def get_token_count(self, text):
        return int(len(text.split()) * 1.3)

    def generate_response(self, prompt):
        self.history.append({'role': 'user', 'content': prompt})
        
        # Calculate tokens
        prompt_tokens = self.get_token_count(prompt)
        # Mock Completion output
        reply = f"[AI Persona Reply] Understood! Processing request: '{prompt}'"
        completion_tokens = self.get_token_count(reply)
        
        self.total_tokens += (prompt_tokens + completion_tokens)
        self.history.append({'role': 'assistant', 'content': reply})
        return reply

def main():
    load_dotenv()
    print("="*50)
    print("       PERSONAL AI ASSISTANT (CONSOLE)")
    print("="*50)
    print("Select a Persona:")
    print("1. Python Teacher")
    print("2. Chef Consultant")
    print("3. Technical Recruiter")
    
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        persona = "You are a friendly Python programming instructor."
    elif choice == '2':
        persona = "You are a Michelin-star culinary chef."
    else:
        persona = "You are an experienced technical developer recruiter."
        
    assistant = AIConsoleAssistant(persona)
    print(f"System Persona active: {persona}")
    print("Type 'exit' to quit the playground.\n")
    
    # Pre-loading commands for dry-run if run in background/non-interactive terminals
    mock_inputs = ['Explain variables', 'How do you cook pasta?', 'exit']
    for val in mock_inputs:
        print(f"User Input: {val}")
        if val.strip().lower() == 'exit':
            print("Terminating assistant session.")
            break
        res = assistant.generate_response(val)
        print(f"Assistant: {res}")
        print(f"[Metrics - Total Session Tokens: {assistant.total_tokens}]")
        print("-" * 50)

if __name__ == '__main__':
    main()
