#include<iostream>
#include<stdio.h>
#include<stdlib.h>

#define LIST_INIT_SIZE 100 //���Ա�洢�ռ�ĳ�ʼ������
#define LISTINCREMENT 10   //���Ա�洢�ռ�ķ�������(���洢�ռ䲻��ʱҪ�õ�)

typedef int ElemType;      //����Ԫ�ص����ͣ�������int�͵�

typedef struct {
	ElemType *elem;       //�洢�ռ�Ļ���ַ
	int length;      //��ǰ���Ա�ĳ���
	int listsize;    //��ǰ����Ĵ洢����
}SqList;

//��ʼ��
int InitList(SqList &L)
{
	L.elem = (ElemType *)malloc(LIST_INIT_SIZE * sizeof(ElemType));//����һ���洢�ռ䣬�������洢�ռ�Ļ���ַ��ֵ��elem
	if (!L.elem)
	{
		return -1; //�ռ����ʧ��
	}

	L.length = 0; //��ǰ����
	L.listsize = LIST_INIT_SIZE; //��ǰ������
	return 0;
}

//����
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

//����
int ListInsert(SqList &L, int i, ElemType e)
{
	//�жϲ���λ�õĺϷ���
	if (i<1 || i>L.length + 1) return -1;
	//�жϴ洢�ռ��Ƿ���
	if (L.length >= L.listsize)
	{
		ElemType *newbase = (ElemType *)realloc(L.elem, (L.listsize + LISTINCREMENT) * sizeof(ElemType));
		if (!newbase) return -1;//�洢�ռ����ʧ��
		L.elem = newbase;//�»�ַ
		L.listsize += LISTINCREMENT;//���Ӵ洢����
	}
	//�������
	ElemType *q, *p; //����2��ָ�����
	q = &(L.elem[i - 1]); //qΪ����λ��(ע���β�i����ţ�����ǴӴ�1��ʼ�ģ����±��Ǵ�0��ʼ�ģ��������ת���±����i-1)
	for (p = &(L.elem[L.length - 1]); p >= q; --p) //��ai��an-1���κ��ƣ�ע����Ʋ���Ҫ�Ӻ���ǰ����
	{
		*(p + 1) = *p;
	}
	*q = e;
	++L.length;//����1
	return 0;
}

//ɾ��
int ListDelete(SqList &L, int i, ElemType &e)
{
	//�ж�ɾ��λ�õĺϷ���
	if (i<1 || i>L.length) return -1;
	//ɾ������
	ElemType *q, *p;//����2��ָ�����
	p = &(L.elem[i - 1]);//pΪ��ɾ��Ԫ�ص�λ��(ע���β�i����ţ�����ǴӴ�1��ʼ�ģ����±��Ǵ�0��ʼ�ģ��������ת���±����i-1)
	e = *p; //��ɾ����Ԫ�ظ�ֵ��e(�����ò�����Ҳ�����õ������Ա����e��)
	q = L.elem + L.length - 1;//qָ���β���һ��Ԫ��(q�����һ��Ԫ�صĵ�ַ)
	for (++p; p <= q; ++p) //��p����һ��Ԫ�ؿ�ʼ����ǰ��
	{
		*(p - 1) = *p;
	}

	--L.length;//����1
	return 0;
}


int main()
{
	SqList list;
	InitList(list);

	int n = 10;

	//���10�����ָ����Ա�list
	for (int i = 0; i < 10; i++)
	{
		ListInsert(list, i + 1, i + 1);
	}
	//ɾ����5��
	ElemType e;
	ListDelete(list, 5, e);
	printf("ɾ����Ԫ���ǣ�%d\n", e);

	//�ڵ�2��λ�ò���һ��Ԫ��-1
	ListInsert(list, 2, -1);

	//������Ա�
	for (int i = 0; i < 10; i++)
	{
		printf("%d ", list.elem[i]);
	}
	//�������ǣ�1 -1 2 3 4 6 7 8 9 10

	system("pause");
}