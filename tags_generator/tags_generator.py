import openai
import ast

class TagsGenerator:
    def __init__(self, openai_api_key):
        self.api_key   = openai_api_key
        openai.api_key = self.api_key
    
    def generate_tags(self, text, max_tags=5, order="relevance"):
        # Prepare the prompt
        full_prompt = f"Generate a python list of tags for the following text: \"{text}\". Limit the number of tags to {max_tags} and order them by {order}. The output sample is [\"tag1\", \"tag2\", ...]"
        # Send the API request
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=50,
            top_p=1.0,
            temperature=0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        tags_str  = response.choices[0].text.strip()
        tags_list = ast.literal_eval(tags_str)
        return tags_list
