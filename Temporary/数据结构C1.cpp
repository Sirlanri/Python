#include<iostream>
#include<stdio.h>
#include<stdlib.h>

#define LIST_INIT_SIZE 100 //线性表存储空间的初始分配量
#define LISTINCREMENT 10   //线性表存储空间的分配增量(当存储空间不够时要用到)

typedef int ElemType;      //数据元素的类型，假设是int型的

typedef struct {
	ElemType *elem;       //存储空间的基地址
	int length;      //当前线性表的长度
	int listsize;    //当前分配的存储容量
}SqList;

//初始化
int InitList(SqList &L)
{
	L.elem = (ElemType *)malloc(LIST_INIT_SIZE * sizeof(ElemType));//开辟一个存储空间，并把这块存储空间的基地址赋值给elem
	if (!L.elem)
	{
		return -1; //空间分配失败
	}

	L.length = 0; //当前长度
	L.listsize = LIST_INIT_SIZE; //当前分配量
	return 0;
}

//查找
int LocateElem(SqList L, ElemType x)
{
	int pos = -1;
	for (int i = 0; i < L.length; i++)
	{
		if (L.elem[i] == x)
		{
			pos = i;
		}
	}
	return pos;
}

//插入
int ListInsert(SqList &L, int i, ElemType e)
{
	//判断插入位置的合法性
	if (i<1 || i>L.length + 1) return -1;
	//判断存储空间是否够用
	if (L.length >= L.listsize)
	{
		ElemType *newbase = (ElemType *)realloc(L.elem, (L.listsize + LISTINCREMENT) * sizeof(ElemType));
		if (!newbase) return -1;//存储空间分配失败
		L.elem = newbase;//新基址
		L.listsize += LISTINCREMENT;//增加存储容量
	}
	//插入操作
	ElemType *q, *p; //定义2个指针变量
	q = &(L.elem[i - 1]); //q为插入位置(注意形参i是序号，序号是从从1开始的，而下标是从0开始的，因此这里转成下标后是i-1)
	for (p = &(L.elem[L.length - 1]); p >= q; --p) //从ai到an-1依次后移，注意后移操作要从后往前进行
	{
		*(p + 1) = *p;
	}
	*q = e;
	++L.length;//表长加1
	return 0;
}

//删除
int ListDelete(SqList &L, int i, ElemType &e)
{
	//判断删除位置的合法性
	if (i<1 || i>L.length) return -1;
	//删除操作
	ElemType *q, *p;//定义2个指针变量
	p = &(L.elem[i - 1]);//p为被删除元素的位置(注意形参i是序号，序号是从从1开始的，而下标是从0开始的，因此这里转成下标后是i-1)
	e = *p; //被删除的元素赋值给e(可能用不到，也可能用到，所以保存给e吧)
	q = L.elem + L.length - 1;//q指向表尾最后一个元素(q是最后一个元素的地址)
	for (++p; p <= q; ++p) //从p的下一个元素开始依次前移
	{
		*(p - 1) = *p;
	}

	--L.length;//表长减1
	return 0;
}


int main()
{
	SqList list;
	InitList(list);

	int n = 10;

	//添加10个数字给线性表list
	for (int i = 0; i < 10; i++)
	{
		ListInsert(list, i + 1, i + 1);
	}
	//删除第5个
	ElemType e;
	ListDelete(list, 5, e);
	printf("删除的元素是：%d\n", e);

	//在第2个位置插入一个元素-1
	ListInsert(list, 2, -1);

	//输出线性表
	for (int i = 0; i < 10; i++)
	{
		printf("%d ", list.elem[i]);
	}
	//输出结果是：1 -1 2 3 4 6 7 8 9 10

	system("pause");
}