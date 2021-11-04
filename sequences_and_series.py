# Have a look at the following numbers.
#
#  n | score
# ---+-------
#  1 |  50
#  2 |  150
#  3 |  300
#  4 |  500
#  5 |  750
# Can you find a pattern in it? If so, then write a function getScore(n)/get_score(n)/GetScore(n) which returns the score for any positive number n:
#
# int getScore(1) = return 50;
# int getScore(2) = return 150;
# int getScore(3) = return 300;
# int getScore(4) = return 500;
# int getScore(5) = return 750;


def get_score(n):
    result = 0
    for i in range(1, n+1):
        result += i * 50
    return result

print(get_score(5))



# test.describe("basic tests")
# test.expect(get_score(1) == 50, 'get_score(1) returns a wrong result')
# test.expect(get_score(2) == 150, 'get_score(2) returns a wrong result')
# test.expect(get_score(3) == 300, 'get_score(3) returns a wrong result')
# test.expect(get_score(4) == 500, 'get_score(4) returns a wrong result')
# test.expect(get_score(5) == 750, 'get_score(5) returns a wrong result')
