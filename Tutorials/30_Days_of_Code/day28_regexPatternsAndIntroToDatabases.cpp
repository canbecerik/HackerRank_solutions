#include <bits/stdc++.h>
#include <string>
#include <regex>

using namespace std;

vector<string> split_string(string);

bool checkGmail (const std::string emailID)
{
    // function to check if gmail
    regex rMailCheck("\\S+\\@gmail\\.com");
    return regex_match(emailID, rMailCheck);    
};

bool comparator (std::string x, std::string y)
{
    // simple compare function
    return (x<y);
}

int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    vector<string> sorted_names;

    for (int N_itr = 0; N_itr < N; N_itr++) {
        string firstNameEmailID_temp;
        getline(cin, firstNameEmailID_temp);

        vector<string> firstNameEmailID = split_string(firstNameEmailID_temp);

        string firstName = firstNameEmailID[0];

        string emailID = firstNameEmailID[1];
        if (checkGmail(emailID))
        {
            // add name to list of names to sort if using gmail
            sorted_names.push_back(firstName);
        }
    }
    std::sort(sorted_names.begin(),sorted_names.end(),comparator);
    for (std::vector<std::string>::iterator it=sorted_names.begin(); it!=sorted_names.end(); ++it)
    {
        std::cout << *it << std::endl;
    };
    return 0;
}



vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
