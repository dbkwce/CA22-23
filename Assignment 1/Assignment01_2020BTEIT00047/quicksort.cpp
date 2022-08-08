#include <bits/stdc++.h>
using namespace std;

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int partition(vector<int> &arr, int l, int h)
{
    int i = l, j = h, pivot = arr[l];

    do
    {

        do
        {
            i++;
        } while (arr[i] <= pivot);
        do
        {
            j--;
        } while (arr[j] > pivot);

        if (i < j)
            swap(arr[i], arr[j]);
    } while (i < j);

    swap(arr[l], arr[j]);

    return j;
}

void quick_sort(vector<int> &arr, int l, int h)
{
    int j;
    if (l < h)
    {
        j = partition(arr, l, h);
        quick_sort(arr, l, j);
        quick_sort(arr, j + 1, h);
    }
}

int main()
{

    int n;
    cout << "Enter the number of values" << endl;
    cin >> n;

    vector<int> arr(n);
    cout << "Enter the values " << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    quick_sort(arr, 0, n - 1);
    for (auto x : arr)
        cout << x << " ";

    cout << endl;

    return 0;
}