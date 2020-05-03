

// Write your MyBook class here
class MyBook : Book
{
    private:
        int price;
    public:
        string title;
        string author;

    MyBook (string title_, string author_, int price_) : Book(title_,author_),price(price_){}

    void display()
    {
        cout << "Title: " << Book::title << endl;
        cout << "Author: " << Book::author << endl;
        cout << "Price: " << price << endl;
    }
    
// End class
};
