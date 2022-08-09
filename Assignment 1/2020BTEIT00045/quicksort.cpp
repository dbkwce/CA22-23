/*
PRN: 2020BTEIT00045
Subject: Computer Algorithm
Assignment 1 : QuickSort
*/


#include <bits/stdc++.h>
using namespace std;

void printArray(int num[], int n) {
  int i;
  for (i = 0; i < n; i++)
    cout << num[i] << " ";
  cout << endl;
}


void swap(int *x,int *y)
{
   int temp=*x;
   *x=*y;
   *y=temp;
}


int partition(int A[],int l,int h)
{
   int pivot=A[l];
   int i=l,j=h;
   do
   {
      do{i++;}
      while(A[i]<=pivot);

      do{j--;}
      while(A[j]>pivot);

      if(i<j)
      swap(&A[i],&A[j]);
   }
   while(i<j);

   swap(&A[l],&A[j]);
   return j;
}


void QuickSort(int A[],int l,int h)
{
    int j;
    if(l<h)
    {
       j=partition(A,l,h);
       QuickSort(A,l,j);
       QuickSort(A,j+1,h);
    }
}


int main(int argc, char const *argv[])
{
    int n;
    cout<<"Enter the value of N: ";
    cin>>n;
    int num[n];

    for(int i=0;i<n;i++)
    {
        num[i] = n-i;
    }
    QuickSort(num, 0, n);
    
    printArray(num,n);
    cout << endl;

    return 0;
}