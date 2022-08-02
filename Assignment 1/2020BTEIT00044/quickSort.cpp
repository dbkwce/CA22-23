#include<iostream>
using namespace std;

void printArray(int arr[],int n)
{
for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;	
}

void swap(int arr[],int i,int j)
{
	int temp=arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}
int partition(int arr[],int l, int r)
{
	int pivot=arr[r];
	int i=l-1;
	for(int j=l;j<r;j++)
	{
		if(arr[j]<pivot)
		{
			i++;
			swap(arr,i,j);
		}
	}
	swap(arr,i+1,r);
	return i+1;
}

void quickSort(int arr[],int l,int r)
{
	if(l<r)
	{
		int pi=partition(arr,l,r);
		quickSort(arr,l,pi-1);
		quickSort(arr,pi+1,r);

	}
}
int main()
{
	int n;
	cout<<"Enter the size of the array: ";
	cin>>n;
	int arr[n];
	cout<<"Enter the elements of the unsorted array:"<<endl;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	cout<<"The unsorted array is: "<<endl;
	printArray(arr,n);

	quickSort(arr,0,n-1);

	cout<<"The sorted array is: "<<endl;
	printArray(arr,n);

	return 0;
}