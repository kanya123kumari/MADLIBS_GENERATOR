# Mad Libs Python Project
# A simple interactive program to generate a humorous story based on user input to learn Nouns, Verbs and Adjectives
# Introduction message
print("Welcome to the Mad Libs story generator, where your creativity meets comedy!!!!!!!!!!!!!")
print("----------------------------------------------------------------------------")

print("\nGet ready to unleash your imagination by providing different types of words, \nand watch which words are nouns, verbs and adjectives.")


print("-----------------------------------------------------------------------------------------")

# Two Cats and A Monkey
story = """\nSTORY: Two Cats and A Monkey:
Once upon a time, two cats used to live in a village. They were good friends and both used to live very lovingly with each other. 
One day both the cats became very hungry while playing. They saw a piece of bread at some distance. They started fighting over that bread. One cat said, "I found it first so it is mine."The other cat was saying the same thing.The first cat took two pieces of bread and extended one piece towards the second cat. Seeing this, the other cat said again, "What is this, you gave me a small piece. That is wrong. 
A clever monkey on the tree was seeing them fighting over the bread and wanted to eat that bread too.He said, \n"Why are you quarreling? I can help you because I have a scale which can divide the bread into equal amounts." 
Both cats liked the monkeys' advice. The monkey climbed the tree and brought the scale.He put both the pieces in a pan.He deliberately divided the bread into unequal amounts and said, "Hey, this piece is big, let's make both  equal and after saying this, he ate a little bit from the big piece and ate it.

Monkey Dividing Bread
In this way, every time the scale became heavy, he broke a little bread from that side and started putting it in his mouth. Both the cats were now terrified. She still quietly waited for the monkey's decision as they did not \nwant to give each other more amount of bread. 
At last small pieces of bread were in pans of the scale. The monkey said, "As you have seen that I have done the hard work of dividing bread with my scale so I must get the wages of my hard work”.He ate the rest of the pieces of bread. The poor cats went on empty stomachs from there.

Both the cats had realized their mistake and felt that others could take advantage of their weakness.
""" 



# Predefined words classified by part of speech
nouns = ["time", "cats", "village", "friends", "day", "piece", "bread", "distance", "thing", "pieces", "monkey", "tree", "scale", "amounts", "pan", "side", "mouth", "decision", "amount", "work", "wages", "stomachs", "mistake", "advantage", "weakness"]
verbs = ["used", "live", "were", "became", "playing", "saw", "started", "said", "found", "took", "extended", "gave", "seeing", "seeing", "was", "quarreling", "help", "have", "divide", "liked", "climbed", "brought", "put", "divided", "make", "ate", "became", "broke", "putting", "waited", "want", "give", "get", "went", "realized", "felt", "take"]
adverbs = ["very", "lovingly", "first", "again", "too", "equally", "deliberately", "quietly", "now"]
adjectives = ["two", "good", "hungry", "small", "clever", "equal", "big", "heavy", "terrified", "empty", "poor", "hard"]
articles = ["a","an","the"]

def main():
   
    # Print the story
    print(story)
    while True: 
        # Ask the user to input a word from the story
        user_word = input("\nEnter a word from the story: ").strip().lower()
        if user_word == 'exit':
                print("Exiting the program. Goodbye!")
                break
        # Check if the word exists in the story (case-insensitive)
        if user_word not in story.lower():
            print(f"Error: The word '{user_word}' does not exist in the story. Please enter a word from the story.")
            return
        
        # Check the part of speech for the word
        if user_word in nouns:
            print(f"The word '{user_word}' is classified as: Noun")
        elif user_word in verbs:
            print(f"The word '{user_word}' is classified as: Verb")
        elif user_word in adverbs:
            print(f"The word '{user_word}' is classified as: Adverb")
        elif user_word in adjectives:
            print(f"The word '{user_word}' is classified as: Adjective")
        elif user_word in articles:
            print(f"The word '{user_word}' is classified as: Articles")
        else:
            print(f"Error: The word '{user_word}' exists in the story but is not classified. Please check the word.")


# Run the program
main()