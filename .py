import random

def add_typo(word):
    # Swap two adjacent characters
    if len(word) > 1:
        idx = random.randint(0, len(word) - 2)
        word = list(word)
        word[idx], word[idx + 1] = word[idx + 1], word[idx]
    return ''.join(word)

def add_noise_to_sentence(sentence, noise_level=0.1):
    words = sentence.split()
    noised_sentence = []
    for word in words:
        if random.random() < noise_level:
            word = add_typo(word)
        noised_sentence.append(word)
    return ' '.join(noised_sentence)

def add_noise_to_dataset(dataset, noise_level=0.1):
    noised_dataset = [add_noise_to_sentence(sentence, noise_level) for sentence in dataset]
    return noised_dataset

# Example usage
original_dataset = [
    "This is the first example sentence.",
    "Here is another one.",
    "Adding random noise to datasets can be fun!"
]

noised_dataset = add_noise_to_dataset(original_dataset, noise_level=0.2)

print("Original dataset:")
for sentence in original_dataset:
    print(sentence)

print("\nNoised dataset:")
for sentence in noised_dataset:
    print(sentence)
