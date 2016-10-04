#include <stdio.h>
void squeezeMy(char s1[], char s2[]);

char string1[5]={'c', 'a', 't', 'l','\0'};
char string2[4]={'b', 'a', 'n', '\0'};

int main()
{
  squeezeMy(string1, string2);
  printf("%s", string1);
  return 0;
}



void squeezeMy(char s1[], char s2[]) {
  int i=0;
  int j=0;
  int k=0;

  while (s1[k] != '\0') {

    for (j = 0; s2[j] != '\0' && s1[k] != s2[j] ; j++) {

    }


    (s2[j] == '\0')  ?  s1[i++] = s1[k++] : k++;

  }

  s1[i] = '\0';
}



