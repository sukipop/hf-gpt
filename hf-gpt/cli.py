#!/usr/bin/env python3
import click
import os
import requests

# Define the base API URL
BASE_API_URL = "https://api-inference.huggingface.co/models/"

# Ensure HF_TOKEN is set
if 'HF_TOKEN' not in os.environ:
    print("Error: $HF_TOKEN is not set. Please set the $HF_TOKEN environment variable before running hf-gpt.")
    exit(1)

# Function to query Hugging Face API
def query(api_url, payload):
    headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

# Define your command line interface using Click
@click.command()
@click.option('--model', default='openai-community/gpt2', help='Model ID to use for generation.')
@click.argument('text')
def generate(model, text):
    """Generate text using the specified model."""
    api_url = BASE_API_URL + model
    output = query(api_url, {"inputs": text})
    print(output)

if __name__ == '__main__':
    generate()