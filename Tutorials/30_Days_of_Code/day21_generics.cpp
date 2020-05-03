

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/
template <typename T>
void printArray (vector<T> &gen_array)
{
    for (int i=0;i<gen_array.size();i++)
    {
        std::cout << gen_array[i] << std::endl;
    }


}

// Write your code here

