def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    if temp<0:
        l=str("Freezing")
    if temp>=1 and temp<=10:
        l=str("Very Cold")
    if temp>=11 and temp<=20:
        l=str("Cold")
    if temp>=21 and temp<=30:
        l=str("Normal")
    if temp>=31 and temp<=40:
        l=str("Hot")
    if temp>40:
        l=str("Very Hot")
    return l
temp=int(input())
print(main(temp))