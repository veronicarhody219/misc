from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')


while True:
    # Prompt the user for input
    prompt = input("You: ")

    # Generate a response to the user input
    generated_text = generator(prompt, max_length=50, do_sample = True, temperature=0.9)

    # Extract the generated text from the response object
    response = generated_text[0]['generated_text'].strip()

    # Print the response and prompt the user again
    print("Chatbot:", response)