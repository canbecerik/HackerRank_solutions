

class Student :  public Person{
    private:
        vector<int> testScores;  
        char grade;
    
    public:
          // Write your constructor
        Student(string firstName, string lastName, int identification, vector<int> scores) : Person(firstName, lastName, identification), testScores(scores) {
            
        };
  
          // Write char calculate()
        char calculate(){
            long sum = 0;
            for(int &val : testScores){
                sum += val;
            }
            sum /= testScores.size();
            if(sum < 40){
                grade = 'T';
            } else if(sum < 55){
                grade = 'D';
            } else if(sum < 70){
                grade = 'P';
            } else if(sum < 80){
                grade = 'A';
            } else if(sum < 90){
                grade = 'E';
            } else {
                grade = 'O';
            }
            return grade;
        }
};

