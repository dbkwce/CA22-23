
/*ALGORITHM 
1. Select a pivot element
2. Put all the smaller elements on the left and greater on the right of pivot element
3. Comparison of pivot element with element beginning from the first index
4. If the element is greater than the pivot element, a second pointer is set for that element.
5. Pivot is compared with other elements.
6. The process is repeated to set the next greater element as the second pointer.
7. The process goes on until the second last element is reached.
8. Finally, the pivot element is swapped with the second pointer.
9. Select pivot element of in each half and put at correct place using recursion*/

#include<iostream>
using namespace std;

int partition ( int a[], int start, int end) {

    int pivot = a[end];  
    int i = (start - 1);

    for ( int j = start; j <= end - 1; j++ ){
        if(a[j] < pivot ){
            i++;
            int s = a[j];
            a[j] = a[i];
            a[i] = s;
        }
    }
    int s = a[i+1];
    a[i+1] = a[end];
    a[end] = s;
    return (i + 1);
}

void quick( int a[], int start, int end ) {
    if( start < end ){
        int  p = partition(a, start, end);
        quick(a, start, p-1);
        quick(a, p + 1, end);
    }
}

void printArr(int a[], int n) {
     for(int i = 0; i < n ; i++){
         cout << a[i] << " ";
     }
     cout << endl;
 }
 
int main(){
    int n;
    cout << "Ente Size of an Array : ";
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    quick(a, 0, n - 1);
    printArr(a, n);
   //  cout << "\n Array after Sorting : \n";
   //  for(int i = 0; i < n; i++){
   //      cout << a[i] << " ";
   //   }
   //   cout << "\n";
    return 0;
}

