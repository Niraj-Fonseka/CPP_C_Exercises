#include <iostream>

//https://www.tutorialspoint.com/cplusplus/cpp_polymorphism.htm

using namespace std;

class Shape{
    protected:
        int width, height;

    public:
        Shape( int a = 0 , int b = 0 ) {
            width = a ;
            height = b;
        }

        //virtual function , dynamic linkage , late binding
        virtual int area() = 0;
        virtual string name() = 0;
};

class Rectangle: public Shape{
    
    public:
        Rectangle( int a = 0 , int b = 0 ):Shape(a,b) {}

        int area(){
            
            cout << "Rectangle class area : " << (width * height) << endl;
            return (width * height);
        }

        string name(){
            cout << "This is a Rectangle" << endl;

        }
};

class Triangle: public Shape{
    public:
        Triangle( int a = 0 , int b = 0):Shape(a,b){}

        int area(){
            cout << "Traingle class area : " << (width * height / 2) <<  endl;
            return (width * height / 2);
        }

        string name(){
            cout << "This is a Traingle" << endl;
            
        }
};



int main() {
    Shape *shape;
    Rectangle rec(10,7);
    Triangle tri(10,5);

    shape = &rec;

    shape->area();
    shape->name();

    shape = &tri;

    shape->area();
    shape->name();

    return 0;
}