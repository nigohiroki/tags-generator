# Tags Generator

A Python library to generate a tags list from a text using OpenAI.

## Installation

Install the package using pip:


## Usage

```python
from tags_generator import TagsGenerator

# Set your OpenAI API key
openai_api_key = "your_openai_api_key"

# Initialize the TagsGenerator
tg = TagsGenerator(openai_api_key)

# Generate tags from a text
text = "Create a step-by-step guide on building a pip library to distribution the library."
tags = tg.generate_tags(text)

print(tags)

