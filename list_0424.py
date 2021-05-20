def is_sublist(l,s):
    sub_set = False
    if s== []:
        sub_set=True
    elif s==l:
        sub_set = true
    elif len(s)>len(l):
        sub_set = false
    else:
        for i in range(len(l)):
            if l[i]==s[0]:
                n=1
                print("value of n is: ", n," value of i is: ", i)
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                    print("value of n is: ", n," value of i is: ", i)
                
                if n == len(s):
                    sub_set = True
 
    return sub_set
 
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_sublist(a, b))
print(is_sublist(a, c))

