# A programs prints out the two largest and two smallest elements of a list
# called scores

from random import randint

scores = []
for i in range(10):
    scores.append(randint(0,10))
    scores.sort()
                  
print(scores)
print('Two lowest scores:',scores[0],scores[1])
print('Two highest scores:',scores[-1],scores[-2])   

print('Average:',sum(scores)/len(scores))
