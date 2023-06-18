Just a chatterbot test and sandbox. 
Any discoveries are to be noted here. 

This software, requires a library called Chatterbot, which is basically going to provide me with the tools I need to build the bot. 

So far, I have discovered that I can modify the chatbot's base knowledge to a degree that is quite fundamental, which I found fascinating, tho I mustn't dwelve. 

This was learned while using the corpus_trainer and the list_trainer methods simultaneously.

Now, the following will narrate the story of how trying with only one of the lists at a time goes as per the chatbot's behaviour. This will require a full on deletion of the database as it is created automatically by the bot instance.

**Attempt with only one list**

I came to realize that, obviously, the data was being input into the robot. Now, I know how to create the simple robot with a few commands, I need to implement my own corpus in order to train this chatbot correctly. 

I found that the database doesn't even bother on checking for duplicate words, it just hashes them, which causes bugs and unwanted behaviour. Hence, ** I'll have to create my own database to train the chatbot. **

I will use CS50's library, and sqlite3 as well as the codespace to make the robot. (Thank you, Professor David, before this, I'd never thought I'd end up saying "I'll code myself a chatbot").

But meanwhile, I will try to use the English corpus trainer, to see how the bot interacts. 

** Attempt with only the English corpus trainer **

Disastrous. It doesn't respond as well as it should with a corpus that, supposedly includes a lot of context like jokes and stuff... anyways. Trying to set up my own SQL database this time. See how it goes. 

Reading about training the chatbot has been by far the most complex part, but also the most exciting. 






