/*
    In this algorithm, we sort the array by divide and conquer method or partition method.
    1. We consider a pivot at low position in each recursive call and run a while loop atleast once until (i>j) (i=low+1, j=high, pivot = arr[low]).
    2. Find element greater than pivot with help of i and element less than pivot with help of j.
    3. And if i remains less than j, we swap arr[i] and arr[j].
    4. And finally we swap arr[j] and arr[low].
    5. Such that elements on left of arr[low] are less than arr[low], and that on right are higher than arr[low]. This operation is performed recursively until (low < high).
*/

#include<bits/stdc++.h>
using namespace std;

// Function to swap two numbers.
void swap1(int &n1, int &n2){
     int temp = n1;
     n1 = n2;
     n2 = temp;
}

// Function returns a position of pivot and arranges the array in such a way that all values to the left are smaller than pivot and to the right are greater than pivot.
int partition(int arr[], int low, int high){
    int pivot = arr[low];
    int i = low+1;
    int j = high;
    
    do{
    	// Finding the element greater than pivot with help of i.
       while(arr[i] <= pivot){
          i++;
       }
        // Finding the element less than pivot with help of j.
       while(arr[j] > pivot){
	  j--;
       }

       if(i<j){
  	  swap1(arr[i], arr[j]);
       }
    }while(i<j);

    swap1(arr[low], arr[j]);
    return j;
}

// Quick sort function executes recursively until the index (low < high) are in range.
void quicksort(int arr[], int low, int high){
    int partitionIndex;
    if(low < high){
        partitionIndex = partition(arr, low, high);
        quicksort(arr, low, partitionIndex-1);
	quicksort(arr, partitionIndex+1, high);
    }
}

int main(){
    // Size of the array.
    int n;
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        // Taking input for array elements.
        arr[i] = n-i;
    }
   
    quicksort(arr, 0, n-1);
    for(int i=0;i<n;i++){
       cout<<arr[i]<<" ";
    }
    return 0;
}
