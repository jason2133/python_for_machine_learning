word_count = {}
text = """Jason Lee is the best ceo of the world. He has bachelor degree in statistics, korea university. I think korea is the best country in the world.""".lower().split()

for word in text:
    if word in word_count.keys():
        word_count[word] += 1

    else:
        word_count[word] = 1

print(word_count)



