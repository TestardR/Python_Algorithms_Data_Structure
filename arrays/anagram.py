# O(n) Linear Time Complexity
def anagram(s1, s2):
    return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())


# O(n) Linear Time Complexity
def anagram2(s1, s2):
    store = {}

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    for l in s1:
        if l in store:
            store[l] += 1 
        else: 
            store[l] = 1

    for l in s2:
        if l in store:
            store[l] -= 1 
        else: 
            store[l] = 1

    for l in store.values():
        if l != 0:
            return False
    
    return True




anagram('public relations', 'crap built on lies')