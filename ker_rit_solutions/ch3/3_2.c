#include <stdio.h>

void escape( char s[], char t[]);
void revescape(char s[], char t[]);
char string1[6]={'c', 'a', 't', '\t', '\n', '\0'};
char string1Trans[12];

char string2[10]={'c', 'a', 't', '\\', 't', 'm', '\\', 'n', 'q', '\0'};
char string2Trans[16];

int main()
{
  escape(string1Trans, string1);

  revescape(string2Trans, string2);

  printf("%s\n", string1Trans);
  printf("%s", string2Trans);

  return 0;
}

void escape( char s[], char t[])
{
  int j=0;

  for (int i=0; t[i] != '\0'; i++) {
    switch ( t[i] ) {

      case '\t':
	s[j] = '\\';
	s[j+1] = 't';
	j +=2;
	break;

      case '\n':
	s[j] = '\\';
	s[j+1] = 'n';
	j+=2;
	break;


      default:
	s[j]=t[i];
	j++;
	break;
    }
  }
}


void revescape( char s[], char t[])
{
  int j=0;
  for (int i = 0; t[i] != '\0'; ++i) {
    if (t[i] == '\\') {
      switch ( t[i+1] ) {

	case 't':
	  s[j] = '\t';
	  j++;
	  i++;
	  break;

	case 'n':
	  s[j] = '\n';
	  j++;
	  i++;
	  break;

	default:
	  s[j] = t[i];
	  s[j+1] = t[i+1];
	  j +=2;
	  break;
      }
    }
    else {
      s[j]=t[i];
      j++;
    }


  }


}




