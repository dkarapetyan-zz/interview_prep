#include <stdio.h>

#ifndef out
#define out 1
#endif
#ifndef in
#define in 0
#endif


int main()
{
  int lword =0;
  int hist[20];
  int c;
  int state=in;

  for (int i = 0; i < 20; ++i) {

    hist[i]=0;
  }

  while ((c=getchar()) != EOF) {
    switch ( c ) {

      case ' ':
	state=out;
	break;

      case '\n':
	state=out;
	break;

      case '\t':
	state=out;
	break;

      default:
	++lword;
	state=in;
	break;
    }
   if (state==out) {
   
     ++hist[lword];
     lword=0;
   }
   

  }

/*for (int i = 0; i < 20; ++i) {*/

  /*printf("%d ", hist[i]);*/
/*}*/
  
    for (int i = 0; i < 20; ++i) {
if (hist[i]!=0) {
      printf("%d ", i);
  for (int j = 0; j < hist[i]; ++j) {
 printf("*"); 
  }
 printf("\n"); 
}
  else {
    printf("%d\n", i);
  }
}

printf("%c", 33 );
  return 0;
}
