import json
import pandas as pd
import matplotlib.pyplot as plt


def plot_count_graph(df: pd.DataFrame):
    alphabet_counts = {}
    for word in df["word"]:
        for alphabet in set(word):
            alphabet_counts[alphabet] = alphabet_counts.get(alphabet, 0) + 1

    sort_by_alphabet = sorted(alphabet_counts.items(), key=lambda x: x[0])
    letters = [item[0] for item in sort_by_alphabet]
    counts = [item[1] for item in sort_by_alphabet]

    plt.bar(letters, counts)

    plt.xlabel("Letters")
    plt.ylabel("Counts")
    plt.title("Letter Counts Histogram")

    plt.show()


def analyze_alphabets(df: pd.DataFrame):
    alphabet_counts: dict[str, int] = {}
    for word in df["word"]:
        for alphabet in set(word):
            alphabet_counts[alphabet] = alphabet_counts.get(alphabet, 0) + 1

    sort_by_alphabet = sorted(alphabet_counts.items(), key=lambda x: x[0])
    letters = [item[0] for item in sort_by_alphabet]

    max_count = max(sort_by_alphabet, key=lambda x: x[1])[1]
    non_alphas = []
    less_than_10 = []
    outliers = []
    remainings = []
    for alphabet, count in sort_by_alphabet:
        if not alphabet.isalpha():
            non_alphas.append(alphabet)
        elif count < 10:
            less_than_10.append(alphabet)
        elif count < max_count * 0.005:
            outliers.append(alphabet)
        else:
            remainings.append(alphabet)

    print(f"all alphabets: {''.join(letters)}")
    print(f"non_alphas: {''.join(non_alphas)}")
    print(f"less_than_10: {''.join(less_than_10)}")
    print(f"outliers: {''.join(outliers)}")
    print(f"remainings: {''.join(remainings)}")


def change_character(vocab: str, alphabets: list[str]) -> list[str]:
    new_vocabs = []
    for i, c in enumerate(vocab):
        for a in alphabets:
            if a != c:
                new_vocab = vocab[:i] + a + vocab[i + 1 :]
                new_vocabs.append(new_vocab)

    return new_vocabs


def character_difference(from_: str, to: str) -> int:
    count = 0
    for c1, c2 in zip(from_, to):
        if c1 != c2:
            count += 1
    return count


def distance(
    from_: str,
    to: str,
    vocabs_pool: set[str],
    alphabets: list[str],
    max_distance: int | None = None,
) -> tuple[int, list[str]]:
    if len(from_) != len(to):
        return (-1, [])

    vocab_path = {from_: ""}
    queue = [(from_, 0)]
    while queue:
        (cur_vocab, cur_distance) = queue.pop(0)
        if cur_vocab == to:
            path = [cur_vocab]
            while path[0] != from_:
                path.insert(0, vocab_path[path[0]])
            return (cur_distance, path)

        if cur_distance == max_distance:
            continue

        for new_vocab in change_character(cur_vocab, alphabets):
            if (new_vocab not in vocab_path) and (new_vocab in vocabs_pool):
                vocab_path[new_vocab] = cur_vocab
                queue.append((new_vocab, cur_distance + 1))

    return (-1, [])
