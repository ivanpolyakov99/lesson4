import random

def ran(n):
    if n > 0:
        count = 0
        for i in range(n):
            if int(random.random() * 100) % 2 == 0:
                count += 1
        return str(count / n *100) + " % "
