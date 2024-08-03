import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. Bye :)"]
    ],
]

chatbot = Chat(pairs, reflections)

print("Hi, I'm the chatbot you created. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Bye! Have a nice day!")
        break
    else:
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")