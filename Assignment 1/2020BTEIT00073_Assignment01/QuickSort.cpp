#include <iostream>
using namespace std;

void swap(int* x, int* y) 
{ 
    int t = *x; 
    *x = *y; 
    *y = t; 
} 
   

int partition (int arr[], int l, int h) 
{ 
    int pivot = arr[h];    
    int i = (l - 1);   
   
    for (int j = l; j <= h- 1; j++) 
    { 
        
        if (arr[j] <= pivot) 
        { 
            i++;    
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[h]); 
    return (i + 1); 
} 
   

void quickSort(int arr[], int l, int h) 
{ 
    if (l < h) 
    { 
       
        int pivot = partition(arr, l, h); 
   
        
        quickSort(arr, l, pivot - 1); 
        quickSort(arr, pivot + 1, h); 
    } 
} 
   
void displayArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        cout<<arr[i]<<"\t"; 
      
} 
   
int main() 
{ 
    int arr[10],i;
    for(i=0;i<10;i++)
    {
     arr[i]=rand();
    }
    int n = sizeof(arr)/sizeof(arr[0]); 
    cout<<"Enter array"<<endl;
    displayArray(arr,n);
    cout<<endl;
    quickSort(arr, 0, n-1); 
    cout<<"Array sorted with quick sort"<<endl; 
    displayArray(arr,n); 
    return 0; 
}