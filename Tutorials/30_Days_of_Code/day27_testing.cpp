

class TestDataEmptyArray {
public:
    static vector<int> get_array() {
        vector<int> empty_array={};
        return empty_array;
    }

};

class TestDataUniqueValues {
public:
    static vector<int> get_array() {
        vector<int> unique_array={0,2};
        return unique_array;
    }

    static int get_expected_result() {
        return 0;
    }

};

class TestDataExactlyTwoDifferentMinimums {
public:
    static vector<int> get_array() {
        int max_index=31;
        vector<int> two_min_array;
        for (int i=0;i<max_index;i++)
        {
            if ( (i==5) || (i==24) )
            {
                two_min_array.push_back(7);
            }
            else {
              two_min_array.push_back(i+8);
            }          
        }
        return two_min_array;
    }

    static int get_expected_result() {
        return 5;
    }

};

