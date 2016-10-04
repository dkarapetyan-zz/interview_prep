#include <stdio.h>
#include <string.h>


#define MAXLINE 1000


char string[MAXLINE];
void itob(int n, char s[], int b);
 void reverse(char s[]);


int main()
{
itob(-23, string, 5); 
printf("%s\n", string);
 
return 0;
}

void itob(int n, char s[], int b) {
int sign=0;
int i=0;


if ((sign = n) < 0) {
  n = -n;
}




while (n > 0) {
  s[i++] = n % b + '0';
  n /= b;
}
if (sign < 0)
{
  s[i++]='-';
reverse(s);
  s[i] = '\0';
}
else {
reverse(s);
  s[i]='\0';
}




}
/* reverse:  reverse string s in place */
void reverse(char s[])
{
  int c, i, j;
  for (i = 0, j = strlen(s)-1; i < j; i++, j--) { 
    c = s[i];
    s[i] = s[j];
    s[j] = c; 
  }
}
