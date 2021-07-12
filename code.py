import collections
a=[1,2,2,5,5,5,5,5]
count = collections.Counter(a)
        
answer = 0
for key, value in count.items():
    if key == value:
        answer = max(answer, key)
print(answer)
