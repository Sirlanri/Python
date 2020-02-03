def one(strs):
    lenlist=[len(item) for item in strs]
    for i in range(1,min(lenlist)+1):
        same=strs[0][0:i]
        for item in strs:
            if item[0:i]!=same:
                return strs[0][0:i-1]
        count=i
    return strs[0][0:count]


def others(strs:list):
    front=min(strs)
    if len(front)==0:
        return ''
    least=max(strs)
    count=''
    for f,l in enumerate(front):
        if l!=least[f]:
            return front[0:f]
        count=front[0:f+1]
    return count

print(others(["aaa","aav"]))