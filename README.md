# Tags Generator

A Python library to generate a tags list from a text using OpenAI.

## Features

- Generate tags list from a text
- Limit the number of tags (max_tags)
- Order tags by relevance or randomly (order)

## Installation

Install the package using pip:

pip install tags-generator


## Usage

```python
from tags_generator import TagsGenerator

# Set your OpenAI API key
openai_api_key = "your_openai_api_key"

# Initialize the TagsGenerator with custom attributes
tg = TagsGenerator(openai_api_key, max_tags=5, order='relevance')

# Generate tags from a text
text = "Create a step-by-step guide on building a pip library to distribution the library."
tags = tg.generate_tags(text)

print(tags)
```


## Attributes
- max_tags (integer, default=5): Define the maximum number of tags in the output list.
- order (string, default='relevance'): Specify the order of tags based on their relevance. Options are 'relevance' or 'random'.

## License

This project is licensed under the MIT License.
