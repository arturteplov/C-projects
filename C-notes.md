# C Notes – Growth Log  
----

## Day 1 – ATM simulator (part 1, part 2)

✅ Worked
-user input (e.g printf("How much do you require to deposit?)) -> then storing that input in declared integer variable (e.g int amount;)
- when user typed "EXIT", using $break$ in while(1) loop was helpful


❌ Failed
- was trying to scan array simply for match strings like "Deposit" --->  failed, thus must use code-> if (strcmp(x, "Deposit") ==0 via 1.<string.h> , 2.No index for array, 3. If it's a function, use parameter (e.g x) instead of global words -> otherwise parameter is useless. 
- using $break$ -> it's useless in for loops (where $for$ doesn't depend on _i_) but useful in infinite (e.g while(1)) loops when must be stopped or it will keep repeating forever.


💡 Insight
- string can't be in single quotes -> e.g required "Deposit" (not 'Deposit')
- VALID -> printf("%i", transactions[i]); //INVALID-> printf("%i", transactions);
-When setting up array of chars (e.g char words[10]) and possibly user may input long string and thus array may overflow so perhaps → consider char words[50].


🔄 To Review
- strcmp(x, "Deposit") == 0 //means-> will compare entire string for 0 difference, not character

 -scanf("%s", words); // means -> whatever user inpur (e.g "Deposit"), it's gonna store as {'D','e','p''o','s','i','t',\0} (not like array of strings)

-2D array --> char history[100][20]; --> //you can store up to 100 commands; 20 columns (each command can be up to 19 characters long (+1 for \0 end-of-string).)




🧩 Code Snippets

#1 (To execute code based on match in the array)

if (strcmp(x, "Deposit") == 0 || strcmp(x, "deposit") == 0) 
    {
        printf("How much you require to deposit of $USD amount? ");

        scanf("%i", &amount);
    }
why not useless -> scans array, once matched the string execute the code inside braces. 



#2 (To leverage for loop to iterate over array of strings)

char *valid_ops[] = {"deposit", "withdraw", "track", "exit"}; //list of commands you want to accept(not user input yet)
for (int i = 0; i < num_ops; i++)
{
    if (strcasecmp(words, valid_ops[i]) == 0)
    {
        printf("User chose: %s\n", valid_ops[i]);
        break;
    }
}

#3 
(To store strings into array by coping from buffer)

char history[100][20]; // store up to 100 commands
int history_index = 0;

scanf("%s", words); //reads 1 command and storing in buffer _words_

strcpy(history[history_index++], words); //copies the string from _words_
//E.G -> words = "deposit" -> strcpy(history[0], words); → now history[0] = "deposit".

#4 
(To enable user inpput multiple commands "deposit" + "withdraw")

char line[100];
fgets(line, sizeof(line), stdin);

char history[100][20];
int history_index = 0;

char *token = strtok(line, " \n"); //splitting each line into tokens 
while (token != NULL)
{
    strcpy(history[history_index++], token);
    token = strtok(NULL, " \n");
}

----

## Day 2.1 – Caesar cipher

✅ Worked
- int i; cipher[i] = '\0' ---> any garbage will be replaced with null terminator;

❌ Failed
- int output_cipher (char x) //means parameter = single character 'H'  vs   int output_cipher (char * x) //means parameter = string ("HELLO")
- scanf("%i", &key) --> must use '&' ; scanf("%s", text) --> array of strings without '&' ; scanf(" %c", &c); --> for chars must insert space + '&'

💡 Insight
- int index = x[i] - 'A'; ---> internally in C  any characher = integer, so even it doesn't make sense, it's applicable to make math with letters and get number;
-

🔄 To Review
- change input encryption logic (not single word, but multiple)
-

🧩 Code Snippets

#1 (to insert separate letters into array, not words)
char letters[3];
printf("Enter 3 letters: ");
scanf(" %c %c %c", &letters[0], &letters[1], &letters[2]);

#2 (to insert each integer separately and store it into array)
int arr[3];
printf("Enter 3 integers: ");
scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

----

## Day 2.2 – Student grade lookup (not finished yet)

✅ Worked
-
- 

❌ Failed
- scanf will be crazy if you input 2 arguments (e.g string) --> MUST use only 1 argument
- 

💡 Insight
- If you have an array of floats (e.g float grades[5]), then to create workable function aroun this array --> must add format like this $void update_grades(float y[], int size)$ and to call it -> $update_grades(grades, 5)$ 
- char names[10] = array can hold up to 10 chars ('A', 'B' etc); char names[10][50] = can hold up to 10 strings that can be up to 50 characters each --> "Artur Teplov", "John Doe".

🔄 To Review
- float grades [10][5] --> grades[0][0] first grade of first student ; grades[0][1] --> 2nd grade of first student etc
-

🧩 Code Snippets

-----

## Day 2.3 – Struct_exercises

✅ Worked
- declaring & printing struct function outside & inside of main
-using for loop to iterate over each float array inside of struct, and afterwards giving output whehn fucntion is called (inside of main)

❌ Failed
- when calling a fucntion in $printf$ (e.g highest(student1.grades, 5)) -> must match input of that function, e.g as float array here (float highest(float x[], int size1)) //otherwise compiler will complain.
-

💡 Insight
-if the function has output value, inside of the function always must be $return$ - no exceptions.
-structs are good to combine different data types like i.e chars & floats

🔄 To Review
-
-

🧩 Code Snippets

struct Student {
    char name [50];
    float grades [5];
};
int main()
{
struct Student student1;
strcpy (student1.name, "ARTUR TEPLOV");
}



----
## Day 3 – Opening a file + sorting integers there 

✅ Worked
- FILE * x = fopen (argv[1], "r") can open the file, returns NULL if non-existent
- qsort (numbers, counter, sizeof(int), cmpfunc) --> can sort input values however you want

❌ Failed
-a bit lack of understanding what's the sense of cmpfunc
-

💡 Insight
- fscanf(x, "%d", &numbers[counter]) == 1)) --> reads the file and can store in array (i.e numbers[1000])
-

🔄 To Review
- in qsort -> cmpfunc function must be reviewd 1 more time
- instead of integers, try strings + some custom case


🧩 Code Snippets
//#0 
   while ((fscanf(x, "%d", &numbers[counter]) == 1)) ---> to store strings/integers into array


//#1 Ascending (small → big) 3, 7 → -4 → negative → 3 before 7
int cmp_asc(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

//#2 Descending (big → small) 3, 7 → 4 → positive → 3 after 7.
int cmp_desc(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

//#3 Absolute Value Order --> Sorts like [-9, -2, 3, 10] → -2, 3, -9, 10.
#include <math.h>
int cmpfunc (const void *a, const void *b) {
    int x = abs(*(int*)a);
    int y = abs(*(int*)b);
    return x - y;
}

//#4 By Last Digit -_> 32, 47, 15 → sorted as 32 (2), 15 (5), 47 (7).
int cmp_last_digit(const void *a, const void *b) {
    int x = *(int*)a % 10;
    int y = *(int*)b % 10;
    return x - y;
}

//#5  Odd First, Even Later
int cmp_odd_even(const void *a, const void *b) {
    int x = *(int*)a;
    int y = *(int*)b;
    return (x % 2) - (y % 2);
}

//#6  STRINGS

//Alphabetic

int cmpfunc (const void*a, const void*b)
{
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}

//By length
int cmpfunc_len (const void*a, const void*b)
{
    const char *s1 = *(const char * const *)a;
    const char *s2 = *(const char * const *)b;
    if (strlen(s1) < strlen(s2)) return -1;
    if (strlen(s1) > strlen(s2)) return 1;
    return 0;
}

//#7 function for saving array into new file
void save_sorted(char *arr[], int n) 
{
    // Open a file named "sorted.txt" in write mode ("w")
    // "w" means: if the file exists → clear it; if not → create it.
    FILE *fp = fopen("sorted.txt", "w");

    // Always check if fopen worked.
    // If fopen fails (e.g. no permissions, disk full, etc.), fp == NULL.
    if (fp == NULL) {
        perror("Error opening file"); // print system error message
        return;                       // exit the function early
    }

    // Loop over all sorted elements in the array
    for (int i = 0; i < n; i++) {
        // Write each string into the file, followed by a newline
        // "%s\n" → print string + newline
        fprintf(fp, "%s\n", arr[i]);
    }

    // Close the file to make sure all data is flushed to disk
    fclose(fp);
}


----

## Day 4 – Opening a file -> reading strings + sorting them (alphab, by length)


✅ Worked
-  writing each string into a new file --->
 for (int i = 0; i < n; i++) {
        // "%s\n" → print string + newline
        fprintf(fp, "%s\n", arr[i]); // Write each string into the file, followed by a newline
    }

❌ Failed
-  Script is not case sensetive - not considering lowcase (i.e lowercase "tunnel" will come after "WORKS")
-  to store strings it must be 2D array -> char words [100] [100]

💡 Insight
- perror = as printf but also automatically tells cause of error
-

🔄 To Review
-  int cmpfunc (const void*a, const void*b) //comparative function for qsort
{
    return strcmp((const char*)a, (const char*)b);
}
-

🧩 Code Snippets

#1 if (fp == NULL) {
        perror("Error opening file"); // print system error message
        return;                       // exit the function early
    

#2 for (int i = 0; i < n; i++) {
        // "%s\n" → print string + newline
        fprintf(fp, "%s\n", arr[i]); // Write each string into the file, followed by a newline
    }

#3 FILE *fp = fopen("sorted.txt", "w");

----

## Day 4 – 

✅ Worked
-  

❌ Failed
-  
-  

💡 Insight
- 
-

🔄 To Review
-  
-

🧩 Code Snippets

#1 

----



















