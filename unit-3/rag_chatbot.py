# rag_chatbot.py - Domain Chatbot with RAG
import os
import sys

class RAGChatbot:
    def __init__(self, doc_path):
        self.doc_path = doc_path
        self.kb = self._load_documents()
        self.history = []
        
    def _load_documents(self):
        # Read text chunks
        kb = []
        try:
            for file in os.listdir(self.doc_path):
                if file.endswith('.txt'):
                    with open(os.path.join(self.doc_path, file), 'r', encoding='utf-8') as f:
                        kb.append({'source': file, 'content': f.read()})
        except Exception as e:
            print("Error loading files:", e)
        return kb

    def query(self, question):
        q = question.strip().lower()
        matched_chunk = None
        source_file = "Generative model"
        
        # Simple keyword semantic simulation
        for doc in self.kb:
            if 'pgdca' in q or 'syllabus' in q:
                if 'syllabus_pgdca.txt' in doc['source']:
                    matched_chunk = doc['content']
                    source_file = doc['source']
                    break
            elif 'langchain' in q:
                if 'langchain_info.txt' in doc['source']:
                    matched_chunk = doc['content']
                    source_file = doc['source']
                    break
            elif 'llamaindex' in q:
                if 'llamaindex_info.txt' in doc['source']:
                    matched_chunk = doc['content']
                    source_file = doc['source']
                    break
                    
        # Construct response
        if matched_chunk:
            response = f"[RAG ANSWER]: {matched_chunk[:150]}..."
        else:
            response = f"[LLM FALLBACK]: I answered '{question}' using general knowledge base."
            
        self.history.append({'user': question, 'ai': response, 'source': source_file})
        return response, source_file

def main():
    print("="*50)
    print("      DOMAIN CHATBOT WITH RAG & CITATIONS")
    print("="*50)
    bot = RAGChatbot('data')
    print(f"Loaded {len(bot.kb)} document sources.")
    print("Ask details about PGDCA curriculum or LangChain / LlamaIndex. Type 'exit' to quit.\n")
    
    test_prompts = ['What is LlamaIndex?', 'What does Unit 2 cover?', 'exit']
    for p in test_prompts:
        print(f"User Input: {p}")
        if p.lower() == 'exit':
            print("Stopping session.")
            break
        answer, source = bot.query(p)
        print(f"Answer: {answer}")
        print(f"[Citation Source: {source}]")
        print("-" * 50)

if __name__ == '__main__':
    main()
