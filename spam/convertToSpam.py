def split_text(text, line_length):
    lines = [text[i:i+line_length] for i in range(0, len(text), line_length)]
    return '\n'.join(lines)

def main():
    input_text = input("Enter the block of text: ")
    line_length = 200

    formatted_text = split_text(input_text, line_length)

    with open("spam.txt", 'w') as file:
        file.write(formatted_text)

    print("Text successfully written to spam.txt")

if __name__ == '__main__':
    main()
