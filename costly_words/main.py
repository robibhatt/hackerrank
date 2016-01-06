prime = 1000000007
def power(base, exponent):
        a = base % prime
        b = exponent % (prime - 1)
        if b == 0:
            return 1
        if a == 0:
            return 0
        if a == 1:
            return 1
        if b == 1:
            return (a % prime)
        if b == 2:
            return ((a*a) % prime)
        if b % 2 == 0:
            temp = power(a, b/2)
            return ((temp * temp) % prime)
        else:
            temp = power(a, b/2)
            return ((temp * temp * a) % prime)

d = int(raw_input())
a = [int(x) for x in raw_input().split(' ')]
t = int(raw_input())
for test in range(t):
    [n, m] = [int(x) for x in raw_input().split(' ')]
    values = []
    for i in range(d+1):
        last_value = power(m-d+i, n)
        for j in range(i):
            next_value = ((m - d + i) * (last_value - values[j])) % prime
            values[j] = last_value
            last_value = next_value
        values.append(last_value)
    answer = 0
    for i in range(d+1):
        answer += (a[i] * values[i]) % prime
        answer = answer % prime
    print answer


    
