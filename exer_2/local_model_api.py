import requests
import json


class LocalModelReviewer:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "codellama"):
        self.base_url = base_url
        self.model = model

    def review_code(self, code: str, prompt_template: str) -> str:
        """
        Use local model for code review.

        TODO: Implement this method
        - Format prompt with code
        - Make request to local model API
        - Return response
        """
        pass

    def stream_review(self, code: str, prompt: str):
        """
        Stream response from local model for long reviews.

        TODO: Implement streaming response
        """
        pass
