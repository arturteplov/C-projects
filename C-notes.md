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
- strscmp(x, "Deposit") == 0 //means-> will compare entire string for 0 difference, not character

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

## Day 2 – 

✅ Worked
-
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










