//-=-=-=-=-=STRUCT_EXERCISES-=-=-=-=-=//


//#1 Print book


#include <stdio.h>
#include <string.h>



struct Book{
    char title[50];
    char author[50];
    float price;
};

int main()
{
    struct Book book1;

    strcpy(book1.title, "Romeo & Julietta");
    strcpy(book1.author, "William Shakespeare");
    book1.price = 19.99;

    printf("Title of the book: %s, author: %s, price: %.2f\n", book1.title,book1.author, book1.price );

    return 0;
}

------

//#2 - Make an array of 5 struct Point { int x, y; } and assign coordinates to each.


#include <stdio.h>
#include <string.h>



struct Point{
    int x;
    int y;
    int z;
};

int main()
{
    struct Point coordinates = {3, 23, 1023132};

    printf("Our 3D coordinates: x=%i, x=%i, x=%i\n", coordinates.x, coordinates.y, coordinates.z);

    return 0;

}
------

//#3 - Assigning values to struct array


#include <stdio.h>
#include <string.h>


struct Point {
    int x;
    int y;
    int z;
};

int main()
{
    struct Point point[5];
    point[0].x = 412;
    point[1].x = 12;

    point[0].y = 242352452;
    point[1].y = -2;
    point[2].y = -5353;

    point[0].z = 0;
    point[1].z = 3233;

    printf("3D coordinates: x= %i, y= %i, z=%i\n", point[0].x,point[0].y, point[0].z);

    return 0;
}


----


//#4 - Write a function that takes a struct Student and prints all its grades.


#include <stdio.h>
#include <string.h>


struct Student {
    char name[50];
    char subject[50];
    float grade;
};

int main()
{
    struct Student student1 = {"John Doe", "physics", 3.9};

    printf("Student's name: %s, subject: %s, grade: %.2f\n", student1.name, student1.subject, student1.grade );

    return 0;
}
-----


//#5 Print Average Grade of student


#include <stdio.h>
#include <string.h>



float average_grade (float x[], int size);

struct Student {
    char name [50];
    float grades [5];
};

float temp [5] = {3.2, 2.4, 4, 4.9, 3.33};

int main()
{
    struct Student student1;
    strcpy (student1.name, "ARTUR TEPLOV");

    for (int i = 0; i<5; i++)
    {
        student1.grades[i] = temp[i];
    }

    printf("Student's name: %s , average grade: %.2f\n", student1.name, average_grade(student1.grades, 5));

    return 0;
}




float average_grade (float x[], int size)
{
    float sum = 0;
    for (int i=0; i<size; i++)
    {

        sum = (float) sum + x[i];
    }
    return sum/size;
}


-----

//#5 - Find Highest & Lowest Grade of student



#include <stdio.h>
#include <string.h>


struct Student {
    char name [50];
    float grades [5];

};


float highest(float x[], int size1);

float lowest(float y[], int size2);



float temp [5] = {3.2, 2.4, 4.5, 5, 4.3};

int main ()
{

    struct Student student1;
    strcpy(student1.name, "ARTUR TEPLOV");

    for (int i = 0; i<5; i++)
    {
        student1.grades[i] = temp[i];
    }

    printf("Student's name: %s, highest grade: %.2f, lowest grade: %.2f\n", student1.name, highest(student1.grades, 5), lowest(student1.grades, 5));

}


float highest(float x[], int size1)
{
    float start = x[0];

    for (int i=0; i<size1; i++)
    {

        if (x[i] > start)
        {
            start = x[i];
        }
    }
    return start;

}


float lowest(float y[], int size2)
{
    float start = y[0];

    for (int i=0; i<size2; i++)
    {

        if (y[i] < start)
        {
            start = y[i];
        }
    }
    return start;

}

//-=-=-=-=-=-=-=-=-=-=-=-=-=END-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--//