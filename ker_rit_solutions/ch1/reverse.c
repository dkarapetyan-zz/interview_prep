#include <stdio.h>
#define MAXLINE 1000
int getlineMy(char []);
void reverse(char []); // reverse function


int main()
{
    char line[MAXLINE];

while (getlineMy(line) > 0) {
 reverse(line);
printf("%s", line); 
}

return 0;

}

void reverse(char s[]) {
    int i=0 , j=0;
    char temp;
    while ( s[i] != '\0')
     ++i; 
      --i;
    if (s[i] == '\n') {
   --i;
 while (j <= i/2) {
   temp = s[j];
   s[j] = s[i-j];
   s[i-j]=temp;
  ++j; 
 }
 
  
    }
    
} 

/* getlineMy:  read a line into s, return length  */
int getlineMy(char s[])
{
    int c=0, i=0;
    while ((c=getchar()) != EOF && c!='\n')
    {
	s[i] = c;
	++i;
    }
    if (c == '\n') {
	s[i] = c;
	s[i+1] = '\0';
    }
	    return i;
}
