special_numbers = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

ones = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

def read_number_in_english(n):
    if n < 0 or n > 99:
        return "Invalid input, please enter a number between 0 and 99."
    
    if n == 0:
        return "zero"
    
    if 10 <= n <= 19:
        return special_numbers[n]
    
    ten = n // 10
    one = n % 10
    
    if ten == 0:
        return ones[one]
    
    if one == 0:
        return tens[ten]
    
    return f"{tens[ten]}-{ones[one]}"

n = int(input("Enter a number (max 2 digits): "))
print(read_number_in_english(n))
