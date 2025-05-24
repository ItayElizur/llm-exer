import json
import numpy as np
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle
import os
from typing import List, Dict, Tuple

class FAQ_SemanticSearch:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initialize the semantic search engine
        
        Args:
            model_name: Name of the sentence transformer model to use
        """
        self.model = SentenceTransformer(model_name)
        self.faq_data = []
        self.embeddings = None
        self.index = None

    def load_faq_dataset(self, file_path: str) -> List[Dict]:
        """
        Load FAQ dataset from CSV or JSON file
        Expected format: columns/keys 'question' and 'answer'
        """
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            self.faq_data = df.to_dict('records')
        elif file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                self.faq_data = json.load(f)
        else:
            raise ValueError("File must be CSV or JSON format")

        print(f"✅ Loaded {len(self.faq_data)} FAQ entries")
        return self.faq_data

    def create_embeddings(self) -> np.ndarray:
        """Create embeddings for all FAQ questions"""
        if not self.faq_data:
            raise ValueError("Load FAQ data first!")

        questions = [item['question'] for item in self.faq_data]
        print("🔄 Creating embeddings...")
        self.embeddings = self.model.encode(questions, show_progress_bar=True)

        return self.embeddings

    def build_vector_index(self):
        """Build FAISS index for fast similarity search"""
        if self.embeddings is None:
            raise ValueError("Create or load embeddings first!")

        # Normalize for cosine similarity
        normalized_embeddings = self.embeddings.copy()
        faiss.normalize_L2(normalized_embeddings)

        # Create FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)  # Inner Product for cosine similarity
        self.index.add(normalized_embeddings.astype('float32'))

        print(f"✅ Built FAISS index with {self.index.ntotal} vectors")
    
    def save_index(self, index_path: str = 'faiss_index.bin', data_path: str = 'qa_data.pkl'):
        """
        Save FAISS index and Q&A data to disk
        """
        if self.index is None:
            raise ValueError("No index built. Call build_faiss_index() first.")
        
        # Save FAISS index
        faiss.write_index(self.index, index_path)
        
        # Save Q&A data and embeddings
        with open(data_path, 'wb') as f:
            pickle.dump({
                'faq_data': self.faq_data,
                'embeddings': self.embeddings
            }, f)
        
        print(f"Saved index to {index_path} and data to {data_path}")
    
    def load_index(self, index_path: str = 'faiss_index.bin', data_path: str = 'qa_data.pkl'):
        """
        Load FAISS index and Q&A data from disk
        """
        if not os.path.exists(index_path) or not os.path.exists(data_path):
            raise FileNotFoundError("Index or data files not found")
        
        # Load FAISS index
        self.index = faiss.read_index(index_path)
        
        # Load Q&A data and embeddings
        with open(data_path, 'rb') as f:
            data = pickle.load(f)
            self.faq_data = data['faq_data']
            self.embeddings = data['embeddings']
        
        print(f"Loaded index with {self.index.ntotal} vectors and {len(self.faq_data)} Q&A pairs")
