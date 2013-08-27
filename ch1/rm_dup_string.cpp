//remove duplicate characters in a string
//

#include <stdlib.h>
#include <stdio.h>

#define SIZE 100

int da_array[SIZE]={0};


void rm_dup(char *string, int len );



int main()
{
    char *string = NULL;
    size_t linecap = 0;

    puts("Please enter a string");

    int len = getline(&string, &linecap, stdin);
    rm_dup(string, len);
    puts(string);
    return 0;
}


void rm_dup(char *string, int len)
{
    int last = 0;
    for (int i = 0; i < len; i++)
    {
        da_array[(int)string[i]] += 1; 
        if (da_array[(int)string[i]] == 1)
        {
            string[last] = string[i];
            last++;
        }
    }
    string[last] = '\0';
} 
