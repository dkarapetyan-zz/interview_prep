//check if string2 is a counterclockwise rotation of string1

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool is_rotation(char *string1, char *string2);


int main()
{
    puts("Input a string, please.");
    char *string1 = NULL;
    size_t lencap1 = 0;
    int len1 = getline(&string1, &lencap1, stdin);
    string1[--len1] = '\0'; // getline includes terminating return character

    puts("Input string number two, please.");
    char *string2 = NULL;
    size_t lencap2 = 0;
    int len2 = getline(&string2, &lencap2, stdin);
    string2[--len2] = '\0';

    printf("%d\n", is_rotation(string1, string2));

    free(string1);
    free(string2);

    return 0;
}

bool is_rotation(char *string1, char *string2)
{
    size_t i = strlen(string1);
    size_t j = strlen(string2);

    bool q = false;

    if (i == j)
    {
        char *array = malloc(sizeof(char) * 2 * i);
        strcpy(array, string1);
        strcat(array, string1);

        if (strstr(array, string2))
            q = true;

        free(array);
    }

    return q;
}

