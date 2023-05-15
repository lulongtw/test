x = input()
h = x.count(":-)")
s = x.count(":-(")
if h > s :
    print("happy")
elif h < s :
    print("sad")
elif h == 0 and s == 0 :
    print("none")
elif h == s :
    print("unsure")
