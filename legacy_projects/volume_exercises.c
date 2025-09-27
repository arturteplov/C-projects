#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Exercise 1: Copy a binary file in blocks

int main(int argc, char * argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <input file name> <output file name\n", argv[0]);
        return 1;
    }

    FILE * x = fopen(argv[1], "rb"); 
    if (x == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        return 1; 
    }

    FILE * y = fopen(argv[2], "wb"); 
    if (y == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        fclose(x); 
        return 1; 
    }

    uint8_t buffer[512]; 
    size_t bytes; 

    while((bytes = fread(buffer, 1, sizeof(buffer), x))> 0)
    {
        fwrite(buffer, 1, bytes, y);
    }


    fclose(x); 
    fclose(y);
    
    return 0; 


}


------

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Exercise 2: Copy a text file character-by-character




int main(int argc, char * argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <input file name> <output file name\n", argv[0]);
        return 1;
    }

    FILE * x = fopen(argv[1], "rb"); 
    if (x == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        return 1; 
    }

    FILE * y = fopen(argv[2], "wb"); 
    if (y == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        fclose(x); 
        return 1; 
    }

    int stuff; 

    while ((stuff = fgetc(x)) != EOF)
    {
        fputc(stuff, y); //copying stuff into new file
    }

    fclose(x);
    fclose(y);

    printf("copying is complete.\n"); 

    return 0; 

}


--------

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Exercise 3: Count character frequencies

int main(int argc, char * argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <input file name> <output file name\n", argv[0]);
        return 1;
    }

    FILE * x = fopen(argv[1], "rb"); 
    if (x == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        return 1; 
    }

    FILE * y = fopen(argv[2], "wb"); 
    if (y == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        fclose(x); 
        return 1; 
    }


    //Counter 
    int counter[256] ={0}; 
    int j;  

    while ((j = fgetc(x)) != EOF)
    {
        counter[j] ++; 
    }


    //Frequences 


    int total = 0; 
    for (int i = 0; i < 256; i++) // can be used for(int i =32; i<= 126; i++)
    {
        if (counter [i] > 0)
        {
            if (i >= 32 && i <= 126) // counter [i] >= 32 || counter [i] <= 126) = wrong
        {
            total += counter[i]; 
        }
        }
        
    }
    fclose(x); 
    fclose(y);

    printf("Total occurrences of printable characters (32–126): %i\n", total);

    
    return 0; 


}
------------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Exercise 4: Reduce WAV volume



const int header = 44; 

int main(int argc, char * argv[])
{
    if (argc != 4)
    {
        printf("Usage: %s <input file name> <output file name> <factor>\n", argv[0]);
        return 1;
    }

    float factor = atof(argv[3]); 

    FILE * x = fopen(argv[1], "rb"); 
    if (x == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        return 1; 
    }

    FILE * y = fopen(argv[2], "wb"); 
    if (y == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        fclose(x); 
        return 1; 
    }

    uint8_t buffer [header]; 
   
    
    fread(buffer, 1, sizeof(buffer), x);
    fwrite(buffer, 1, sizeof(buffer), y);

    //Processing the rest of the file

     int16_t sample; 
     int temp; 

    while (fread(&sample , 1, sizeof(int16_t), x))
    {
        temp = (int)sample * factor; 

        if (temp > 32767) 
        {
            temp = 32767;
        }

        if (temp < -32768) 
        {
            temp = -32768;
        }

        sample = (int16_t) temp; 
        fwrite(&sample, 1, sizeof(int16_t), y); 
    }

    fclose(x); 
    fclose(y);

    

    printf("This is done!\n"); 

    
    return 0; 


}
-------


#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Exercise 5: Merge two files



int main(int argc, char * argv[])
{
    if (argc != 4)
    {
        printf("Usage: %s <input file name1> <input file name2> <output file name> \n", argv[0]);
        return 1;
    }



    FILE * x = fopen(argv[1], "rb"); 
    if (x == NULL)
    {
        printf("Ooops file couldn't be open..\n");
        return 1; 
    }

    FILE * y = fopen(argv[2], "rb"); 
    if (y == NULL)
    {
        printf("Ooops file couldn't be opened..\n");
        fclose(x); 
        return 1; 
    }

    FILE * z = fopen(argv[3], "wb"); 
    if (z == NULL)
    {
        printf("Ooops file couldn't be created..\n");
        fclose(x); 
        fclose(y);
        return 1; 
    }


    //Copy 1 file x -> into 1 file z 

    uint16_t buffer [512]; //better to use unsigned char buffer[512]; (if format is unknown)

    size_t bytes ; 

    while ((bytes = fread(buffer, 1, sizeof(buffer), x)) > 0)
    {
        fwrite(buffer, 1, bytes, z); 
    }

    fprintf(z, "\n--- END OF PART 1 ---\n");  //if input files like WAV, JPED - this will corrupt them

    //Append 1 file y into 1 file z 

    while ((bytes = fread(buffer, 1, sizeof(buffer), y)) > 0)
    {
        fwrite(buffer, 1, bytes, z); 
    }

    fprintf(z, "\n--- THE END ---\n"); 



    fclose(x); 
    fclose(y);
    fclose(z);

    

    printf("<%s> was merged with <%s>. Merged file name: %s\n", argv[1],argv[2],argv[3]); 

    
    return 0; 


}
