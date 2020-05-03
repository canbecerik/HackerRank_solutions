

struct Calculator
{ 
    int power(const int &n, const int &p)
    {
        if (n<0 || p<0)
        {
            throw std::runtime_error ("n and p should be non-negative");
        }        
        return pow(n, p);      
    }
};

