
class Calculator : public AdvancedArithmetic {
public:
    int divisorSum(int n) {
        int div_total=n;
        for (int i=1;i<=(n/2);i++)
        {                     
            if (n%i == 0)
            {
                div_total+=i;
            }
        }
        return div_total;
    }
};

