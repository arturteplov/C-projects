#include <stdio.h>
#include <string.h>
#include <ctype.h>

int balance = 5000;
char words[10]; //array for input
int transactions[5]; // store 5 transactions as well
int transaction_index =0;


//functions
int output_atm (char *x);
int record_transaction(int y);


//
int main(void)
{
    //Input
    while(1)
    {
        printf("Hi! You may select operation: <deposit>, <withdraw>, <track balance>, <exit>  ");
        scanf("%s", words);
        if (strcmp(words, "Exit") == 0 || strcmp(words, "exit") == 0 || strcmp(words, "EXIT") == 0)
        {
            printf("Thank you for your partnership and good luck!\n");
            break;
        }
        else
        {
            output_atm(words);
        }

    }

}

//-=-=-=-=-=-=-=-=-=-=-=//

int output_atm (char *x)
{

        if (strcmp(x, "Deposit") == 0 || strcmp(x, "deposit") == 0 || strcmp(x, "DEPOSIT") == 0) // DEPOSIT
        {
            int amount;
            printf("How much do you require to deposit?\n");
            scanf("%i", &amount);

            if (amount <50)
            {
                printf("Sorry. The minimum deposit amount is $50 USD\n");
            }
            else
            {
                balance += amount;
                printf("Congratulations! Your balance has $%i USD now!\n",balance);
                record_transaction(amount);
            }

        }

        //WITHDRAW -=-=-=-=-=-=-=-=-=-=-=//

        else if (strcmp(words, "Withdraw") == 0 || strcmp(words, "withdraw") == 0 || strcmp(words, "WITHDRAW") == 0)
        {
            int amount;
            printf("How much you require to withdraw?\n");
            scanf("%i", &amount);
            if (amount <70)
            {
                printf("Sorry. The minimum withdrawal amount is $70 USD\n");
            }
            else if (amount>balance)
            {
                printf("Sorry. Insufficient balance, maybe try again... \n");
            }
            else
            {
                balance -= amount;
                printf("Withdrawal was successful! Your balance has $%i USD now!\n",balance);
                record_transaction(-amount);

            }

        }

        //TRACK BALANCE -=-=-=-=-=-=-=-=-=-=-=//

        else if (strcmp(words, "Track") == 0 || strcmp(words, "track") == 0 || strcmp(words, "TRACK") == 0)
        {

            printf("Total balance currently: %i\n", balance);
            printf("Last 5 transactions: ");
            for (int k = 0; k<5 ; k++)
                {
                    if (transactions[k]!=0)
                    {
                        printf("%i ", transactions[k]);
                    }

                }
            printf("\n");
        }


        //-=-=-=-=-=-=-=-=-=-=-=//


        else
        {
            printf("Invalid, perhaps try again..?\n");
        }
    return 0;

}




int record_transaction(int y)
{
    transactions[transaction_index%5] = y;
    transaction_index ++;
    return 0;
}


