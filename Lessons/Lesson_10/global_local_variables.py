def spam():
    global eggs
    eggs = 41
    print(eggs)


eggs = 42
print(eggs)
spam()
print(eggs)
