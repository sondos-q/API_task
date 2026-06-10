import requests

# HuggingFace secret key
HF_TOKEN = ""

# The address on HuggingFace's server that handels chats
URL = "https://router.huggingface.co/v1/chat/completions"

# prove the identity and tells the server that we are sending JSON
headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

# This prompt gives the AI its role which is weather assistant in this case 
SYSTEM_PROMPT = """You are a helpful weather assistant.
The user will ask you questions about weather in any city or country.
- Answer clearly and naturally in conversational English.
- If they ask about a city, mention temperature, humidity, wind, and general conditions.
- If you don't know real-time data, give general climate info for that location and season.
- Keep replies short and useful.
- Always end with a practical tip (e.g. 'bring an umbrella', 'wear sunscreen')."""

# start the conversation history with the system prompt already inside, So the AI knows its role from the first
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# Welcome message
print("🌤  Weather Info Bot")
print("Ask me about the weather anywhere in the world!")
print("Type 'exit' to quit.\n")

# Loop forever until the user exits
while True:
    question = input("You: ")
    if question.lower() in ("exit", "quit"):
        print("Stay safe out there! Goodbye!")
        break

    # Add the user message to the conversation history    
    messages.append({"role": "user", "content": question})

    # The data being sent to the srever. Includes the model we want to use and the conversation history 
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "messages": messages,
        "max_tokens": 300,
    }

    # Send the request to HuggingFace
    response = requests.post(URL, headers=headers, json=payload)
    # Converts the reply to a Python dictionary and extracts just the AI's text.
    data = response.json()
    answer = data["choices"][0]["message"]["content"]
    # save the AI reply to the conversation history
    messages.append({"role": "assistant", "content": answer})
    # print the AI answer 
    print(f"WeatherBot: {answer}\n")