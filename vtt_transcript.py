with open('samples/sample.vtt', 'r') as vtt_file:
    for line in vtt_file:
        line = line.strip()

        if line == "WEBVTT":
            continue
        
        if line == '':
            continue

        if line.isdigit():
            continue

        if '-->' in line:
            continue

        print(line)