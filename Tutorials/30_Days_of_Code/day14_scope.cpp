

	Difference(vector<int> array)
    {
        elements = array;
    }

    void computeDifference()
    {
        sort (elements.begin(), elements.end());
        maximumDifference = elements.back()- *elements.begin();
    }

