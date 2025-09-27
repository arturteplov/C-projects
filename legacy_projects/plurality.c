#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

//ENTER 4 CL arguments , will be stored in char * argv[]
//NUmber of voters (pass: 3 or whatever) --> based on that number program will type (3,5,12 etc)
//Programm keep asking Vote,Vote,Vote --> you typing i.e Bob, Alice,ALice
//Program do math, and just said name  whatever appeared more frequently 

int main (int argc, char * argv[])
{
    if (argc !=4)
    {
        printf("Error of inconsistency: ");
        return 1; 
    }

    int voters ; 
    int k = 0; 
    printf("Number of votes: "); 
    scanf("%i", &voters); 

    char names [50][35]; 

    while (k < voters)
    {
        printf("Vote: ");
        scanf("%s", names[k]); 
        k++; 
    }

    int counter[50] = {0}; 

    for (int i = 0; i<voters ; i++ )
    {
        for (int j = 0; j <voters ; j++ )
        {
            if (strcmp(names[i], names[j]) == 0)
            {
                counter[i]++;   
            }
        }
    }

    int max_index = 0;
    for (int i = 1; i < voters; i++)
    {
        if (counter[i] > counter[max_index])
        {
            max_index = i;
        }
    }

    printf("%s\n", names[max_index]);

    return 0;
    
}

///-=-==-=-=-=-=-=-EXERCISE2=-=-=-=-=-=-=-=-=-///


//Write a program in C that finds which number appears the most frequently and prints it.


int main ()
{
    
    int numbers[8] = {3, 5, 3, 2, 5, 5, 2, 3};

    int counter [8] = {0}; 

    for (int i = 0; i <8; i++ )
    {
        for (int j = 0; j<8; j++)
        {
            if (numbers[i] == numbers[j])
            {
                counter[i] ++ ; 
            }
        }
            
        
    }

    int max_value = 0; 
    for (int i = 0; i <8; i++)
    {
        if (counter[i] > counter[max_value])
        {
            max_value = i; 
        }
    }


    printf("The most frequent number: %i, total occurances: %i\n", numbers[max_value], counter[max_value]);

    return 0; 



    ///-=-==-=-=-=-=-=-EXERCISE3=-=-=-=-=-=-=-=-=-///


//You are given an array of strings (names of fruits):


//Write a program in C that finds which fruit appears the most frequently and prints both:

//the fruit name

//the number of times it appears

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>


int main ()
{
    
    char fruits[6][20] = {"apple", "banana", "apple", "orange", "banana", "apple"};

    int size = sizeof(fruits)/sizeof(fruits[0]); 

    int counter [50] = {0};

    for (int i = 0; i< size; i++)
    {
        for (int  j= 0; j< size; j++)
        {
            if(strcmp(fruits[i], fruits[j])==0)
            {
                counter[i] ++;
            }
        }
    }

    
    int freq_value = 0; 
    for (int i = 0; i< size; i++)
    {
        if (counter[i] > counter[freq_value])
        {
            freq_value = i; 
        }
    }
    printf("The most frequent fruits: %s, the number of times appeared: %i\n", fruits[freq_value], counter[freq_value]) ; 

    return 0; 
}




