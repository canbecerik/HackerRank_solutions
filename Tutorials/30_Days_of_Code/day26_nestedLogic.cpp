#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <istream>

#define DAY_FINE 15
#define MONTH_FINE 500
#define YEAR_FINE 10000

class Book
{
    public:
    int total_fine;
    Book(std::string &actual_input, std::string &due_input)
    {
        total_fine=0;
        processData(actual_input, due_input);
    };
    private:
    void processData(std::string &actual_input, std::string &due_input)
    {
       int act_data[3];
       int due_data[3];
       for (int i=0;i<3;i++)
       {
           act_data[i]=getDigit(actual_input);
           due_data[i]=getDigit(due_input);
       };
       total_fine=calcFine(act_data, due_data);
       std::cout << total_fine << std::endl;

    };
    int getDigit(std::string &temp)
    {
       char delim=' ';
       std::size_t pos=0;
       int token;
       pos = temp.find(delim);
       token = std::stoi(temp.substr(0, pos));
       temp.erase(0, pos+1);
       return token;
    };
    int calcFine(int act_data[], int due_data[])
    {
        int act_year=act_data[2];
        int due_year=due_data[2];
        int act_month=act_data[1];
        int due_month=due_data[1];
        int act_day=act_data[0];
        int due_day=due_data[0];

        if (act_year >= due_year)
        {
            if (act_year > due_year) return YEAR_FINE;
            if (act_month>=due_month)
            {
                if (act_month > due_month) return MONTH_FINE * (act_month - due_month);
                if (act_day >= due_day)
                {
                    if (act_day > due_day) return DAY_FINE * (act_day - due_day);
                }
            }
        }
        return 0;
    }
};
int main() {
    std::string actual_input, due_input;
    getline(std::cin,actual_input);
    getline(std::cin, due_input);
    Book LibraryBook(actual_input, due_input);
    return 0;
}
