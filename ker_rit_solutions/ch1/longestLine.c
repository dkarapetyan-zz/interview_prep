#include <stdio.h>
#define MAXLINE 1000 /* maximum input line length */
int getlineMy(char *);
void copy(char *, char *);
/* print the longest input line */
int main()
{
    int len=0;
    int max=0;
    char line[MAXLINE];
    char longest[MAXLINE]; /* longest line saved here */
    /* current line length */
    /* maximum length seen so far */
    /* current input line */
    while ((len = getlineMy(line)) > 0)
	if (len > max) {
	    max = len;
	    copy(longest, line);
	}
    if (max > 0) /*there was a line*/ 
	printf("%s%s %d", longest, "length =",max);
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
/* copy: copy 'from' into 'to'; assume to is big enough */
void copy(char *to, char *from)
{
    int i=0;
    while ((to[i] = from[i]) != '\0')
	if (i==(MAXLINE-1))
	    break;
	    else
	++i; 
}
