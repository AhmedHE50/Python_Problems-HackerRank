n = int(input())
l = []
cmd_s =[]
for i in range(n):
    cmd = input().split()
    cmd_s.append(cmd)

for i in range(len(cmd_s)):
    if "insert" in cmd_s[i]:
        l.insert(int(cmd_s[i][1]), int((cmd_s[i][2])))
    elif "print" in cmd_s[i]:
        print(l)
    elif "remove" in cmd_s[i]:
        l.remove(int(cmd_s[i][1]))
    elif "append" in cmd_s[i]:
        l.append(int(cmd_s[i][1]))
    elif "sort" in cmd_s[i]:
        l.sort()
    elif "pop" in cmd_s[i]:
        l.pop()
    else:
        l.reverse()