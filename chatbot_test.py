from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import collections.abc

collections.Hashable = collections.abc.Hashable

testbot = ChatBot(
    "Test Bot", 
    logic_adapters = [
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.TimeLogicAdapter"
])

trainer = ListTrainer(testbot)

corpus_trainer = ChatterBotCorpusTrainer(testbot)

trainer.train([
    "Yo!",
    "Hello",
    "All good?",
    "Yes, how about you?",
    "All good too. Thanks for asking. Bye",
    "Goodbye!",
    "How are you?",
    "I'm fine thanks for asking. How about you?",
    "I'm fine too!",
    "I'm happy to hear that",
    "Goodbye",
    "Goodbye!"
])

corpus_trainer.train("chatterbot.corpus.english")

while True:
    try:
        bot_input = testbot.get_response(input("You: "))
        print(f"Test Bot: {bot_input}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    except (AttributeError):
        print("Bot: Sorry, I don't understand your query.")