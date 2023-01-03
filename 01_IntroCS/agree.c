// Logical Operatos

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char question = get_char("Do you agree? (y/n)");

    if (question == 'Y' || question == 'y')
    {
        printf("AGREED\n");
    }
    else if (question == 'N' || question == 'n')
    {
        printf("NOT AGREED\n");
    }
}