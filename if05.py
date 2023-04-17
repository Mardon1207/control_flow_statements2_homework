def main(n):
    """
    Find the largest digit of the five-digit number.
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
    if b>max:
        max=b
    if c>max:
        max=c
    if d>max:
        max=d
    if f>max:
        max=f
    return max
n=int(input())
print(main(n))