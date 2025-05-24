from typing import Dict, List

from exer_1.search import search_faq
from exer_1.semantic_search_faiss import FAQ_SemanticSearch


def search_with_different_models(user_question: str, faq_data: List[Dict],
                                 models: List[str] = ['all-MiniLM-L6-v2', 'all-mpnet-base-v2']) -> Dict:
    """
    🌟 STRETCH: Compare different embedding models
    """
    results = {}

    # TODO: Implement comparison of different models
    # Try models like: 'all-MiniLM-L6-v2', 'all-mpnet-base-v2', 'paraphrase-multilingual-MiniLM-L12-v2'

    return results


def hyde_search(faq_search: FAQ_SemanticSearch, user_question: str, top_k: int = 3) -> List[Dict]:
    """
    🌟 STRETCH: Implement HyDE (Hypothetical Document Embeddings)

    HyDE technique:
    1. Generate a hypothetical answer to the user question
    2. Use this hypothetical answer for embedding/search instead of the question
    3. Often improves search quality
    """

    # TODO: Implement HyDE technique
    # You might need to use a language model to generate hypothetical answers
    # Or simulate it by rephrasing/expanding the question

    return search_faq(faq_search, user_question, top_k)


def evaluate_search_quality(faq_search: FAQ_SemanticSearch, test_cases: List[Dict]) -> Dict[str, float]:
    """
    🌟 STRETCH: Evaluate search quality

    test_cases format:
    [
        {
            "question": "How do I reset my password?",
            "expected_faq_indices": [5, 12]  # Indices of relevant FAQ entries
        }
    ]
    """

    # TODO: Implement evaluation metrics
    # Consider: Precision@K, Recall@K, MRR (Mean Reciprocal Rank)

    metrics = {
        "precision_at_1": 0.0,
        "precision_at_3": 0.0,
        "mean_reciprocal_rank": 0.0
    }

    return metrics
