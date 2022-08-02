#include <iostream>
using namespace std;
  
void swap(int a, int b)      //function for swapping two elements.
{ 
    int t = a; 
    a = b; 
    b = t; 
} 
   
int partition (int arr[], int low, int high)     //function for partitioning the given array.
{ 
    int pivot = arr[high];   
    int i = (low - 1);   
   
    for (int j = low; j <= high- 1; j++) 
    { 
        if (arr[j] <= pivot) 
        { 
            i++;  
            swap(arr[i], arr[j]); 
        } 
    } 
    swap(arr[i + 1], arr[high]); 
    return (i + 1); 
} 
   
void quickSort(int arr[], int low, int high)      //driver function for quicksort.
{ 
    if (low < high) 
    { 
        int pivot = partition(arr, low, high); 
   
        quickSort(arr, low, pivot - 1); 
        quickSort(arr, pivot + 1, high); 
    } 
} 
   
void displayArray(int arr[], int size) 
{ 
     
    for (int i=0; i < size; i++) 
        cout<<arr[i]<<"\t"; 
      
} 
   
int main() 
{ 
    int arr[1000];
    for(int i=0;i<1000;i++){
        arr[i]=10000-i;
    }
    int n = sizeof(arr)/sizeof(arr[0]); 
    cout<<"Input array is :"<<endl;
    displayArray(arr,n);
    cout<<endl;
    quickSort(arr, 0, n-1); 
    cout<<"Array sorted with quick sort :"<<endl; 
    displayArray(arr,n); 
    return 0; 
}
