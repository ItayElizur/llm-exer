import openai
from typing import Dict, Any


class OpenAICodeReviewer:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def review_code(self, code: str, prompt_template: str) -> str:
        """
        Send code to OpenAI for review using the specified prompt template.

        TODO: Implement this method
        - Format the prompt with the code snippet
        - Make API call to OpenAI
        - Return the response
        - Handle errors appropriately
        """
        pass

    def compare_prompts(self, code: str, prompts: list) -> Dict[str, str]:
        """
        Compare multiple prompt strategies on the same code.

        TODO: Implement this method
        - Test each prompt in the list
        - Return dictionary mapping prompt name to response
        """
        pass


# Example usage template
if __name__ == "__main__":
    # TODO: Set your API key
    API_KEY = "your-openai-api-key-here"
    reviewer = OpenAICodeReviewer(API_KEY)

    # TODO: Test with code samples
    code_to_review = """
    # Paste code sample here
    """

    # TODO: Use your designed prompts
    response = reviewer.review_code(code_to_review, "your_prompt_here")
    print(response)
