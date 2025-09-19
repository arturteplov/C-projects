//code by chatgpt


#include <stdio.h>
#include <stdlib.h>


int cmpfunc (const void *a, const void *b)
{
    return (*(int*)a - *(int*)b);
}


int main (int argc, char * argv[])
{

    if (argc != 2)
    {
        printf("Eror, must be only 2 CL arguments!");
        return 1;
    }

    FILE * x = fopen (argv[1], "r");

    if (x == NULL)
    {
        printf("File doesn't exist or can't be open");
        return 0;
    }
    else
    {
        printf("File has been opened successfully!");
    }

    int numbers [1000]; 
    int counter = 0; 
    while ((fscanf(x, "%d", &numbers[counter]) == 1))
    {
        counter++; 
        if (counter >= 1000)
        {
            break; 
        }
    }
    printf("Total numbers: %i\n", counter); 
    

    fclose(x);


    qsort(numbers, counter, sizeof(int),cmpfunc); 
    printf("Sorted numbers: \n"); 
    for (int i =0; i < counter; i++)
    {
        printf("%i\n", numbers[i]); 
    }
}





//Exercise 5 — Try Variations of Sorting

//Do any of these variants (pick one per run):

//Sort descending (modify cmpfunc).

//Sort by “last digit” of number (e.g. 32 → 2, 47 → 7).

//Read floats instead of ints (%f, float arr[], sizeof(float)).

//Read strings from file (words) and sort alphabetically (strcmp inside cmpfunc).

//Save sorted output into a new file "sorted.txt" with fprintf.
