def sanitize_string(data):
    """
    Removes special characters and trims the input.
    Handles None, empty strings, and non-string inputs safely.
    """
    if data is None:
        return ""
    if not isinstance(data, str):
        data = str(data)

    data = data.strip()
    for ch in ['!', '@', '#', '$', '%']:
        data = data.replace(ch, '')
    return data


def parse_int_list(csv_string):
    """
    Parses a CSV string of integers into a list of ints.
    Handles None, empty strings, and invalid values safely.
    """
    if csv_string is None:
        return []
    if not isinstance(csv_string, str):
        csv_string = str(csv_string)

    csv_string = csv_string.strip()
    if csv_string == "":
        return []

    parts = [p.strip() for p in csv_string.split(',') if p.strip() != ""]
    int_list = []

    for p in parts:
        try:
            int_list.append(int(p))
        except ValueError:
            # Instead of crashing, skip invalid entries
            continue

    return int_list


def reverse_words(sentence):
    """
    Reverses each word in a sentence.
    Handles None, non-string inputs, and punctuation gracefully.
    """
    if sentence is None:
        return ""
    if not isinstance(sentence, str):
        sentence = str(sentence)

    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    return " ".join(reversed_words)


def main():
    print("==== Running sanitize_string ====")
    raw_string = input("Enter a string with special characters (!,@,#,$,%): ")
    clean_string = sanitize_string(raw_string)
    print("Sanitized String:", clean_string)

    print("\n==== Running parse_int_list ====")
    csv_input = input("Enter a CSV of integers (e.g. 1,2,3,4): ")
    int_list = parse_int_list(csv_input)
    print("Parsed Integer List:", int_list)

    print("\n==== Running reverse_words ====")
    sentence_input = input("Enter a sentence without punctuation: ")
    reversed_sentence = reverse_words(sentence_input)
    print("Reversed Words Sentence:", reversed_sentence)


if __name__ == "__main__":
    main()
