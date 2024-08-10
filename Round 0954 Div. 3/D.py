def finder(s, n):
    if n == 2:
        return int(s)
    
    l = list(s)
    if l[0] == '0' or l[-1] == '0':
        return 0
    
    if n >= 4 and '0' in l:
        return 0
    
    mini = l[0] + l[1]
    ind = 0
    for i in range(1, n-1):
        if (l[i] + l[i+1]) < mini:
            mini = l[i] + l[i+1]
            ind = i
    l[ind] = l[ind] + l[ind+1]
    del l[ind+1]
    