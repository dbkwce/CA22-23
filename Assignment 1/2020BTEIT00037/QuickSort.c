#include <stdio.h>
void quicksort(int[],int,int);
void print(int arr[], int n);
//void swap1(int &n1, int &n2);

int main()
{
    int n;
    printf("Enter no of array elements:");
    scanf("%d",&n);
    int i,j,datalist[n];


    for(i=0;i<n;++i)
    {
        datalist[i]=n-i;
    }

    quicksort(datalist,0,n-1);
    printf("\nDatalist after quick sort:");

    print(datalist, n);

}

void print(int arr[], int n){
    for(int i=0;i<n;i++){
        printf("%d ", arr[i]);
    }
}

void swap1(int *n1, int *n2){
    int temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}

void quicksort(int datalist[],int low,int high)
{
    int pivot,i,j,temp;

    if(low<high)
    {
        pivot=low;
        i=low;
        j=high;

        while(i<j)
        {
            while((datalist[i]<=datalist[pivot])&&i<=high)
            {
                i++;
            }
            while((datalist[j]>datalist[pivot])&&j>=low)
            {
                j--;
            }
            if(i<j)
            {
                swap1(&datalist[i],&datalist[j]);
                /*temp=datalist[i];
                datalist[i]=datalist[j];
                datalist[j]=temp;*/
            }
        }

        swap1(&datalist[j],&datalist[pivot]);
        /*temp=datalist[j];
        datalist[j]=datalist[pivot];
        datalist[pivot]=temp;*/

        quicksort(datalist,low,j-1);
        quicksort(datalist,j+1,high);
    }
}
/*int break1(int datalist[], int start, int end){
    int pivot = datalist[start];
    int count = 0;
    for(int i=start+1;i<=end;i++)
    {
        if(datalist[i]<=pivot)
        {
            count++;
        }
    }
    int p = start+count;
    swap1(datalist[p],datalist[start]);
    int i = start;
    int j = end;

    while(i<p && j>p){
        while(datalist[i] <= pivot){
            i++;
        }
        while(datalist[j] > pivot){
            j--;
        }

        if(i<j){
            swap1(&datalist[i], &datalist[j]);
            i++;
            j--;
        }
    }

    return p;
}

void quicksort(int datalist[],int start,int end)
{
    int ind;
    if(start < end){
        ind = break1(datalist, start, end);
        quicksort(datalist, start, ind-1);
        quicksort(datalist, ind+1, end);
    }
}*/




