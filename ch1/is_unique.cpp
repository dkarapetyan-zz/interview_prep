// check to see if string has all unique characters

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define SIZE 256 // support for ASCII character set

int array[SIZE] = {0};
bool is_unique(const char *string);

int main()
{
    char *string = NULL;
    size_t linecap = 0;
    printf("%s\n", "Please enter a string");
    getline(&string, &linecap, stdin);

    printf("%d\n", is_unique(string));
    return 0;
}


bool is_unique(const char *string)    
{
    for (int i = 0; i< SIZE; i++)
    {
        if (string[i])
        {
            if (array[(int)string[i]] == 0)
                array[(int)string[i]]+=1;
            else
                return false;
        }
        else
            break;

    }

    return true;
}
