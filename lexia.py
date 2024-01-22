input_path = "in.txt"
words_path = "words.txt"
output_path = "out.md"

def read(path):
    with open(path, 'r') as file:
        return file.read()

text = read(input_path)
frequent_words = read(words_path).split("\n")


def f1(word):
    if not word in frequent_words:
        word = f"**{word}**"
    return word

def f2(word: str):
    return f"**{word[0]}**" + word[1:]

def f3(word: str):
    return f"**{word[0:2]}**" + word[2:]

def bold(s):
    return f"**{s}**"

def f4(word: str):
    # out = bold(word[0]) + word[1] + bold(word[2]) + word[3:]
    n = len(word)
    w0 = bold(word[0])
    w1 = word[1] if n > 1 else None
    w2 = bold(word[2]) if n > 2 else None
    w3 = word[3:] if n > 3 else None
    
    if w1:
        w0 += w1
    if w2:
        w0 += w2
    if w3:
        w0 += w3
    return w0

def f5(word):
    n = len(word)
    w0 = bold(word[0])
    if n - 2 > 0:
        w1 = word[1:-1]
        w0 += w1

        w2 = bold(word[-1])
        w0 += w2
    else:
        return word
    return w0

output = []
for word in text.split():
    output.append(f5(word))

text = ' '.join(output)

with open(output_path, 'w') as file:
    file.write(text)