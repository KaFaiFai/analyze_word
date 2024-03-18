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
        elif count < max_count * 0.01:
            outliers.append(alphabet)
        else:
            remainings.append(alphabet)

    print(f"all alphabets: {''.join(letters)}")
    print(f"non_alphas: {''.join(non_alphas)}")
    print(f"less_than_10: {''.join(less_than_10)}")
    print(f"outliers: {''.join(outliers)}")
    print(f"remainings: {''.join(remainings)}")
