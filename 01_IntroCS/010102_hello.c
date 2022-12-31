#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("Your Name: ");
    printf("hello, @s\n", answer);
}