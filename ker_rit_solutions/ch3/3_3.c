#include <stdio.h>
#include <string.h> 
#ifndef MAXLINE
#define MAXLINE 1000
#endif
void expand(char s1[], char s2[]);
char string2[8]= {'a', '-', 'z', '0', '-', '9','\0'};
char string1[MAXLINE];

int main()
{
  expand(string1, string2);
  printf("%s\n", string1);
  return 0;
}



void expand(char s1[], char s2[])
{
  int n = strlen(s2) -1;
  int i;
  int j;
  int k = 0;

  for (j = 1; j <= n; ++j) {


// first check for '-' character
    if (s2[j] == '-' && s2[j+1] != '-' && s2[j-1] != '-') {
      for (i = 0; i <= s2[j+1] - s2[j-1]; i++) { //fill first few elements with char

	s1[k + i] = (i + s2[j-1] );
      }

    k = k+1 + s2[j+1] - s2[j-1]; //restart the loop at appropriate index value, so you don't overwrite old vals
    }


  }
  s1[k++]='\0';
}
