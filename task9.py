if __name__ == '__main__':

    # Since we need three numbers
    # that equal 1000, we iterate
    # up to 400 to save time.
    # This because we know that
    # a and b will be worth less than 400
    # because a < b < c
    for a in range(1, 400):
        for b in range(1, 400):
            c = (1000 - a) - b
            if a < b < c:
                if a ** 2 + b ** 2 == c ** 2:
                    print(a + b + c)