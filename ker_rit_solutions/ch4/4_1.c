#include <stdio.h>
#include <string.h>

#define MAXLINE 1000

int strindex(char s[], char t[]);
int strindexright(char s[], char t[]);


int main()
{
char string1[MAXLINE] = {'b', 'o', 'b', 'o', '\0'};
char string2[MAXLINE] = {'b', 'o', 'b', 'o', 'b', 'o', 'b', 'o', '\0'};
printf("%d", strindexright(string2, string1));
  return 0;
}


/* strindex:  return index of t in s, -1 if none */
   int strindexright(char s[], char t[])
   {
int i=0;
int  j=0;
int k=0;
for (i = strlen(s)-1; i != -1; i--) {
for (j=i, k=0; t[k]!='\0' && s[j]==t[k]; j++, k++)
               ;
           if (k > 0 && t[k] == '\0')
return i;
}
return -1; 
}




/* strindex:  return index of t in s, -1 if none */
   int strindex(char s[], char t[])
   {
int i, j, k;
for (i = 0; s[i] != '\0'; i++) {
for (j=i, k=0; t[k]!='\0' && s[j]==t[k]; j++, k++)
               ;
           if (k > 0 && t[k] == '\0')
return i;
}
return -1; }
