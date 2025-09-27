#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>




char upper[26] ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
char lower[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z'};

char text [100];
char cipher [26] ;
int key;

//functions
int output_cipher(char *x);



int main(void)
{
    //Input
    while(1)
    {
    printf("Enter a word: ");
    scanf("%s", text);
    if (strcmp(text, "NO") ==0) //Type NO to finish program
    {
        break;
    }
    else
    {
        printf("Enter a shift key: ");
        scanf("%i", &key);
        output_cipher(text);
    }


    }
    return 0; 
}



int output_cipher(char *x)
{
    int i;
    for (i =0; x[i] != '\0'; i++)
    {
        if(!isalpha(x[i]))
        {
            cipher[i] = x[i];
        }
        else if(isupper(x[i]))
        {
            int index = x[i] - 'A';
            int new_index = (index + key) % 26;
            cipher[i] = upper[new_index];
        }
        else if(islower(x[i]))
        {
            int index2 = x[i] - 'a';
            int new_index2 = (index2 + key) % 26;
            cipher[i] = lower[new_index2];
        }
    }
    cipher[i] = '\0';
    printf("%s\n", cipher);
    return 0;
}




