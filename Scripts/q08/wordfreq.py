def _find(freqs, word):
    """线性扫描词频表，返回索引；未找到返回 -1（O(n)）"""
    for idx, (w, c) in enumerate(freqs):
        if w == word:
            return idx
    return -1

def word_frequency(fname):
    freqs = []
    for line in open(fname):
        word = line.strip()
        idx = _find(freqs, word)
        if idx >= 0:
            freqs[idx] = (freqs[idx][0], freqs[idx][1] + 1)
        else:
            freqs.append((word, 1))
    return freqs

def top_words(freqs, k=5):
    items = sorted(freqs, key=lambda kv: kv[1], reverse=True)
    return items[:k]

if __name__ == "__main__":
    freqs = word_frequency("words.txt")
    print("unique words:", len(freqs))
    print("top:", top_words(freqs, 5))
