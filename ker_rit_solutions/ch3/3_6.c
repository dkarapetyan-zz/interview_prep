#include <stdio.h>
#include <string.h>


#define MAXLINE 1000


char string[MAXLINE];
void reverse(char s[]);
void itoa(int n, char s[], int w);


int main()
{
  itoa(23, string, 5); 
  printf("%s\n", string);

  return 0;
}

/* itoa:  convert n to characters in s */
void itoa(int n, char s[], int w)
{
  int i, sign;
  if ((sign = n) < 0)  /* record sign */
    n = -n;          /* make n positive */
  i = 0;
  do {      /* generate digits in reverse order */
    s[i++]=n%10+'0'; /*getnextdigit*/
  } while ((n /= 10) > 0);
if (sign < 0)
  s[i++] = '-';
  
  while(i < w) {
    s[i++] = '*';
  }
  s[i] = '\0';
    reverse(s);

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
