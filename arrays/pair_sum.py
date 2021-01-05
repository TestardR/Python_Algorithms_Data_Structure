
def pair_sum(arr, k):

    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for n in arr:
        target = k - n

        if target not in seen:
            seen.add(n)
        else:
            output.add((min(target, n), max(target, n)))

    print(output)


pair_sum([1, 3, 2, 2], 4)
