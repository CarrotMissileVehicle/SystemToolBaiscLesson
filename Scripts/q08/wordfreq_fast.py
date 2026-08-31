def word_frequency_fast(fname):
    """优化版：用字典 O(1) 计数，替代 O(n) 线性扫描"""
    freqs = {}
    for line in open(fname):
        word = line.strip()
        freqs[word] = freqs.get(word, 0) + 1
    return freqs

def top_words(freqs, k=5):
    items = sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)
    return items[:k]

if __name__ == "__main__":
    import sys
    freqs = word_frequency_fast("words.txt")
    print("unique words:", len(freqs))
    print("top:", top_words(freqs, 5))
