from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import collections.abc

collections.Hashable = collections.abc.Hashable

# Chatbot instance it loads the SQL table with the data over and over.

testbot = ChatBot(
    "Test Bot", 
    logic_adapters = [
        "chatterbot.logic.BestMatch"
    ],
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    database_uri = "sqlite:///chatbot_test_db.db"
)

clerk_convo = [
    "Hi",
    "Hi, how can I help you?",
    "I need to buy shoes",
    "Sure thing, what size would you be?",
    "Sure, I'm 10",
    "I'm sorry, unfortunately, we don't have that size at the moment",
    "Oh... okay then. Thank you.",
    "You're welcome, anything else I can do for you?",
    "Not right now, thanks.",
    "Alright, thank you. Goodbye.",
    "Goodbye."
]

small_talk = [
    "Hello",
    "Hi!",
    "How's the weather today?",
    "It's cool.",
    "Oh, by the way, what time is it?"
]

list_trainer = ListTrainer(testbot)

corpus_trainer = ChatterBotCorpusTrainer(testbot)

while True:
    bot_input = ""
    quit_words = ["q", "quit", "end"]
    try:
        bot_input = testbot.get_response(input("You: "))
        print(f"Test Bot: {bot_input}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    except (AttributeError):
        print("Bot: Sorry, I don't understand your query.")