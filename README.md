
<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/numichat.appspot.com/o/Perf_Lola%2BH.way%20banner.png?alt=media&token=8a0dac42-1f76-4754-ac9c-40a93ba02125" alt="Logo">
</p>



# NLP Bots Tests End-to-End

This project arises from the need to stabilize a complete NLP chatbot stack. Those who have been working on such projects in the past year know that AIs like OpenAI and derivatives from Llama have undergone many changes, especially in the case of OpenAI. We have seen how GPT3, particularly the davinci-003 model, and GPT3.5 (the untamed one) have had their capabilities degraded.

That's why it's important to have a tool that allows not only stabilizing the prompts but the entire stack.

This library uses Telethon as a Telegram client to impersonate a user.

# Smart Assert

In the case of NLP bots, we won't always have a clear text to evaluate the response with just a string match. Sometimes a semantic assert is necessary.

This function allows evaluating the expected response using OpenAI.
```python
def nlp_assert(text_to_analyze, question, expected, treshold=90):
```

- **text_to_analyze**: response from the bot
- **question**: a direct question that GPT3.5/GTP4 can resolve to text that is easily evaluable by fuzzy match.
- **expected**: string expected as an answer to the question.
- **threshold**: how similar the expected value of the question response should be.

```python
eval, o, e = nlp_assert(resp.message, "Is the code valid? Answer only true or false", "false")
```

# Install

```bash
pip install -r requirements.txt
```


# Setup

create a .env file with the following variables:

```bash

# TELEGRAM 
# you can get this from https://my.telegram.org/apps
TELEGRAM_API_HASH=446db6985669********************
TELEGRAM_API_ID=2###########

# Whatever you want
TELETHON_SESSION_NAME=telethon

# OpenAI
OPENAI_API_KEY=sk-23t3qkfjwefhqlwkefjasdffsdf
OPENAI_MODEL=gpt-4
```

# Usage

If you are using Visual Code you can use the launch.json file to run the tests: Pytest: Current File



