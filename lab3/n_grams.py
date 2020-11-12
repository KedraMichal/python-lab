
def get_words(file_txt):
    with open(file_txt, "r", encoding="utf-8") as f:
        for word in f.read().replace(".", "").replace(",", "").replace("-", "").replace("!", "").replace("?", "").split():
            yield word


def count_n_grams(words_list, n):
    n_grams = {}
    saved = []
    i = 0
    for word in words_list:
        if i < n:
            saved.append(word)
            i += 1

        if i >= n:  # else
            if " ".join(saved) not in n_grams:
                n_grams[" ".join(saved)] = 1
            else:
                n_grams[" ".join(saved)] += 1

            saved.pop(0)
            saved.append(word)

    return n_grams


def count_words(words_list):
    return count_n_grams(words_list, 1)


def count_digrams(words_list):
    return count_n_grams(words_list, 2)


def count_trigrams(words_list):
    return count_n_grams(words_list, 3)


def find_top20_with_ties(counted_words):
    words = {k: v for k, v in sorted(counted_words.items(), key=lambda item: item[1], reverse=True)}
    i = 0
    top_20 = dict()
    for k, v in words.items():
        if i == 20: # ta 20 mogłaby być parametrem funkcji
            break
        else:
            top_20[k] = v
            i += 1
            value = v

    for k, v in words.items():  # jeśli słownik jest posortowany, to czy jest sens przeglądać cały?
        if v == value:
            if (k, v) not in top_20:
                top_20[k] = v

    return top_20


if __name__ == "__main__":
    words_top20 = find_top20_with_ties(count_words(get_words("potop.txt")))
    print("Top 20 words: {}".format(words_top20))
    digrams_top20 = find_top20_with_ties(count_digrams(get_words("potop.txt")))
    print("Top 20 digrams: {}" .format(digrams_top20))
    trigrams_top20 = find_top20_with_ties(count_trigrams(get_words("potop.txt")))
    print("Top 20 trigrams: {}".format(trigrams_top20))




