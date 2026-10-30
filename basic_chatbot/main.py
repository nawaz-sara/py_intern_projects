#basic chatbot for conversation

question=["hello","how are you","bye","see you"]
replies=["hi","I'm fine ,thank you!","Goodbye","See you later!"]

q=input("Ask what you eant to ask\n").lower()

if q in question:
    index=question.index(q)
    print(replies[index])
else:
    print("I don't understand that question.")

#print("ChatBot: Hello! I am your chatbot.")
#print("ChatBot: You can talk to me. Type 'bye' to exit.")
#
#while True:
#    user = input("You: ").lower()
#
#    if user == "hello" or user == "hi":
#        print("ChatBot: Hello! How are you?")
#
#    elif user == "how are you":
#        print("ChatBot: I am fine! Thanks for asking.")
#
#    elif user == "what is your name":
#        print("ChatBot: My name is PyBot.")
#
#    elif user == "what can you do":
#        print("ChatBot: I can chat with you and answer basic questions.")
#
#    elif user == "bye":
#        print("ChatBot: Goodbye! Have a nice day.")
#        break
#
#    else:
#        print("ChatBot: Sorry, I don't understand that.")
#