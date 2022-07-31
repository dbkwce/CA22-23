#include<iostream>
using namespace std;

void swap(int &i,int &j){
    int temp=i;
    i=j;
    j=temp;
}

int partition( int arr[], int l, int h) {
      int pivot =arr[l];
      int i=l,j=h;
      
      while(i<j){
      do{
        i++;
      }while(arr[i]<=pivot);
      do{
        j--;
      }while(arr[j]>pivot);
      if(i<j){
      swap(arr[i],arr[j]);
      }
      }
      swap(arr[l],arr[j]);
    return j;

}
void quickSort(int a[],int l, int h){
    if(l<h){
      int j=partition(a,l,h);
      quickSort(a,l,j);
      quickSort(a,j+1,h);
    }
}

int main()
{
    int n;
    cout<<"Enter how many number you want to enter : "<<endl;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
    a[i] = n-i;
    }
    quickSort(a,0,n);
    for(int i=0;i<n;i++){
    cout<<a[i]<<" ";
    }
    cout<<endl;
    return 0;   
}