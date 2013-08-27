// replace spaces in string with '%20'
 
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


size_t replace_spaces(char *string, int len); //return new string length


int main()
{
    char *string = NULL;
    size_t lencap = 0;

    puts("Please enter a string.");

    int len = getline(&string, &lencap, stdin);

    replace_spaces(string, len);
    puts(string);

    return 0;
}


size_t replace_spaces(char *string, int len)
{
    int count = 0;
    char new_string[3*len];
    int i,k;

    for (i=k=0; string[i]; i++)
    {
        if (string[i] == ' ')
        {
            count +=1;
            new_string[k] = '%';
            new_string[k+1] = '2';
            new_string[k+2] = '0';
            k+=3;
        }
        else
        {
            new_string[k] = string[i];
            k++;
        }
    }
    new_string[k] = '\0';
    realloc(string, len + count * 3);
    strncpy(string, new_string, len + count *3);
    return len + count*3;
}

