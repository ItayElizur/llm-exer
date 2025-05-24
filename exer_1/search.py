from typing import List, Dict

from exer_1.semantic_search_faiss import FAQ_SemanticSearch


def search_faq(faq_search: FAQ_SemanticSearch, user_question: str, top_k: int = 3) -> List[Dict]:
    """
    🎯 TASK: Implement semantic search function

    This function should:
    1. Create embedding for the user question
    2. Search the FAISS index for similar questions
    3. Return top 1-3 most relevant FAQ entries with similarity scores

    Args:
        faq_search: The FAQ_SemanticSearch instance
        user_question: User's input question
        top_k: Number of results to return (1-3)

    Returns:
        List of dictionaries with keys: 'question', 'answer', 'similarity_score'
    """

    # TODO: Implement this function!
    # Hints:
    # 1. Use faq_search.model.encode() to create question embedding
    # 2. Normalize the embedding with faiss.normalize_L2()
    # 3. Use faq_search.index.search() to find similar vectors
    # 4. Return the matching FAQ entries with scores

    # PLACEHOLDER - Replace with your implementation
    results = []

    # Your code here:
    # Step 1: Create embedding for user question
    # query_embedding = ...

    # Step 2: Search FAISS index
    # similarities, indices = ...

    # Step 3: Format and return results
    # for i in range(min(top_k, len(indices[0]))):
    #     if indices[0][i] != -1:  # Valid result
    #         results.append({
    #             'question': faq_search.faq_data[indices[0][i]]['question'],
    #             'answer': faq_search.faq_data[indices[0][i]]['answer'],
    #             'similarity_score': float(similarities[0][i])
    #         })

    return results
