from sys import argv

if len(argv) < 2:
    print("Please provide file name.")
else:
    file = open(argv[1])
    lines = file.read()

    lines = lines.split("\n")  # a list of string
    print(lines)
    word_count = 0
    letter_count = 0

    for line in lines:
        words = line.split(" ")
        # print(words)
        word_count += len(words)
        # print(word_count)
        letter_count += len(line)

    line_count = len(lines)

    print(f"The line count is {line_count}")
    print(f"The word count is {word_count}")
    print(f"The letter count is {letter_count}")
