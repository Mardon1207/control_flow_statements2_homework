def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    b=n//1000%10
    c=n//100%10
    d=n//10%10
    f=n%10
    max=a
    ind=5
    if b>max:
        ind=4
    if c>max:
        ind=3
    if d>max:
        ind=2
    if f>max:
        ind=1
    return ind
n=int(input())
print(main(n))