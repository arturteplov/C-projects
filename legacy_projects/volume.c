//coding with ChatGPT

#include <stdio.h>      // for file input/output (fopen, fread, fwrite, fclose, fprintf)
#include <stdlib.h>     // for exit handling and atof (string → float conversion)
#include <stdint.h>     // for fixed-width integer types like uint8_t and int16_t

// WAV files have a fixed 44-byte header we must copy as-is (metadata, not sound data).
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check that the user gave exactly 3 arguments:
    // 1. input file
    // 2. output file
    // 3. volume factor
    // We don't need more or fewer, so we enforce it here.
    if (argc != 4) {
        fprintf(stderr, "Usage: %s input.wav output.wav factor\n", argv[0]);
        return 1;   // return error because the program cannot run without these args
    }

    // Store arguments into named variables so the code is easier to read.
    char *infile = argv[1];   // first argument: input filename
    char *outfile = argv[2];  // second argument: output filename
    float factor = atof(argv[3]); // third argument: volume multiplier (string → float)

    // Open the input file for reading ("rb" = read binary).
    // We need binary because WAV is not text, it's raw bytes.
    FILE *in = fopen(infile, "rb");
    if (in == NULL) {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;   // can't continue without input file
    }

    // Open the output file for writing ("wb" = write binary).
    // If file doesn't exist, it's created. If it exists, it gets overwritten.
    FILE *out = fopen(outfile, "wb");
    if (out == NULL) {
        fprintf(stderr, "Could not create %s.\n", outfile);
        fclose(in);  // must close input before returning
        return 1;    // can't continue without output file
    }

    // Copy header: the first 44 bytes must be identical (contains WAV metadata).
    // We don't modify it, so just read it into a buffer and write it out.
    uint8_t header[HEADER_SIZE];                // unsigned 8-bit integers = raw bytes
    fread(header, HEADER_SIZE, 1, in);          // read exactly 44 bytes from input
    fwrite(header, HEADER_SIZE, 1, out);        // write those 44 bytes to output

    // Now handle the actual audio data (16-bit PCM samples).
    // We read one sample at a time, multiply by factor, then write back.
    int16_t sample; // signed 16-bit integer = standard WAV audio sample type
    while (fread(&sample, sizeof(int16_t), 1, in)) {
        sample = sample * factor;                          // adjust volume
        fwrite(&sample, sizeof(int16_t), 1, out);          // write new sample
    }

    // Close files to free resources (always good practice).
    fclose(in);
    fclose(out);

    // No need to free header/sample manually → they are on the stack, not malloc’d.
    // No other code is necessary, because:
    // - We don’t need to parse the header (just copy it).
    // - We don’t need to know the length ahead (loop until fread fails).
    // - Error handling was already done.
    return 0;   // success
}

---------

#include <stdio.h>      // file I/O
#include <stdlib.h>     // atof, exit
#include <stdint.h>     // uint8_t, int16_t

const int h = 44;       // header size (44 bytes for WAV)

int main(int a, char *b[])
{
    // Check command-line arguments count
    if (a != 4) {
        fprintf(stderr, "Usage: %s input.wav output.wav factor\n", b[0]);
        return 1;
    }

    // Assign arguments to short names
    char *c = b[1];     // input file name
    char *d = b[2];     // output file name
    float e = atof(b[3]); // volume factor

    // Open input file
    FILE *f = fopen(c, "rb");
    if (f == NULL) {
        perror("fopen input");
        return 1;
    }

    // Open output file
    FILE *g = fopen(d, "wb");
    if (g == NULL) {
        perror("fopen output");
        fclose(f);
        return 1;
    }

    // Copy WAV header unchanged
    uint8_t i[h];
    fread(i, h, 1, f); // = read 1 block of 44 bytes from file f into array i.
    fwrite(i, h, 1, g); // = write 1 block of 44 bytes from array i into file g.

    // Process samples
    int16_t j;
    while (fread(&j, sizeof(int16_t), 1, f)) {
        j = j * e;                          // adjust volume
        fwrite(&j, sizeof(int16_t), 1, g);  // write sample
    }

    // Close files
    fclose(f);
    fclose(g);

    return 0;
}

------------
#include <stdio.h>
#include <stdlib.h>

/// Exercise 1: Copy a text file character by character

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        return 1;
    }

    FILE *x = fopen(argv[1], "r");
    if (x == NULL)
    {
        printf("Input file can't be opened.\n");
        return 1;
    }

    FILE *y = fopen(argv[2], "w");
    if (y == NULL)
    {
        printf("Output file can't be opened.\n");
        fclose(x);
        return 1;
    }

    int stuff;  // use int for fgetc
    while ((stuff = fgetc(x)) != EOF)
    {
        fputc(stuff, y);
    }

    fclose(x);
    fclose(y);

    printf("Copying was successful, Artur.\n");
    return 0;
}




----

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

///Exercise 2: Copy a binary file in blocks

//Open a .wav or .jpg file.

//Create an output copy.

//Use a buffer, e.g. uint8_t buffer[512];.

//Read with fread(buffer, 1, 512, inp_file) until EOF.

//Write with fwrite(buffer, 1, bytes_read, out_file).



int main(int argc, char * argv[])
{

    if (argc !=3)
    {
        printf("Usage: %s <input file name> <output file name>\n", argv[0]); 
        return 1;
    }

    FILE * x = fopen (argv[1], "rb"); //opening wav, jpeg file
    if (x == NULL)
    {
        printf ("File can't be opened...\n");
        return 1; 
    }


    FILE * y = fopen (argv[2], "wb");
    if (y == NULL)
    {
        printf ("File can't be opened...\n");
        fclose(x); 
        return 1; 
    }


    uint8_t buffer[512]; 
     size_t bytes_read;



    while((bytes_read = fread(buffer, 1, sizeof(buffer), x)) > 0) //fread returns number of elevemts read -> 0 when file ends
    {
        fwrite(buffer, 1, bytes_read, y);
    }

    

    fclose (x); 
    fclose(y);

    return 0; 



}

-------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

///Exercise 2: Count characters in a file

//Open a .txt file.

//Read every byte with fgetc.

//Count how many times each ASCII character appears.

//Print frequencies (e.g., 'a' = 42 times).



int main(int argc, char * argv[])
{

    if (argc !=2)
    {
        printf("Usage: %s <input file name>\n", argv[0]); 
        return 1;
    }

    FILE * x = fopen (argv[1], "rb"); //opening wav, jpeg file
    if (x == NULL)
    {
        printf ("File can't be opened...\n");
        return 1; 
    }




    int counter [256] = {0}; 
    int c ; 

    while ((c = fgetc(x)) != EOF) // EOF returns (-1) when done
    {
        counter[c] ++;  //increment count for the character from file

        
    }
    fclose(x);

    
    //print frequences
    for (int i = 0; i < 256; i++)
    {
        if (counter[i] > 0)
        {
            if (i >= 32 && i <= 126) // printable ASCII
                {
                    printf("'%c' = %d times\n", i, counter[i]);
                }
            else
            {
                printf("0x%02X = %d times\n", i, counter[i]);
            }
                
        }
    }
        


    


    
    return 0; 

}





----

E#include <stdio.h>
#include <string.h>
#include <stdlib.h>

///Exercise 4: Skip header, copy rest

//Take a .wav file.

//Read and copy the first 44 bytes unchanged (header).

//Then read the rest as int16_t samples.

//Multiply each sample by 0.5 (reduce volume).

//Write the modified samples to a new file.


const int header = 44; 

int main(int argc, char * argv[])
{

    if (argc !=4)
    {
        printf("Usage: %s <input file name> <input file name> factor\n", argv[0]); 
        return 1;
    }
    float factor = atof(argv[3]); 

    FILE * x = fopen (argv[1], "rb"); //opening wav, jpeg file
    if (x == NULL)
    {
        printf ("File can't be opened...\n");
        return 1; 
    }

    FILE * y = fopen (argv[2], "wb"); //creating new file
    if (y == NULL)
    {
        printf ("File can't be created...\n");
        return 1; 
    }


    //Copy header 
    uint8_t buffer [header]; 
    fread(buffer, 1, header, x); 
    fwrite(buffer, 1, header, y); 
    
    //Process samples
    int16_t sample; 

    while (fread(&sample, sizeof(int16_t), 1, x))
    {
        sample = sample * factor; 
        fwrite(&sample, 1, sizeof(int16_t), y); 
    }

    fclose(x);
    fclose(y);
    
    printf("Wav was created!\n"); 

    return 0 ; 






    

}
------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

///Exercise 4: Skip header, copy rest

//Take a .wav file.

//Read and copy the first 44 bytes unchanged (header).

//Then read the rest as int16_t samples.

//Multiply each sample by 0.5 (reduce volume).



//Write the modified samples to a new file.


const int header = 44; 

int main(int argc, char * argv[])
{

    if (argc !=4)
    {
        printf("Usage: %s <input file name> <input file name> factor\n", argv[0]); 
        return 1;
    }
    float factor = atof(argv[3]); 

    FILE * x = fopen (argv[1], "rb"); //opening wav, jpeg file
    if (x == NULL)
    {
        printf ("File can't be opened...\n");
        return 1; 
    }

    FILE * y = fopen (argv[2], "wb"); //creating new file
    if (y == NULL)
    {
        printf ("File can't be created...\n");
        return 1; 
    }


    //Copy header 
    uint8_t buffer [header]; 
    fread(buffer, 1, header, x); 
    fwrite(buffer, 1, header, y); 
    
    //Process samples
    int16_t sample; 

    while (fread(&sample, sizeof(int16_t), 1, x))
    {
        sample = sample * factor; 
        fwrite(&sample, 1, sizeof(int16_t), y); 
    }

    fclose(x);
    fclose(y);
    
    printf("Wav was created!\n"); 

    return 0 ; 






    

}


------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

///
//Exercise 5: Merge two files

//Open two text files, part1.txt and part2.txt.

//Create merged.txt.

//Copy the entire content of file1, then append file2.

//Bonus: Add a separator line like "--- END OF PART 1 ---".
//


int main(int argc, char * argv[])
{

    if (argc !=4)
    {
        printf("Usage: %s <file1> <file2> <output>\n", argv[0]); 
        return 1;
    }

    FILE * x = fopen (argv[1], "rb"); //opening wav, jpeg file
    if (x == NULL)
    {
        printf ("File can't be opened...\n");
        return 1; 
    }

    FILE * y = fopen (argv[2], "rb"); //reading file
    if (y == NULL)
    {
        printf ("File can't be opened...\n");
        fclose(x);
        return 1; 
    }

    FILE * z = fopen (argv[3], "wb"); //creating new file 
    if (z == NULL)
    {
        printf ("File can't be created...\n");
        fclose(x); 
        fclose(y); 
        return 1; 
    }

    //////1) Copying x into z 
    size_t bytes;
    uint8_t buffer [512]; 

    while  ((bytes = fread(buffer, 1, sizeof(buffer), x)) > 0)

    {
        fwrite(buffer, 1, bytes, z); 
    }

fprintf(z, "\n--- END OF PART 1 ---\n"); 


    //2) Append y to z

while ((bytes = fread(buffer, 1, sizeof(buffer), y)) > 0)

    {
        fwrite(buffer, 1, bytes, z); 
    }
  

    fprintf(z, "\n-=-=-=-=-=-=-FINAL-=-=-=-=-=-=-\n"); 


    fclose(x); 
    fclose(y); 
    fclose(z); 

    printf("DONE! %s was merged with %s. Result: %s\n", argv[1],argv[2],argv[3] ) ;

    return 0 ; 



}

-------






    