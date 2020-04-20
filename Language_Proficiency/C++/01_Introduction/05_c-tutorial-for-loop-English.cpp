#include <iostream>
#include <cstdio>
#include <map>
#include <string>

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

int main() {
    int a;
    std::cin >> a;
    int b;
    std::cin >> b;

    for (int n=a;n<=b;n++)
    {
        if (n>9)
        {
            if (n%2 == 0)
            {
                std::cout << "even" << std::endl;
            }
            else
            {
                std::cout << "odd" << std::endl;
            }
        }
        else
        {
            print_number(n);
        }
    }

    
    return 0;
}
