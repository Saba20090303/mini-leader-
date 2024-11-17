#codewars_1_8kyu_Reversed Words.
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

#codewars_2_8kyu_Total amount of points
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
#codewars_3_7kyu_Largest 5 digit number in a series.
def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)

#codewars_4_7kyu_Palindrome chain length.
def palindrome_chain_length(n):
    steps = 0
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        steps += 1
    return steps

#codewars_5_6kyu_Persistent Bugger.
def persistence(num):
    steps = 0
    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        
        steps += 1
    
    return steps

#codewars_6_5kyu_Beeramid.
def beeramid(bonus, price):
    total_cost = 0
    level = 0
    while True:
        level += 1
        total_cost += level * level * price
        if total_cost > bonus:
            return level - 1 
    
    return level