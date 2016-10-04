/*Program to replace string with one or more blanks by a single blank.*/

#include <stdio.h>
int main()
{
  
    
  int c=getchar();		// Get the first two letters
  int d=getchar();

  if (c == EOF)  	// The base case. If you type nothing in, terminate
    return 0;
  else
    putchar(c);

  while(c != EOF) {       // Iterative Induction. All possible two char combos
    if (d == EOF)
      break;
    else if (c == ' ' && d != ' ') {
      putchar(d);
    }
    else if (c == ' ' && d == ' ')
      ;
    else if (c != ' ' && d == ' '){
      putchar(d);
    }
    else if (c != ' ' && d != ' ') {
      putchar(d);
    }
    c=d;
    d=getchar();
  }


  return 0;
}
