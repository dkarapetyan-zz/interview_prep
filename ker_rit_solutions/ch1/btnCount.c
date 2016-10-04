#include <stdio.h>
int main()
{
  int c=0, blank=0, tab=0, nl=0;
while ((c = getchar()) !=EOF) {
  if (c == '\n')
    ++nl;
    else if (c == '\t')
      ++tab;
  else if (c ==' ')
    ++blank;

}
  printf("%s %s %s \n%d %d %d \n", "blank", "tab", "nl", blank, tab, nl);

  return 0;
}
