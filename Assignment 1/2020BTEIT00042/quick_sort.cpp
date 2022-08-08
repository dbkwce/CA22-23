//Name: Shivaprasad Umshette
//PRN: 2020BTEIT00042

#include <bits/stdc++.h>
using namespace std;

// function to swap
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int *a, int l, int r)
{
    int i = l, j = r, k = a[l];
    do
    {
        do
            ++i;
        while (a[i] < k);
        do
            --j;
        while (a[j] > k);
        if (i < j)
            swap(a + i, a + j);

    } while (i < j);
    swap(a + j, a + l);
    return j;
}

void pivot(int *a, int l, int r)
{
    if (a[l] > a[r])
        swap(a + l, a + r);
}
void quick(int *a, int l, int r)
{
    int pos;
    if (l < r)
    {
        pivot(a, l, r);
        pos = partition(a, l, r);
        quick(a, l, pos - 1);
        quick(a, pos + 1, r);
    }
}
int main()
{

    // Inut the array
    int M;
    cin >> M;
    int x[M];
    cout << "Enter the data:";
    for (int i = 0; i < M; i++)
    {
        cin >> x[i];
    }
    // Array before sorting
    for (int i = 0; i < M; i++)
    {
        cout << x[i] << " ";
    }
    cout << "\n";
    quick(x, 0, M - 1);
    // array After Sorting
    for (int i = 0; i < M; i++)
    {
        cout << x[i] << " ";
    }
    return 0;
}
