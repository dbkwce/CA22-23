#include <bits/stdc++.h>
using namespace std;

int partition(int *a, int start, int end)
{
    int temp = a[end];

    int req = start;
    int i, t;
    for (i = start; i < end; i++)
    {
        if (a[i] <= temp)
        {
            t = a[i];
            a[i] = a[req];
            a[req] = t;
            req++;
        }
    }
    t = a[end];
    a[end] = a[req];
    a[req] = t;

    return req;
}

void Quicksort(int *a, int start, int end)
{
    if (start < end)
    {
        int req = partition(a, start, end);
        Quicksort(a, start, req - 1);
        Quicksort(a, req + 1, end);
    }
}

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int arr[n];

    cout << "Enter the array elements:\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    Quicksort(arr, 0, n - 1);
    cout << "Array after Quick Sort :\n";
    
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}