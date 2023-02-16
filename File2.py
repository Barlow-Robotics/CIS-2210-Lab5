time = 5

def countDown(n):
    if n == 1:
        print("Blast Off")
    else:
        print(n)
        countDown(n-1)

countDown(time)