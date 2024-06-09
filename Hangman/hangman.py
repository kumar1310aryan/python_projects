import random

def hangman():
    common_words = [
    "apple", "banana", "house", "car", "tree", "book", "chair", "table", "dog", "cat",
    "ball", "phone", "computer", "pencil", "paper", "window", "door", "bed", "lamp", "clock",
    "bread", "milk", "cheese", "coffee", "tea", "water", "juice", "egg", "rice", "pasta",
    "potato", "tomato", "cucumber", "onion", "garlic", "chicken", "fish", "beef", "pork",
    "salad", "pizza", "burger", "fries", "sandwich", "soup", "cake", "cookie", "candy",
    "chocolate", "ice cream", "spoon", "fork", "knife", "plate", "bowl", "cup", "glass",
    "shirt", "pants", "shoes", "socks", "jacket", "hat", "gloves", "scarf", "dress", "skirt",
    "tie", "belt", "watch", "ring", "earrings", "necklace", "bracelet", "bag", "wallet", "key",
    "phone", "umbrella", "backpack", "suitcase", "map", "passport", "ticket", "calendar",
    "notebook", "diary", "pen", "pencil", "marker", "eraser", "ruler", "scissors", "tape",
    "glue", "calculator", "computer", "keyboard", "mouse", "monitor", "printer", "scanner",
    "headphones", "microphone", "camera", "charger", "battery", "flashlight", "alarm",
    "remote", "speaker", "television", "radio", "fan", "microwave", "oven", "stove", "fridge",
    "freezer", "dishwasher", "washing machine", "dryer", "vacuum cleaner", "broom", "mop",
    "bucket", "sponge", "soap", "shampoo", "conditioner", "toothbrush", "toothpaste", "floss",
    "mouthwash", "towel", "washcloth", "tissue", "lotion", "perfume", "deodorant", "razor",
    "shaving cream", "sunscreen", "bug spray", "bandage", "ointment", "medication", "pill",
    "inhaler", "thermometer", "first aid kit", "fire extinguisher", "life jacket", "seatbelt",
    "helmet", "goggles", "gloves", "apron", "oven mitts", "pot holder", "spatula", "whisk",
    "ladle", "tongs", "can opener", "corkscrew", "cutting board", "mixing bowl", "measuring cup",
    "measuring spoon", "colander", "grater", "peeler", "rolling pin", "baking sheet", "saucepan",
    "skillet", "stockpot", "utensils", "dishes", "utensils", "tupperware", "foil", "saran wrap",
    "ziploc bags", "trash can", "recycling bin", "compost bin", "broom", "dustpan", "vacuum",
    "mop", "bucket", "bleach", "cleaner", "detergent", "fabric softener", "scrub brush", "sponge",
    "towel", "bucket", "squeegee", "dust rag", "disinfectant", "trash bags", "paper towels"
]

    word = random.choice(words)
    guessed = "_" * len(word)
    tries = 6
    guessed_letters = []

    print("Let's play Hangman!")
    print(guessed)

    while tries > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            guessed = "".join([char if char in guessed_letters else "_" for char in word])
            print(guessed)
        else:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")
    if "_" not in guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Out of tries! The word was {word}.")

if __name__ == "__main__":
    hangman()
