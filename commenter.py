import random
import pyperclip

# Expanded list of comments
comments = [
    "Amazing post! 👏",
    "Love the vibes here! 💖",
    "Keep up the great work! 🌟",
    "So inspiring, thank you! 🙌",
    "Fantastic content as always! 😍",
    "This made my day! 😊",
    "Such great insight, well done! 💡",
    "Wow, I love this! ✨",
    "You’re doing amazing, keep it up! 🔥",
    "So creative and inspiring! 🎨",
    "This is pure genius! 🧠",
    "Absolutely stunning! 😍",
    "Your content always brightens my day! 🌞",
    "This deserves all the applause! 👏👏",
    "I’m loving this so much! ❤️",
    "Beautifully done, as always! 💕",
    "Such a unique perspective! 🌈",
    "This is perfection! 😍",
    "Keep sharing amazing stuff like this! 💪",
    "Just wow! You’re so talented! ✨",
    "Love how you put this together! 🖤",
    "This speaks volumes, amazing work! 🎤",
    "I’m in awe of your creativity! 🌟",
    "This is so well thought out! 🧐",
    "Every time I see your posts, it’s a treat! 🍬",
    "This is so uplifting, thank you! 🙏",
    "You’ve got such an eye for detail! 👁️",
    "Such a cool idea, well executed! 🎯",
    "This is top-tier content! 🏆",
    "Absolutely love your style! 🌺",
    "You’re a source of endless inspiration! 💫"
]

# Loop for generating random comments
while True:
    # Generate a random comment
    random_comment = random.choice(comments)

    # Copy to clipboard
    pyperclip.copy(random_comment)
    print(f"Copied to clipboard: {random_comment}")

    # Wait for user input to continue or exit
    user_input = input("Press Enter for a new comment or type 'exit' to quit: ").strip().lower()
    if user_input == "exit":
        break
