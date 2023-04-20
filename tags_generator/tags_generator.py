import openai

class TagsGenerator:
    def __init__(self, openai_api_key):
        self.api_key   = openai_api_key
        openai.api_key = self.api_key

    def generate_tags(self, text):
        # Prepare the prompt
        full_prompt = f"Generate tags as list for the following prompt: {text}"
        # Send the API request
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=full_prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.2,
        )
        tags_str = response.choices[0].text.strip()
        tags = [tag.strip() for tag in tags_str.split(',')]
        return tags
