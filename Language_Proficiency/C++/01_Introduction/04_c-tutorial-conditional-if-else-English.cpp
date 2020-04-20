#include <bits/stdc++.h>
#include <climits>
#include <utility>
#include <map>
#include <string>

using namespace std;



void print_number(const int &n)
{
    std::map<int, std::string> mynumbers;
    mynumbers[1]= "one";
    mynumbers[2]= "two";
    mynumbers[3]= "three";
    mynumbers[4]= "four";
    mynumbers[5]= "five";
    mynumbers[6]= "six";
    mynumbers[7]= "seven";
    mynumbers[8]= "eight";
    mynumbers[9]= "nine";
    
    std::cout << mynumbers[n] << std::endl;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    if (n>9)
    {
        std::cout << "Greater than 9" << std::endl;
    }

    else
    {
        print_number(n);
    }
    

    return 0;
}


