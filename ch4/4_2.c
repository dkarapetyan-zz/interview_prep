#include <stdio.h>
#include <ctype.h>
#ifndef MAXLINE
#define MAXLINE 1000
#endif

/* atof:  convert string s to double */
double atof(char s[])
{
  double val, power, expo=1; 
  int exposign=1, i, sign;

  for (i = 0; isspace(s[i]); i++) /* skip white space */ ;
  sign = (s[i] == '-') ? -1 : 1;
  if (s[i] == '+' || s[i] == '-')
    i++;
  for (val = 0.0; isdigit(s[i]); i++)
    val = 10.0 * val + (s[i] - '0');
  if (s[i] == '.')
    i++;
  for (power = 1.0; isdigit(s[i]); i++) {
    val = 10.0 * val + (s[i] - '0');
    power *= 10; 
  }
  for (; s[i] == 'e' || s[i] == 'E' || s[i] == '-'; ++i) {
    if (s[i] == '-') {
      exposign=-1;
    }
  }
  // now i gives us the exponent value
  if (exposign < 0) {
    for (int j=0; j < s[i]-'0'; ++j) {
      expo /= 10;
    }
  }
  else {
    for (int j=0; j < s[i] - '0'; ++j) {
      expo *= 10;
    }
  }


  return (sign * val / power) * expo;
}

int main()
{
  char string1[MAXLINE] = {'1', '2', '3', '.', '4', '5', 'e', '-', '6', '\0'};
  printf("%f\n", atof(string1));
  return 0;
}
