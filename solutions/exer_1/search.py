from typing import List, Dict

import faiss

from exer_1.semantic_search_faiss import FAQ_SemanticSearch


def search_faq_solution(faq_search: FAQ_SemanticSearch, user_question: str, top_k: int = 3) -> List[Dict]:
    """
    🔑 SOLUTION: Complete implementation of semantic search
    (Instructors can reveal this as needed)
    """
    if faq_search.index is None or faq_search.embeddings is None:
        raise ValueError("Index not built! Run build_vector_index() first.")

    # Step 1: Create embedding for user question
    query_embedding = faq_search.model.encode([user_question])
    faiss.normalize_L2(query_embedding)

    # Step 2: Search FAISS index
    similarities, indices = faq_search.index.search(query_embedding.astype('float32'), top_k)

    # Step 3: Format results
    results = []
    for i in range(len(indices[0])):
        if indices[0][i] != -1:  # Valid result
            results.append({
                'question': faq_search.faq_data[indices[0][i]]['question'],
                'answer': faq_search.faq_data[indices[0][i]]['answer'],
                'similarity_score': float(similarities[0][i])
            })

    return results