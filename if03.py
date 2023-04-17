def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b<c and c<b<a:
        l=b
    if a<c<b and b<c<a:
        l=c
    if b<a<c and c<a<b:
        l=a
    return l
a=int(input())
b=int(input())
c=int(input())
print(main(a,b,c))