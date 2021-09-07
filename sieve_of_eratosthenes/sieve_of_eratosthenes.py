def primes_less_then(n: int) -> list[int]:
    if n <= 2:
        return list()

    boolean_array: list[bool] = [True] * n
    boolean_array[0] = False
    boolean_array[1] = False  # 0 and 1 need to be marked as False.

    # go to each number that is marked True and mark out all of its multiples as False.
    for i in range(2, n):
        if boolean_array[i]:
            for j in range(i * i, n, i):  # start out with the multiples of i that are bigger then or equal to i*i.
                boolean_array[j] = False
            yield i  # return the base prime number.


if __name__ == '__main__':
    for x in primes_less_then(100):
        print(x)
