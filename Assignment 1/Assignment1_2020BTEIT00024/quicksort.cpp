
#include <cstdlib>
#include <time.h>
#include <iostream>
using namespace std;


int split(int arr[], int low, int high)
{

	int pivot = arr[high];
	
	int i = (low - 1);

	for (int j = low; j <= high - 1; j++)
	{
		
		if (arr[j] <= pivot) {

			
			i++;
			swap(arr[i], arr[j]);
		}
	}
	swap(arr[i + 1], arr[high]);
	return (i + 1);
}


int split_r(int arr[], int low, int high)
{
	
	srand(time(NULL));
	int random = low + rand() % (high - low);

	
	swap(arr[random], arr[high]);

	return split(arr, low, high);
}


void quickSort(int arr[], int low, int high)
{
	if (low < high) {

		
		int pi = split_r(arr, low, high);

		
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}


void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout<<arr[i]<<" ";
}

int main()
{
	int sz;
   cout<<"Enter the size of array::";
   cin>>sz;
   int randArray[sz];
   for(int i=0;i<sz;i++)
      randArray[i]=rand()%100;
	
	quickSort(randArray, 0, sz);
	printf("Sorted array: \n");
	printArray(randArray, sz);
	
	return 0;
}
