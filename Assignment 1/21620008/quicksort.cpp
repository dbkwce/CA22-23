// QuickSort by Umesh Bagade,
// PRN:  21620008
// Time Complexity (average) O(nlog(n))


#include<iostream>
using namespace std;

void swap(int nums[], int lb, int hb)
{
    int temp = nums[lb];
    nums[lb] = nums[hb];
    nums[hb] = temp;
}

int myPartition(int arr[], int lb, int hb)
{

    int pvid = lb;
    int pivot = arr[lb++];
    
    while(lb<hb)
    {
        while(arr[lb] <= pivot)
            lb++;
        while(arr[hb] >pivot)
            hb--;
            
        if(lb<hb)
            swap(arr,hb,lb);
    }
    
    swap(arr, pvid, hb);
        
    return hb;    
}
  
void quicksort(int nums[], int lb, int hb)
{
    if(lb<hb)
    {
        int pi = myPartition(nums, lb, hb);
        
        quicksort(nums, lb, pi-1);
        quicksort(nums, pi+1, hb);
    }
}
int main()
{
/* for Custom Input
    int n;
    cout<<"How Many Numbers You wanted to Sort: ";
    cin>>n;
    int arr[n];
    cout<<"Enter the "<<n<<" Numbers:";
    for(int i=0;i<n;i++)
        cin>>arr[i];
*/
    int n=100;
    int arr[] = {13,25,30,45,72,71,57,5,12,58,20,72,73,14,89,85,65,1,60,91,17,78,21,52,25,29,65,25,70,91,64,47,28,16,33,25,11,75,21,36,96,50,7,95,70,6,81,4,26,77,99,37,93,59,33,6,39,39,53,3,38,61,30,67,13,50,92,61,66,1,88,63,69,23,95,30,51,99,22,79,88,47,67,4,90,94,32,57,14,84,4,90,5,47,99,43,78,91,39,18};


    quicksort(arr, 0, n-1);

    for(int i:arr)
        cout<<i<<" ";
    cout<<endl;

    return 0;
}
