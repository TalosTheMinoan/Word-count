def count_words_characters_lines(text):
    num_words = len(text.split())
    num_characters = len(text)
    num_lines = text.count('\n') + 1
    return num_words, num_characters, num_lines

def main():
    user_input = input("Enter text or specify a file path: ").strip()

    try:
        # Check if user input is a file path
        with open(user_input, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        text = user_input

    num_words, num_characters, num_lines = count_words_characters_lines(text)

    # Display the results
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_characters}")
    print(f"Number of lines: {num_lines}")

if __name__ == "__main__":
    main()
