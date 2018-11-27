#include <iostream>
#include <cstring>
using namespace std;


class Person {
    private:
        char *name;
        int   age;
        char *location;

    public:
        Person(const char *name= NULL , const char *location=NULL , const int age=0 ); //Constructor
        ~Person() {
            delete[] name;
            delete[] location;
        }
        Person(const Person&); // copy constructor
        void toString(){
            cout << name  << endl;
        }

        void updateInfo(const char * , const char * , const int);
}

//Constructor
Person::Person(const char *name ,  const char *location , const int age ){
    name = new char[strlen(name) + 1];
    strcpy(name , name);
}





