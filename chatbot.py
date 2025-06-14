# chatbot.py
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["hello", ["Hey!", "Hi, how can I help you?"]],
    ["how are you?", ["I'm doing great. What about you?"]],
    ["what is your name?", ["I am CodBot, your virtual assistant."]],
    ["who created you?", ["I was created by Potti during internship 😎."]],
    ["what can you do?", ["I can chat with you, answer questions, and make your day better."]],
    ["where are you from?", ["I'm from the cloud 🌩️."]],
    ["tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!"]],
    ["bye", ["Goodbye!", "See you later!"]],
]


chatbot = Chat(pairs, reflections)
chatbot.converse()
