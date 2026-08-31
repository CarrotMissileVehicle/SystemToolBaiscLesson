import random

VOCAB = [f"w{i:04d}" for i in range(5000)]

def generate_words(n):
    return [random.choice(VOCAB) for _ in range(n)]

if __name__ == "__main__":
    random.seed(42)
    words = generate_words(200_000)
    with open("words.txt", "w") as f:
        f.write("\n".join(words))
    print("wrote", len(words), "words from vocab", len(VOCAB))
