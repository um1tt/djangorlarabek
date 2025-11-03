# string_utils.py — строковые утилиты: частоты, токенизация, простая нормализация.
from __future__ import annotations
from typing import Dict, List, Tuple

_PUNCT = set(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")

def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

def word_count(text: str) -> int:
    return len(tokenize(text))

def char_frequency(text: str) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for char in text:
        if char.isalpha():
            key = char.lower()
            freq[key] = freq.get(key, 0) + 1
    return freq

def replace_vowels(text: str, symbol: str = '*') -> str:
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return ''.join(symbol if c in vowels else c for c in text)

def capitalize_words(text: str) -> str:
    return ' '.join(w.capitalize() for w in tokenize(text, keep_case=True))

def most_common_char(text: str) -> str:
    freq = char_frequency(text)
    return max(freq, key=freq.get) if freq else ''

def remove_punctuation(text):
    import string
    allowed = set(string.punctuation) - set(["-", "_"])
    return ''.join(c for c in text if c not in allowed)

def tokenize(text: str, keep_case: bool = False) -> List[str]:
    clean = remove_punctuation(text)
    return clean.split() if keep_case else clean.lower().split()

def ngrams(tokens: List[str], n: int) -> List[Tuple[str, ...]]:
    if n <= 0:
        raise ValueError("n must be > 0")
    return [tuple(tokens[i:i+n]) for i in range(0, len(tokens) - n + 1)]

def summary(text: str) -> dict:
    toks = tokenize(text)
    return {
        "chars": len(text),
        "words": len(toks),
        "unique_words": len(set(toks)),
        "is_palindrome": is_palindrome(text)
    }

def levenshtein(a: str, b: str) -> int:
    # классическая DP
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(
                dp[i-1][j] + 1,      # удаление
                dp[i][j-1] + 1,      # вставка
                dp[i-1][j-1] + cost  # замена
            )
    return dp[n][m]

def most_common_ngram(text: str, n: int = 2) -> Tuple[Tuple[str, ...], int]:
    toks = tokenize(text)
    grams = ngrams(toks, n) if len(toks) >= n else []
    freq: Dict[Tuple[str, ...], int] = {}
    for g in grams:
        freq[g] = freq.get(g, 0) + 1
    if not freq:
        return ((), 0)
    best = max(freq.items(), key=lambda kv: kv[1])
    return best[0], best[1]

def main() -> None:
    text = "Madam Arora teaches Malayalam. Level, kayak! Noon?"
    print("Original:", text)
    print("Summary:", summary(text))
    print("Reversed:", reverse_string(text))
    print("Common char:", most_common_char(text))
    print("levenshtein('kitten','sitting'):", levenshtein("kitten", "sitting"))
    grams, cnt = most_common_ngram(text, 2)
    print("Most common bigram:", grams, cnt)

if __name__ == "__main__":
    main()
