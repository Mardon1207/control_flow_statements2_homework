def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        l=0
    if a>b:
        l=a
    if b>a:
        l=b

    return l
a=int(input())
b=int(input())
print(main(a,b))