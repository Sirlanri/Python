def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):    #以长的二进制字符串为遍历起点
            temp = a
            a = b
            b = temp
        a = a[::-1]           #倒序二进制字符串
        b = b[::-1]
        extra = 0             #进位
        new_binary = ""
        for index, num in enumerate(a):     #遍历
            if index > len(b) - 1:          #判断短的二进制字符串是否越界
                b_sum = 0
            else:
                b_sum = int(b[index])
            new_binary = new_binary + str((int(num) + b_sum + extra) % 2)     #二进制加法运算
            if int(num) + b_sum + extra > 1:     #是否进位
                extra = 1
            else:
                extra = 0
        if extra == 1:        #最高位是否进位
            new_binary = new_binary + "1"     
        return new_binary[::-1]    #倒序输出
print(addBinary('11110011101','1111101001'))