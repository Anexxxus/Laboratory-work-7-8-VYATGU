n = input()
if (n[0] == 'a' and n[1] == 'b' and n[2] == 'c'):
    print(n.replace('abc', 'www'))
else:
    n += "zzz"
    print(n)
