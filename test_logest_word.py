txt = input()

#your code goes here
septxt = txt.split(" ")
lenseptxt = [len(i) for i in septxt]
maxxed = max(lenseptxt)
print(maxxed)
print(septxt[lenseptxt.index(maxxed)])
