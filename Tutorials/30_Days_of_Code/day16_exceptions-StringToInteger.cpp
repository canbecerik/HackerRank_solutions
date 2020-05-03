#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <stdexcept>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void str2integer(const std::string &S)
{
    try 
    {
        int i = std::stoi(S);
        std::cout << i << std::endl;
    }
    catch (std::invalid_argument const &e)
    {
        std::cout << "Bad String" << std::endl;
    }
}

int main(){
    string S;
    cin >> S;
    str2integer(S);
    return 0;
}
