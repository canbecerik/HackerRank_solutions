#include <bits/stdc++.h>

using namespace std;


void hourglass(vector<vector<int>> &array)
{
    int cur_sum = 0;
    int max_sum = -64;
    for (int i = 0; i < 4; i++)
    {
        for (int j =0; j < 4; j++)
        {
            cur_sum=array[i][j]+array[i][j+1]+array[i][j+2]+array[i+1][j+1]+array[i+2][j]+array[i+2][j+1]+array[i+2][j+2];
      
            if (cur_sum>max_sum)
            {
                max_sum=cur_sum;
            }
        }
    }
    cout << max_sum;
}

int main()
{
    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    hourglass(arr);
    return 0;
}
