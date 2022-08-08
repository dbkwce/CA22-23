#include<bits/stdc++.h>
using namespace std;

void PrintArray(int arr[], int n){

    for(int i=0; i<n; i++){

        cout<<arr[i]<<" ";
    }cout<<endl;
}

int Partition(int *arr, int low, int high){

    int pivot = arr[low];
    int i = low, j = high;
    do{

        do{i++;}while(arr[i] <= pivot);
        do{j--;}while(arr[j] > pivot);
        if(i < j) swap(arr[i], arr[j]);

    }while(i < j);

    swap(arr[low], arr[j]);
    return j;
}

void QuickSort(int arr[], int low, int high){

    int j;
    if(low < high){

        j = Partition(arr, low, high);
        QuickSort(arr, low, j);
        QuickSort(arr, j+1, high);
    }
}

int main()
{
    int n;
    cout<<"Enter the size of array\n";
    cin>>n;
    int v[n];
    int j=-1;
    for(int i=n; i>0; i--){
        v[j++] = i;
    }
    cout<<"Input array is: ";
    PrintArray(v, n);
    QuickSort(v, 0, n-1);
    cout<<"Sorted array is: ";
    PrintArray(v, n);
}
