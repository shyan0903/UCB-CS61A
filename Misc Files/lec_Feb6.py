def happy_child(n):
    """Return the next number in the happy sequence, derived
    by summing the squares of digits of n
    >>> happy_child(13)
    10
    >>> happy_child(145)
    42
    """
    sum = 0
    while n > 0:
        sum += (n % 10) ** 2
        n //= 10
    return sum


def new_happy_child(n):
    """
    Has the same intent as happy_child but using process_digit func
    """
    def process_digit(n, digit_mapper, digit_check, digit_retval):
        mapped, place = 0, 0
        while n > 0:
            d = n % 10
            if digit_check(d):
                return digit_retval(mapped, place, d)
            mapped = digit_mapper(mapped, place, d)
            n //= n
            place += 1
        return mapped

    return process_digit(n, lambda mapped, place, d: mapped + d**2,
                         lambda d: False,
                         lambda mapped, place, d: None)

def happy_v1(n):
    """
    Return True if the number n is happy
    """
    step = 0
    while step < 25 and n != 1:
        n = happy_child(n)
        step += 1
    return n == 1

def happy_dot(n):
    """>>> happy_dot(4)
    digraph G {
    7->49
    49->97
    97->130
    130->10
    10->1
    }
    :param n:
    :return: a digraph of the happy sequence that starts with n
    """
    count = 0
    seen = set()
    print("digraph G {")
    while n != 1 and count < 25:
        if n not in seen:
            print(str(n) + "->" + str(happy_child(n)))
            seen.add(n)
        count, n = count + 1, happy_child(n)
    print("}")


happy_dot(93)
