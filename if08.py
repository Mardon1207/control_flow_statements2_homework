def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    l=str()
    if number%7==1:
        l="Monday"
    if number%7==2:
        l="Tuesday"
    if number%7==3:
        l="Wednesday"
    if number%7==4:
        l="Thursday"
    if number%7==5:
        l="Friday"
    if number%7==6:
        l="Saturday"
    if number%7==0:
        l="Sunday"
    return l
number=int(input())
print(main(number))