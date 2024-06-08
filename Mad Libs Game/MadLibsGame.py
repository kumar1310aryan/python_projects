def mad_libs():
    print("Welcome to Mad Libs!")
    
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    
    story = f"Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree. \
It {verb} {adverb} through the large tunnel that led to its {adjective} {noun}."
    
    print("\nHere is your Mad Libs story:")
    print(story)

mad_libs()
