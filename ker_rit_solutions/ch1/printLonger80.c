#include <stdio.h>
#define MAXLINE 1000 /* maximum input line length */
int getlineMy(char *);
/* print the longest input line */
int main()
{
    int len=0;
    char line[MAXLINE];
    /* current line length */
    /* maximum length seen so far */
    /* current input line */
    while ((len = getlineMy(line)) >= 0)
	if (len > 20) 
	printf("%s%s %d \n", line, "length =",len);
    return 0; 
}
    /* getlineMy:  read a line into s, return length  */
int getlineMy(char *s)
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
