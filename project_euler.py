## Project Euler problem 26
# by Egbuna Chinedu
def cycle(d):
    n = 1
    count = 0
    recur = []
    while True:
       
       if n in recur:
           return count
       else:
           recur.append(n)
           count += 1
           n *= 10
           remainder = n % d
       if remainder == 0:
           return count # not a recursive number
       else:
           n = remainder
           
max_cycle = 0
index = 0
for i in range(1,5000): 
    length = cycle(i)
    if length > max_cycle:
        max_cycle = length
        index = i
print(index, max_cycle)