
def generate_tokens(file):
    with open(file, "r", encoding="utf8") as f:
        for token in f.read().strip().replace(".", " .").replace(",", " ,").replace("\n", "").split(" "):
            yield token


def generate_sentences(file):
    with open(file, "r", encoding="utf8") as f:
        for token in f.read().strip().replace("\n", "").replace(".",". ").split("  "):
            yield token


def generate_tokens_conll(file):
    with open(file, "r", encoding="utf8") as f:
        for line in f:
            yield line.replace('"','').split(" ")[0]


def generate_sentences_conll(file):
    with open(file, "r", encoding="utf8") as f:
        sentence = ""
        for line in f:
            token = line.replace('"', '').split(" ")[0]
            sentence += token + " "
            if token == ".":
                yield sentence.replace(" .", ".")
                sentence = ""


##token-1kolum,kripka tez token

a = generate_tokens("nkjp.txt")
for i in generate_tokens("nkjp.txt"):
    print(i)
