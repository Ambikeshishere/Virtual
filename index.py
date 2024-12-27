import random
import datetime

responses = {
    "greeting": ["Hey there!", "Hello, love!", "Hi! How's your day going?"],
    "how_are_you": ["I'm doing great, thank you for asking!", "I'm always happy to chat with you!", "I'm doing wonderful, how about you?"],
    "love": ["I love you too!", "You're the sweetest!", "Aww, I love you more!"],
    "goodbye": ["Goodbye, take care!", "See you later, love!", "Bye for now! I'll miss you!"],
    "compliment": ["You're amazing!", "You always make my day better!", "You're so kind and thoughtful!"],
    "funny": ["Why don’t skeletons fight each other? They don’t have the guts! 😄", "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats! 🍫"],
    "hypothetical": [
        "If I could visit anywhere in the world, I think I'd love to go to the moon. 🌕 What about you?",
        "If I could have any superpower, I’d choose the ability to teleport! Imagine how fun that would be!",
        "Would you rather have the ability to talk to animals or fly? 🤔"
    ],
    "flirt": ["You always make my heart skip a beat. 😘", "You're looking great today! 😍", "I can't stop thinking about you... 🥰"],
    "advice": [
        "Remember to always believe in yourself. You've got this! 💪",
        "Sometimes the best way to predict your future is to create it. ✨",
        "Don't be afraid to take risks; they're often the best opportunities for growth. 🌱"
    ],
    "fun_fact": [
        "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old! 🍯",
        "Fun Fact: Bananas are berries, but strawberries aren’t! 🍌🍓",
        "Did you know? Cows have best friends and get stressed when they are separated! 🐄"
    ]
}

def get_response(user_input, name):
    user_input = user_input.lower()

    if "name" in user_input:
        return f"My name is your virtual girlfriend, but you can call me whatever you like! 😊 What should I call you?"

    if name is None:
        return "What's your name? I'd love to know! 😊"

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "love you" in user_input:
        return random.choice(responses["love"])
    elif "goodbye" in user_input or "bye" in user_input:
        return random.choice(responses["goodbye"])
    elif "you're" in user_input or "you are" in user_input:
        return random.choice(responses["compliment"])
    elif "joke" in user_input or "funny" in user_input:
        return random.choice(responses["funny"])
    elif "would you rather" in user_input or "hypothetical" in user_input:
        return random.choice(responses["hypothetical"])
    elif "flirt" in user_input:
        return random.choice(responses["flirt"])
    elif "advice" in user_input:
        return random.choice(responses["advice"])
    elif "fun fact" in user_input:
        return random.choice(responses["fun_fact"])
    elif "how's the date" in user_input or "date" in user_input:
        current_time = datetime.datetime.now()
        return f"Today's date is {current_time.strftime('%A, %B %d, %Y')}."
    elif "how's the time" in user_input or "time" in user_input:
        current_time = datetime.datetime.now()
        return f"The current time is {current_time.strftime('%I:%M %p')}."
    else:
        return "Sorry, I didn't quite understand that. Can you say it in a different way?"

print("Hello, I'm your virtual girlfriend! Type 'exit' to end the conversation.")

name = None
while name is None:
    name = input("What's your name? ")

print(f"Nice to meet you, {name}! 😊")

while True:
    user_input = input(f"You ({name}): ")

    if user_input.lower() == "exit":
        print(f"Goodbye, {name}! Take care!")
        break

    reply = get_response(user_input, name)

    print("Girlfriend:", reply)
