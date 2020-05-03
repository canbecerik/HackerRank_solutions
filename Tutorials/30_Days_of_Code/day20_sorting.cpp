#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
    	cin >> a[a_i];
    }

    int totalSwapNo=0;
    
    for  (int i = 0; i < n; i++)
    {
        int currSwapNo = 0;
        for (int j = 0; j < n - 1; j++) 
        {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) 
            {
                swap(a[j], a[j + 1]);
                currSwapNo++;
            }
        }
        totalSwapNo+=currSwapNo;    
    // If no elements were swapped during a traversal, array is sorted
        if (currSwapNo == 0) 
        {
            break;
        }
    }
    
    std::cout << "Array is sorted in " << totalSwapNo << " swaps." << std::endl;
    std::cout << "First Element: " << a[0] << std::endl;
    std::cout << "Last Element: " << a[n-1] << std::endl;

    return 0;
}
