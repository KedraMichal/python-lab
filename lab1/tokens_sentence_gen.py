from nltk.tokenize import TweetTokenizer


def generate_tokens_txt(file):
    with open(file, "r", encoding="utf8") as f:
        tkn = TweetTokenizer()
        for token in tkn.tokenize(f.read().strip()):
            yield token


def generate_sentences_txt(file):
    with open(file, "r", encoding="utf8") as f:
        for token in f.read().strip().replace("\n", "").replace(".",". ").split("  "):  # hack, nie zawsze skuteczny
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


for i in generate_sentences_conll("nkjp.conll"):
    print(i)
