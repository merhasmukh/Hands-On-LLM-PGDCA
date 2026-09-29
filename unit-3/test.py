from dotenv import load_dotenv
import os

# Load environment variables from .env file in workspace root
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
# Part 4 Code: Modern LlamaIndex Setup with Settings & Persistence
try:
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
    from llama_index.llms.google_genai import GoogleGenAI
    from llama_index.embeddings.google_genai import GoogleGenAIEmbedding   
    print("✅ LlamaIndex Core packages detected!")
    
    # 1. Configure Global Settings

    if api_key:
        Settings.llm=llm = GoogleGenAI(model="gemini-3.5-flash-lite",api_key=api_key)
        Settings.embed_model = GoogleGenAIEmbedding(model_name="gemini-embedding-2", api_key=api_key)
    Settings.chunk_size = 512
    Settings.chunk_overlap = 50
    
    PERSIST_DIR = "./storage"
    
    # 2. Check if index already exists to avoid redundant embedding costs
    if not os.path.exists(PERSIST_DIR):
        print("📁 Creating new VectorStoreIndex from 'data/' directory...")
        documents = SimpleDirectoryReader("unit-3/data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print(f"💾 Index successfully persisted to '{PERSIST_DIR}'.")
    else:
        print(f"⚡ Loading existing index from '{PERSIST_DIR}' (Zero API cost!)...")
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        
    # 3. Create Query Engine and query
    query_engine = index.as_query_engine(similarity_top_k=2)
    response = query_engine.query("What is LlamaIndex and how does it work?")
    print("=" * 60)
    print("🤖 LLAMAININDEX QUERY ENGINE RESPONSE:")
    print("=" * 60)
    print(response)
    
    # 4. Display Citations & Sources
    print("\n📚 SOURCE CITATIONS:")
    for node in response.source_nodes:
        print(f"- Source File: {node.metadata.get('file_name', 'Unknown')}")
        print(f"  Relevance Score: {node.score}")
        print(f"  Excerpt: {node.text[:120]}...")
        
except ImportError as e:
    print("ℹ️ Note: 'llama-index' package is not installed in current environment.")
    print("   To install modern LlamaIndex with Gemini support, run:")
    print("   !pip install llama-index llama-index-llms-gemini llama-index-embeddings-gemini\n")
    print(f"   (Import message: {e})")
    print("\n👉 Proceed to Part 5 to run the complete, transparent First-Principles LlamaIndex Engine!")