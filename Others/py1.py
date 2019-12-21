file1 = open('a.txt','r',encoding='utf8')  
file1_str = file1.readlines()  
file_list_new = []  
for stu in file1_str:  
    stu_grade = stu.split()  
    x = int(stu_grade[1])  

    if x > 90:
        stu_grade.append('优秀')
    elif x > 80:
        stu_grade.append('良好')
    elif x > 70:
        stu_grade.append('中等')
    elif x > 60:
        stu_grade.append('及格')
    else:
        stu_grade.append('不及格')
    stu_grade_str = '\t'.join(stu_grade)+'\n' 
    file_list_new.append(stu_grade_str) 
    file1.close() 
file2 = open('b.txt','rw+',encoding='utf8')  
file2.writelines(file_list_new)  
file2.close()
