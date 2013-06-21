#include <stdio.h>
#define MAXLINE 1000


int strend(char *s, char *t);

int main()
{
  char string[MAXLINE]= "bobo went";
  char anostring[MAXLINE]= "ent";
  printf("%d\n", strend(string, anostring));
  return 0;
}

int strend(char *s, char *t)
{
  char *begint = t;

  while(*s++ != '\0') {
    ; 
  }
  while(*t++ != '\0') {
    ; 
  }


  s -= 1;
  t -= 1;

  while(*s-- == *t-- ) {
    ;  
  }

  if (*begint == *(t+2)) {
    return 1;
  }

  else
    return 0;

}
