def text_extractor(vtt_file):
    """
    Extract transcript text lines from a WebVTT file.

    Args: 
        vtt_file: Path to the WebVTT file.

    Returns: 
        A list of caption text lines.
    """
    with open(vtt_file, 'r') as file:
        lines = []
        for line in file:
            line = line.strip()

            if line == "WEBVTT":
                continue
            if line == '':
                continue
            if line.isdigit():
                continue
            if '-->' in line:
                continue

            lines.append(line)

    return lines

def paragraph_maker(vtt_file):
    """
    Concatenate caption lines from a WebVTT 
    file into a single paragraph.

    Args:
        vtt_file: Path to the WebVTT file.

    Returns:
        Concatenated string of all caption lines.
    """

    line_list = text_extractor(vtt_file)

    connect_string = ""

    for line in line_list:
        connect_string = connect_string + " " + line

    connect_string = connect_string.strip()

    return connect_string

paragraph = paragraph_maker('samples/sample.vtt')
print(paragraph)

sentences = []
current_sentence = ""

for char in paragraph:
    current_sentence += char

    if char == "." or char == "?" or char == "!":
        sentences.append(current_sentence.strip())
        current_sentence = ""
    
print(sentences)