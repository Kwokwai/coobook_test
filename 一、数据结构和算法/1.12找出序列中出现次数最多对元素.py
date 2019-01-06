words = [
    'look', 'into', 'my', 'eyes', 'look', 'my', 'eyes', 'the', 'eyes', 'the',
    'eyes', 'the', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around',
    'eyes', 'the', 'look', 'into', 'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)

a = Counter(words)
b = Counter(morewords)

print('*'*50)
c = a + b
print(c)

d = a - b
print(d)