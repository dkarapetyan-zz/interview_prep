// reverse string in place
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char *array, int x, int y);
void reverse(char *array, int len);

int main()
{
    char *string = NULL;
    size_t lencap = 0;

    printf("%s\n", "Input a string");
    int len = getline(&string, &lencap, stdin);
    reverse(string, len);
    printf("%s", string);
    return 0;
}


void swap(char *array, int x, int y)
{
char temp = array[x];
array[x] = array[y];
array[y] = temp;
}


void reverse(char *array, int len)
{
    for (int i = 0; i < len/2; i++)
        swap(array, i, len - i -1);
}




