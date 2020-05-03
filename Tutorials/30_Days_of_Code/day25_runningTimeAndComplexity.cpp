#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

void checkPrime(const int &n)
{
    if (n==1)
    {
        std::cout<<"Not prime"<<std::endl;
        return;
    }
    if (n==2)
    {
        std::cout<<"Prime"<<std::endl;
        return;
    }

    int sq = sqrt(n);
    for(int i = 2; i <= sq; i++) 
    {
        if(n%i == 0) 
        {
            std::cout<<"Not prime"<<std::endl;
            return;
        }
    }
    std::cout<<"Prime"<<std::endl;
}

int main() {
    int T;
    std::cin>>T;   
    int input[T];
    for (int i=0;i<T;i++)
    {
        std::cin>>input[i];
        checkPrime(input[i]);
    }
    return 0;
}
