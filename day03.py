steps=[6200,7800,5100,9300,10400,4300,8800]

def average(steps):
    total = sum(steps)
    days = len(steps)
    return round(total / days , 1)
print(average(steps))



def max_steps(steps):
    big = max(steps)
    day = steps.index(big) + 1
    return big , day
print(max_steps(steps))