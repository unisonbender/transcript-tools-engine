def text_extractor(vtt_file):

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
    line_list = text_extractor(vtt_file)

    connect_string = ""
    for line in line_list:
        connect_string = connect_string + " " + line

    connect_string.strip()

    return connect_string

paragraph = paragraph_maker('samples/sample.vtt')
print(paragraph)