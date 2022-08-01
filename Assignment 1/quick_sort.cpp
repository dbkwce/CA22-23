#include<iostream>
#include<vector>
using namespace std;

void swap(int arr[],int a,int b){
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
int partition(int arr[],int start,int end){
    int pivot = arr[end];
    int i =start-1;
    for(int j =start;j<end;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr,i,j);
        }
    }
    swap(arr,i+1,end);
    return i+1;
}

void quick_sort(int arr[],int start,int end){
    if(start<end){
        int pivot = partition(arr,start,end);
        quick_sort(arr,start,pivot-1);
        quick_sort(arr,pivot+1,end);
    }
    
}
int main(){
    int arr[] = {5,14,3,7,1,34,6};
    int n = sizeof(arr)/sizeof(int);
    for(int i = 0;i<n;i++) cout<<arr[i]<<" ";
    cout<<endl;
    quick_sort(arr,0,n-1);
    for(int i = 0;i<n;i++){
        cout<<arr[i]<<" ";
    }
return 0;
}