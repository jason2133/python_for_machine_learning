from collections import Counter

text = """Jason Lee is the best ceo of the world. He has bachelor degree in statistics, korea university. I think korea is the best country in the world.""".lower().split()

print(Counter(text))
print(Counter(text)["the"])


