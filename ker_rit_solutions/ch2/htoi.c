#include <stdio.h>
#define NO 0
#define YES 1
int htoi(char s[], int length);
int hex=YES;

int main()
{
    char string[5] = {'0', 'X', '0', '2', 'F'};
    int num=htoi(string, 5);
    if (hex == YES)
	printf("%d", num);
    else
	printf("\n%s", "You didn't enter a hexadecimal string. Please retry.");
} 

int htoi(char s[], int length)
{
    int n = 0;

    for (int i = 0; i < length; ++i) {
	if (s[i] == 'x' || s[i] =='X') {
	}

	else if (s[i] >= 'a' && s[i] <= 'f')
	    n = 16 * n + (s[i] - 'a' + 10);

	else if (s[i] >= 'A' && s[i] <= 'F')
	    n = 16 * n + (s[i] - 'A' + 10);

	else if (s[i] >= '0' && s[i] <= '9')
	    n = 16 * n + (s[i] - '0');

	else {
	   	    hex=NO;
	    break;
	}
    }
    return n;


}
