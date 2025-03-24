a = input("")
counta = a.index("@")
numa = a[0:counta]
alist = list(numa)
alist.sort()
ans = "".join(alist)
print(ans)