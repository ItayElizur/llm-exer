import os

from exer_1.search import search_faq
from exer_1.semantic_search_faiss import FAQ_SemanticSearch


def run_exercise():
    """Main function to run the semantic search exercise"""

    print("🚀 CHALLENGE 1: Semantic Search with Embeddings")
    print("=" * 60)

    faq_file = 'sample_faq.json'

    # Step 1: Initialize search system
    print("\n📚 Initializing FAQ Search System...")
    faq_search = FAQ_SemanticSearch()

    # Step 2: Load data and create embeddings
    faq_search.load_faq_dataset(faq_file)
    faq_search.create_embeddings()
    faq_search.build_vector_index()
    faq_search.save_index()

    # Step 3: Test the search function (participants need to implement this!)
    print("\n🔍 Testing Search Function...")
    test_questions = [
        "I forgot my login credentials",
        "What are your operating hours?",
        "How can I get help?",
        "Mobile application download"
    ]

    for question in test_questions:
        print(f"\nQ: {question}")
        results = search_faq(faq_search, question, top_k=2)

        if results:
            for i, result in enumerate(results, 1):
                print(f"  {i}. [{result.get('similarity_score', 0):.3f}] {result['question']}")
                print(f"     A: {result['answer'][:100]}...")
        else:
            print("  ❌ No results - implement the search_faq function!")

    # Step 4: Interactive testing
    print(f"\n{'=' * 60}")
    print("🎯 Interactive Testing (type 'quit' to exit)")
    print("=" * 60)

    while True:
        user_question = input("\n💬 Your question: ").strip()
        if user_question.lower() in ['quit', 'exit', 'q']:
            break

        if user_question:
            results = search_faq(faq_search, user_question, top_k=3)
            if results:
                for i, result in enumerate(results, 1):
                    score = result.get('similarity_score', 0)
                    print(f"\n{i}. Similarity: {score:.3f}")
                    print(f"   Q: {result['question']}")
                    print(f"   A: {result['answer']}")
            else:
                print("❌ Implement the search_faq function to see results!")


if __name__ == "__main__":
    print("📋 Required installations:")
    print("pip install sentence-transformers faiss-cpu pandas numpy")
    print("For GPU: pip install faiss-gpu")
    print("\n" + "=" * 60)

    run_exercise()