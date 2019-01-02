def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        print('uh oh')
        raise Exception(message % (first, second))
