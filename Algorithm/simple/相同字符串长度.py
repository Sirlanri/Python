def one(strs):
    for i in range(1,len(strs)):
        same=strs[0][0:i]
        for item in strs:
            if item[0:i]!=same:
                return i-1
        count= i
    return count
print(one(["dog","dogecar","dog"]))
            