// Suyog Prashant Patil
// 2020BTEIT00043
// CA :- Assignment 1

#include <bits/stdc++.h>
using namespace std;

int cntSwaps = 0;
int cntPivot = 0;
int cntQuick = 0;

void mySwap(int &a, int &b)
{
    cntSwaps++;

    int temp = a;
    a = b;
    b = temp;
}

int getPivot(int low, int high, int v[])
{
    cntPivot++;
    int pivot = v[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        if (v[j] < pivot)
        {
            i++;
            mySwap(v[i], v[j]);
        }
    }
    i++;
    mySwap(v[high], v[i]);

    return i;
}

void quickSort(int low, int high, int v[])
{
    cntQuick++;
    if (low < high)
    {
        int pivot = getPivot(low, high, v);
        quickSort(low, pivot - 1, v);
        quickSort(pivot + 1, high, v);
    }
}

int main()
{
    int n;
    cout << "Enter the size of an array\n";
    cin >> n;

    int v[n];
    cout << "Enter " << n << " elements\n";
    for (int i = 0; i < n; i++)
    {
        int x = rand() % n + 1;
        v[i] = x;
    }

    for (int i = 0; i < n; i++)
        cout << v[i] << " ";
    cout << "\n";

    quickSort(0, n - 1, v);

    for (int i = 0; i < n; i++)
        cout << v[i] << " ";
    cout << "\n";

    cout << "Total comparisons for n = " << n << " are " << cntSwaps + cntPivot + cntQuick << "\n";

    return 0;
}
