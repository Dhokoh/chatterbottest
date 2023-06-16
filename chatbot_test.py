from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

testbot = ChatBot("Test Bot")

while True:
    try:
        bot_input = testbot.get_response(input())
        print(f"User: {bot_input}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    except (AttributeError):
        print("Bot: Sorry, I don't understand your query.")