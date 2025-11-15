import re

import ollama

from ollama import Client

# LM | Must be available in Ollama library (https://ollama.com/library)
lm_name: str = 'qwen3:0.6b'

# Message | Example message to send to LM
message: str = 'Why is the sky blue?'

## Connect to the Ollama client
def _init_client(
    self
):
    # Create the client
    client = Client(host=self.url)            
    return client

## Check existing Ollama models
def _list_pulled_models(
    self
):
    # List all models available with Ollama
    ollama_models = ollama.list()
    # List all model names
    model_names = [
        model.model for model in ollama_models.models
    ]
    return model_names

## Pull LM
def _pull_lm(
    self,
    lm_name = lm_name
):
    response = ollama.pull(lm_name)
    return response

## Setup LM
def _init_lm(
    self, 
    lm_name = lm_name
):
    # Check existing models in Ollama
    model_names = self._list_pulled_models()

    # If `lm_name` not in model_names, pull it from Ollama
    if lm_name not in model_names:
        self._pull_lm(lm_name=lm_name)

## Clean LM response
def _remove_think_tags(
    self, 
    text
):
    # Find <think>...</think> within the text
    think_tag_pattern = re.compile(r'<think>.*?</think>\s*', re.DOTALL)
    # If the tag is not fully closed, we handle that separately
    if not think_tag_pattern:
        # Find any instances of <think> and </think> and 
        # substitute them with empty strings
        outside_tags = re.sub(r'</?think>', '', text).strip()

    # If matched and closed, clean up tags from outside
    else:
        # Change the <think>...</think> to an empty string
        cleaned_text = think_tag_pattern.sub('', text).strip()
        # Make sure no other tags remain
        outside_tags = re.sub(r'</?think>', '', cleaned_text).strip()

    return outside_tags

## Query the LM
def get_response(
    self, 
    lm_name = lm_name, 
    message = message
):
    ## Make sure LM is available
    self._init_lm(lm_name=lm_name)

    ## Get LM response
    # Format the message properly
    messages = {
        'role': 'user',
        'content': message,
    }
    # Send a message to the model
    response = self.client.chat(
        model=lm_name, 
        messages=[messages]
    )

    ## Return the response
    content = self._remove_think_tags(response.message.content)
    return content