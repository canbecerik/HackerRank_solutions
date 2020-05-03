#include <iostream>
#include <bits/stdc++.h> 
#include <queue>

using namespace std;

class Solution {
public:
    void pushCharacter (const char &ch)
    {
        s.push(ch);
    };
    void enqueueCharacter (const char &ch)
    {
        q.push(ch);
    };
    char popCharacter()
    {
        char ret_val = s.top();
        s.pop();
        return ret_val;
    };
    char dequeueCharacter()
    {
        char ret_val = q.front();
        q.pop();
        return ret_val;
    };
private:
    
std::stack <char> s;
std::queue <char> q;

};

