# task 1
def common_elements():
    list1 = [int(x) for x in input("Enter the first list (separate elements with space) ").split()]
    list2 = [int(x) for x in input("Enter the second list (separate elements with space): ").split()]
    return list(filter(lambda x: x in list2, list1))


result = common_elements()
print("New list with the elements that appear in both lists: ", result)


# task 2
def palindromes():
    strings = input("Enter a list of strings (separate with space): ").split()
    return list(filter(lambda x: x == x[::-1], strings))


result2 = palindromes()
print("New list with strings that are palindromes: ", result2)


# task 3
def prime_algorithm(lst):
    if not lst:
        return []

    n = max(lst)
    sieve = list(range(2, n + 1))

    primes = []
    while sieve:
        prime = sieve[0]
        primes.append(prime)

        sieve = [x for x in sieve if x % prime != 0]

    return [x for x in lst if x in primes]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
prime_numbers = prime_algorithm(numbers)
print(prime_numbers)


# task 4
def anagrams(word, word_list):
    word_chars = sorted(word.lower().replace(" ", ""))

    anagrams_list = []

    for w in word_list:

        w_chars = sorted(w.lower().replace(" ", ""))

        if w_chars == word_chars:
            anagrams_list.append(w)

    return anagrams_list

word = "tea"
word_list = ["eat", "ate", "art", "tea", "rat", "tar", "far"]
anagram_list = anagrams(word, word_list)
print(anagram_list)


