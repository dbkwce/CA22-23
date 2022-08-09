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
void swapp(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}


int part(int arr[], int low, int high,int &count)
{
	int pivot = arr[high]; 
	int i = (low - 1);
	for (int j = low; j <= high - 1; j++)
	{
		
		if (arr[j] < pivot)
		{   
		     count+=1;
			i++; 
			swapp(&arr[i], &arr[j]);
		}
	}
	swapp(&arr[i + 1], &arr[high]);
	return (i + 1);
}


void quickSort(int arr[], int low, int high, int &count)
{
	if (low < high)
	{
		
		int pi = part(arr, low, high,count);

		
		quickSort(arr, low, pi - 1, count);
		quickSort(arr, pi + 1, high,count);
	}
}

void printArr(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{       
       int lower = 1, upper = 100000, count;
        cout<<"Enter number: "<<endl;
        cin>>count;
        int comparison = 0 ;
	int arr[count] ; 
	
	 srand(time(0));
        
         printRandoms(lower, upper, count);
	
	
	
	for(int i = 0 ; i< count;i++){
	   arr[i] = printRandoms(lower, upper, count);
	   
	}
	printArr(arr,count);
	int n = sizeof(arr) / sizeof(arr[0]);
	quickSort(arr, 0, n - 1, comparison);
	cout <<endl<< "Sorted array: \n";
	printArr(arr, n);
	return 0;
}
