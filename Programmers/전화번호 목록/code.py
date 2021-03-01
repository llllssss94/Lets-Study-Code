def solution(phone_book):
    answer = True

    # Hash method - Python Dictionary
    hmap = {}

    # init Dict using phone num as a key
    for num in phone_book:
        hmap[num] = 1

    for num in phone_book:
        temp = ""

        # for each character in single number string
        for c in num:
            # accumulate character in temp string
            temp += c

            # for every cycle, check if current temp is in hmap
            if temp in hmap and temp != num:
                return False

    """
    # Python String function
    phone_book.sort()

    # make every pair using zip function
    for n, m in zip(phone_book, phone_book[1:]):
        # using startswith function of python string module
        if m.startswith(n):
            answer = False
            break
    """

    """
    # Linear Search - Worst Method, cannot pass efficiency test
    phone_book = sorted(phone_book, key = lambda x: len(x))
    
    for i in range(len(phone_book)):
        shortest = phone_book[i]
        l = len(shortest)

        for num in phone_book[i+1:]:
            if shortest == num[:l]:
                answer = False
                break
    """
    
    return answer

if __name__ == "__main__":
    # case 1
    result = solution(["119", "97674223", "1195524421"])
    print(result)

    # case 2
    result = solution(["123","456","789"])
    print(result)

    # case 3
    result = solution(["12","123","1235","567","88"])
    print(result)
