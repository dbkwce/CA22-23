// Name: Pratham Yadav
// PRN: 2020BTEIT00006
// Sub: Computer Algorithm
// Assignment 1
// Date: 23/07/2022


// Following is the modular code of the Quicksort Sorting Algorithm in which sorting is done in ascending order.
// Quicksort follows the principle of divide and conquer.
// The code consist of four functions swap(), printArray(), partition(), quicSort().


// C++ code begins.
#include<iostream>
using namespace std;

// swap() which is used to swap the elements from any two indices of the array.
void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

// printArray() is used to print the array elements.
void printArray(int ar[],int n){
    for(int i=0;i<n;i++){
        cout<<ar[i]<<" ";
    }
    cout<<"\n";
}

// partition() one the major function of the alogrithm it returns an integer.
// The integer is the index of array, for which the partition/ division of the array should take place.
// partition() has three arguments 
// ar -> the array to be sorted
// l -> lowest index of the array passed in the function
// h -> highest index of the array passed in the function 
// pivot -> it's the element in the array from which the division of array will take place

// Basic objective of the partition function is that to divide the array,
// into two subarrays in which the first will contain the elements less than pivot, 
// the second will contain the elements greater than pivot.
// after each pass the pivot element is placed at it's correct place of the sorted array.

int partition(int ar[], int l, int h){
    
    int pivot = ar[h];
    int i = l - 1;

    for(int j = l; j<=h-1; j++){
        if(ar[j]<pivot){
            i++;
            swap(ar[i], ar[j]);
        }
    }
    swap(ar[i+1],ar[h]);
    return i+1;

}

// quickSort() it's the another important function of the alogrithm.


// quickSort() is the recursive function of the alogrithm, the arguments of functions are:
// ar -> the array to be sorted
// l -> lowest index of the array passed in the function
// h -> highest index of the array passed in the function 
// pi -> the index of pivot returned from the partition function
// This function is for sorting the first and second subarray formed on the either side of pivot.
void quickSort(int ar[], int l, int h){
    if(l<h){
        int pi = partition(ar, l, h);

        quickSort(ar, l, pi-1);
        quickSort(ar, pi+1, h);
    }
}

// Main 

int main(){

// The program will ask for the size of the array
    cout<<"Enter size of array: ";
    int n;cin>>n;

    int a[n];
// rand() function is used to create the array elements.
    for(int i=0;i<n;i++){
        a[i]=rand()%1000;
    }

// quickSort() is called for the sorting of array
    quickSort(a, 0, n-1);

// printArray() is used to print the array
    printArray(a,n);
    

}