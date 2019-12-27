import random
from collections import Counter

a=[]
for i in range(50):
    a.append(random.randint(1,20))
result=dict(Counter(a))
print(result)