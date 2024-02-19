def generator():
    for element in range(400):
        if (element % 2) == 0:
            yield element

a = generator()
