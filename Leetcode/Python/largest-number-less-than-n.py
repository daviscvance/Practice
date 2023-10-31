# TikTok
# Medium / Hard
# Given a number n, such as 23121; given a set of numbers A such as {2,4,9}, find the largest
# number composed of elements in A that is less than n, such as the largest number less than
# 23121 is 22999.

def largest_number_less_than_n(n: int, A):
    n = list(str(n))
    A = sorted(A, reverse=True)

    def helper(i, flag):
        if i == len(n):
            return []
        for digit in (A if flag else [d for d in A if d <= int(n[i])]):
            res = helper(i + 1, flag or digit < int(n[i]))
            if res is not None:
                return [digit] + res
        return None

    return int(''.join(map(str, helper(0, False))))

# Test the function
ins = [23121, 24121, 29513]
outs = [22999, 22999, 39499]
A = {2, 4, 9}

for input, output in list(zip(ins, outs)):
    print(f'Testing: {input=}')
    assert(largest_number_less_than_n(n = input, A=A) == output)
    print(f'Passed: {input=} -> {output=}')
