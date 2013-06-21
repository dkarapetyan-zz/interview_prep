// program to turn tabs into spaces

#include <stdio.h>
#define MAXLINE 1000
#define TABSTOP 8

int getlineMy(char []);
void detab(char []);

char line[MAXLINE];
int length;
int i=0;
int main()
{
    while ((length=getlineMy(line)) > 2) {
	for (int i = 0; i < MAXLINE; ++i) {

	    if (line[i] != '\n' && line[i] != '\0') {
		int mod=(i % TABSTOP);
		if (line[i] == '\t') {
		    switch ( mod ) {

			case 0:

			    break;

			case 1:

			    line[i] = ' ';

			    break;

			case 2:

			    {
				while (i != (length +3)) {
				    char temp1=line[i];
				    char temp2=line[i+1];
				    line[i +2] = temp1;
				    line[i+3]= temp2; 
				}
				line[i] = ' ';
				line[i+1] = ' ';
			    }

			case 3:

			    {
				int j = i+3;
				char temp;
				while (j != (length +3)) {
				    line[j +1] = temp;
				    line[j+1]= line[j];
				    line[j+2]=temp;	      
				}
				char temp1 = line[i+1];
				char temp2 = line[i+2];
				char temp3 = line[i+3];
				line[i] = ' ';
				line[i+1] = ' ';
				line[i+2] = ' ';
				line[i+3] = temp1;
				line[i+4] = temp2;
				line[i+5] = temp3;
			    }


			default:
			    break;
		    } 
		}


	    }


	}
printf("%s", line);

    }
    
    return 0;
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
    return i+2;
}
