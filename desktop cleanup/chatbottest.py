from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

try: # Python 3.4+
    preferred_clock = time.perf_counter
except AttributeError: # Earlier than Python 3.
    preferred_clock = time.clock



chatbot = ChatBot("Ron Obvious")


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)
