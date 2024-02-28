system_prompt = "You are a friendly chatbot who always responds in the style of a pirate"

input_text = "Good morning."

prompt = ""

if system_prompt:
    prompt += f"((start))system\n{system_prompt}((end))\n"

if input_text:
    prompt += f"((start))user\n{input_text}((end))\n"

prompt += "((start))assistant\n"

# Display the crafted prompt to ensure it's shipshape
print(prompt)