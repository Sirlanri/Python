
def deal(words):
    """
    处理全部文字的循环
    """
    bigAfter=""
    index=0
    for word in words:
        if word.isdigit():
            bigAfter="".join([bigAfter,getWord(words[index-1],word)])
        else:
            bigAfter="".join([bigAfter,word])
        index+=1
    print(bigAfter)
        

def getWord(word,count):
    """
    输入重复的字母+数量
    """
    afterWord=""
    for _ in range(int(count)-1):
        afterWord="".join([afterWord,word])
    return afterWord

deal("d3hlo4e")