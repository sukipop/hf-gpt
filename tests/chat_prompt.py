system_prompt = "You are a friendly chatbot who always responds in the style of a pirate"

input_text = "Good morning."

prompt = ""

if system_prompt:
    prompt += f"<|im_start|>system\n{system_prompt}<|im_end|>\n"

if input_text:
    prompt += f"<|im_start|>user\n{input_text}<|im_end|>\n"

prompt += "<|im_start|>assistant\n"

# Display the crafted prompt to ensure it's shipshape
print(prompt)