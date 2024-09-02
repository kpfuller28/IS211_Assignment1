
def listDivide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1

    return count

class ListDivideException(Exception):
    pass

def test_list_divide():
    """
    Test listDivide
    """
    try:
        assert listDivide([1,2,3,4,5]) == 2, "Test 1 failed! Check your code"
        assert listDivide([2,4,6,8,10]) == 5, "Test 2 failed! Check your code"
        assert listDivide([30, 54, 63, 98, 100], divide=10) == 2, "Test 3 failed! Check your code"
        assert listDivide([]) == 0, "Test 4 failed! Check your code"
        assert listDivide([1,2,3,4,5], 1) == 5, "Test 5 failed! Check your code"
    except AssertionError as e:
        raise ListDivideException(f"A test case failed: {e}") from None
if __name__ == "__main__":
    test_list_divide()
