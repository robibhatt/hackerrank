mod = Modulo(prime)
d = int(raw_input())
a = [int(x) for x in raw_input().split(' ')]
t = int(raw_input())
answers = []
for test in range(t):
    [n, m] = [int(x) for x in raw_input().split(' ')]
    entries = []
    for r in range(d+1):
        entry = (a[r] * total_count(m, n, r)) % prime
        entries.append(entry)
    answers.append(mod.sum(entries))
for answer in answers:
    print answer
