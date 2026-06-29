# 🌤 WeatherBot

A conversational weather assistant powered by Meta's **Llama 3.3 70B** model via the HuggingFace Inference API. Ask about the weather anywhere in the world and get natural, helpful replies with practical tips.

---

## Features

- Conversational interface — ask follow-up questions naturally
- Covers temperature, humidity, wind, and general conditions
- Falls back to seasonal climate info when real-time data isn't available
- Always ends with a practical tip (e.g. "bring an umbrella")
- Maintains full conversation history for context-aware responses

---

## Requirements

- Python 3.7+
- A [HuggingFace account](https://huggingface.co) with an API token

Install the dependency:

```bash
pip install requests
```

---

## Setup

1. **Get a HuggingFace API token**
   - Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Create a new token with **Inference** permissions

2. **Add your token to the script**

   Open `weatherbot.py` and set your token:

   ```python
   HF_TOKEN = "hf_your_token_here"
   ```

---

## Usage

```bash
python weatherbot.py
```

**Example session:**

```
🌤  Weather Info Bot
Ask me about the weather anywhere in the world!
Type 'exit' to quit.

You: What's the weather like in Tokyo right now?
WeatherBot: Tokyo in summer is hot and humid, typically around 30–35°C with high humidity...
            Tip: Stay hydrated and carry a small towel — the heat index can feel intense!

You: What about in winter?
WeatherBot: Tokyo winters are mild and dry, usually 5–10°C with clear sunny days...
```

Type `exit` or `quit` to end the session.

---

## How It Works

1. A **system prompt** sets the assistant's role as a weather expert before the first message.
2. Each user message is appended to a **conversation history** list.
3. The full history is sent to the HuggingFace API on every turn, so the model has full context.
4. The assistant's reply is extracted and appended to history for the next turn.

---

## Configuration

| Variable | Description |
|---|---|
| `HF_TOKEN` | Your HuggingFace API token |
| `URL` | HuggingFace chat completions endpoint |
| `model` | Model to use (default: `meta-llama/Llama-3.3-70B-Instruct`) |
| `max_tokens` | Max length of each reply (default: `300`) |
| `SYSTEM_PROMPT` | Instructions that define the assistant's behavior |

To swap in a different model, change the `"model"` field in the `payload` dictionary.

---

## Notes

- This bot does **not** have access to live weather data — it uses the model's training knowledge and general climate information.
- For real-time weather, consider integrating an API like [OpenWeatherMap](https://openweathermap.org/api) and passing the data into the prompt.
- Conversation history grows with each turn. For very long sessions, you may want to trim older messages to stay within token limits.
