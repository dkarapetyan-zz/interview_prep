// Return first location in string1 with character occurring in string2

#include <stdio.h>
int any(char s1[], char s2[]);

char string1[5]={'c', 'b', 't', 'l','\0'};
char string2[4]={'t', 'a', 'n', '\0'};

int main()
{
  int k=any(string1, string2);
  printf("%d", k);
  return 0;
}



int any(char s1[], char s2[]) {
  int i=0;
  int j=0;

  while (s1[i] != '\0') {

    for (j = 0; s2[j] != '\0' && s1[i] != s2[j] ; j++) {

    }

    if (s2[j] == '\0')  
    {
      i++; 
    }
    else {
      return i;
      break;
    }

  }

 return -1;
}



