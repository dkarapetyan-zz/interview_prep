#include <stdio.h>


int main()
{
    int hist[128];
    int c;

    for (int i = 0; i < 128; ++i) {

	hist[i]=0;
    }

    while ((c=getchar()) != EOF) {
	++hist[c];
    }




    for (int i = 0; i < 128; ++i) {
	if (hist[i]!=0) {
	    printf("%c ", i);
	    for (int j = 0; j < hist[i]; ++j) {
		printf("*"); 
	    }
	    printf("\n"); 
	}
	else {
	    printf("%c\n", i);
	}
    }

}
