a="hello mmumbai hello bombay agra delhi jadoo"
counts={}
b=a.split()
for word in b:
    counts[word]=counts.get(word,0)+1

c=list(counts.items())
print(c)