/*
Name: Ankita Zade
PRN: 2020BTEIT00012
*/
#include<iostream>
using namespace std;

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}
int partition(int a[], int low, int high){
    int i = low-1;
    int pivot=a[high];
    int temp;
    for(int j=low; j<high; j++){
        if(a[j]<pivot){
            i++;
            swap(a[i], a[j]);
        }
    }
    i++;
    swap(a[i], a[high]);
    return i;
}

void quick_sort(int a[], int low, int high){
    if(low<high){
        int pivot_ind = partition(a, low, high);

        quick_sort(a, low, pivot_ind-1);
        quick_sort(a, pivot_ind+1, high);
    }
}

void print(int a[], int size){
    for(int i=0; i<size; i++){
        cout<<a[i]<<' ';
    }
    
}

int main(){
    int size;
    scanf("%d", &size);
    int a[size];
    for(int i=0; i<size; i++){
        a[i]=size-i;
    }

    quick_sort(a,0,size-1);
    print(a, size);
    
    return 0;
}