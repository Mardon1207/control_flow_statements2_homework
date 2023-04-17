def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    return min
a=int(input())
b=int(input())
c=int(input())
print(main(a,b,c))