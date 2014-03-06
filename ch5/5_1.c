#include <ctype.h>
#include <stdio.h>
#define BUFSIZE 100
#define MAXSIZE 1000
char buf[BUFSIZE]; /* buffer for ungetch */
int bufp = 0; /* next free position in buf */
int getch(void);
void ungetch(int);
int getint(int *pn);


int main()
{
  int array[MAXSIZE];
  int *pointer = array;
  getint(pointer); 
  printf("%d\n", *pointer);

  return 0;

}







int getch(void) /* get a (possibly pushed-back) character */ 
{
  return (bufp > 0) ? buf[--bufp] : getchar();
}


void ungetch(int c) 
{
  /* 
     push character back on input */
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters\n");
  else
    buf[bufp++] = c;
}


int getint(int *pn)
{
  int c, d=0, sign;
  while (isspace(c = getch())) /* skip white space */
    ;
  if (!isdigit(c) && c != EOF && c != '+' && c != '-')
  {
    ungetch(c); /* it is not a number */
    return 0;
  }
  sign = (c == '-') ? -1 : 1;
  if ((c == '+' || c == '-') && !isdigit(d=getch())) {
    ungetch(d);
  ungetch(c);
  return 0;
  }
  else
  {
    ungetch(d);
  }

  for (*pn = 0; c = getch(), isdigit(c);)
    *pn = 10 * *pn + (c - '0');
  *pn *= sign;
  if (c != EOF)
    ungetch(c);
  return c;
}
