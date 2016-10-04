#include <stdio.h>

/*Converting Celcius to Fahrenheit*/

    void fahrCelcius();

    int main() {
	fahrCelcius();
	return 0;
    }

void fahrCelcius()
{
    printf("\n%s %s \n \n", "Celcius ", "Fahrenheit");
    for (int i = 0; i <= 100; i= i+20) {
	printf("%d \t %f \n", i, 9.0/5.0* i +32  );  
    }
}

