/* 
   Quicksort Algorithm:
   
   1.QuickSort is a Divide and Conquer algorithm. 
     It picks an element as a pivot and partitions the given array around the picked pivot

   2.pick the last element as a pivot.

   3.The key process in quickSort is a partition(). The target of partitions is, 
     given an array and an element x of an array as the pivot, put x at its correct position in a sorted array 
	 and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.

   4.we start from the leftmost element and keep track of the index of smaller (or equal to) elements as i. 
     While traversing, if we find a smaller element, we swap the current element with arr[i].
	 Otherwise, we ignore the current element. 


*/




#include <bits/stdc++.h>
using namespace std;


int printRandoms(int lower, int upper,
                            int count)
{
    int i;
    for (i = 0; i < count; i++) {
        int num = (rand() %
        (upper - lower + 1)) + lower;
        return num ;
    }
    return 0;
}



// function to swap two elements
void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}


int partition (int arr[], int low, int high,int &count)
{
	int pivot = arr[high]; 
	int i = (low - 1);
	for (int j = low; j <= high - 1; j++)
	{
		
		if (arr[j] < pivot)
		{   
		     count+=1;
			i++; 
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}

/* main function that implements QuickSort */

void quickSort(int arr[], int low, int high, int &count)
{
	if (low < high)
	{
		
		int pi = partition(arr, low, high,count);

		
		quickSort(arr, low, pi - 1, count);
		quickSort(arr, pi + 1, high,count);
	}
}

/* Function to print an array */
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{       
       int lower = 0, upper = 100, nums;
        cout<<"Enter number of elements in array"<<endl;
        cin>>nums;
        int comparison = 0 ;
	int arr[nums] ; 
	
	 srand(time(0));
        
         printRandoms(lower, upper, nums);
	
	
	
	for(int i = 0 ; i< nums;i++){
	   arr[i] = printRandoms(lower, upper, nums);
	   
	}
	printArray(arr,nums);
	int n = sizeof(arr) / sizeof(arr[0]);
	quickSort(arr, 0, n - 1, comparison);
	cout <<endl<< "Sorted array: \n";
	printArray(arr, n);
	cout<<endl<<"Total number of comparison is "<< comparison <<endl;
	return 0;
}



