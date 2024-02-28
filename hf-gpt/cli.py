#!/usr/bin/env python3
import click
import os

# Check if the 'HF_TOKEN' environment variable is set
if 'HF_TOKEN' not in os.environ:
    print("Error: $HF_TOKEN is not set. Please set the $HF_TOKEN environment variable before running hf-gpt.")
    exit(1)
