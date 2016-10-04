#include <stdio.h>
#define MAXLINE 1000


char * strcatMy(char *s, char *t);

int main()
{
  char string1[MAXLINE]="bobo";
  char string2[MAXLINE]="went";
printf("%s\n", strcatMy(string1, string2));
  return 0;
}

/* strcatMy: concatenate t to end of s; s must be big enough */ 

char *  strcatMy(char *s, char *t)
{
  char * begin = s;
  while(*s++ != '\0') {
   ; 
  }
  --s;
  
  

       while ((*s++ = *t++) ) /* copy t */
;


return begin;
}
