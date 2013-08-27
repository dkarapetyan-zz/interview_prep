#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define N 5


typedef struct pixel
{
    int some_data;
} pixel;



void swap(pixel **array, int i, int j, int l, int m);
void rotate_picture_90(pixel **array, size_t len);
void rotate_rec_90(pixel **array, int i, int j, int len);


int main()
{
    srand(time(NULL));

    pixel **array = malloc(sizeof(pixel *) * N);
    // assign memory for pointers in matrix
    for (int j = 0; j < N; j++)
        array[j] = malloc(sizeof(pixel) * N);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            array[i][j].some_data = rand()%10; 
    }

    // initialize matrix
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d ", array[i][j].some_data);
            if (j == N-1)
                printf("\n");
        }
    }

    /*rotate_rec_90(array, 0, 0, N);*/
    rotate_picture_90(array, N);
    /*swap(array, 0, 1, 1, 0);*/

    printf("\n");

    // print rotated matrix
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d ", array[i][j].some_data);
            if (j == N-1)
                printf("\n");
        }
    }

    // free memory in memory (stored on the heap)

    for (int i = 0; i < N; i++)
    {
        free(array[i]);
    }

    free(array);


    return 0;
}


void rotate_picture_90(pixel **array, size_t len)
{
    int i = 0;
    int k = 0;
    while((int)len > 0)
    {
        rotate_rec_90(array, i+k, i+k, len);
        len-=2;
        k++;
    }



}

void swap(pixel **array, int i, int j, int l, int m)
{
    pixel temp = array[i][j];
    array[i][j] = array[l][m];
    array[l][m] = temp;
}

void rotate_rec_90(pixel **array, int i, int j, int len)
{
    int tlc_row = i;
    int tlc_col = j;
    int trc_row = i;
    int trc_col = j + len - 1;
    int blc_row = i + len - 1;
    int blc_col = j;
    int brc_row = i + len - 1;
    int brc_col = j + len - 1;

    for (int k=1; k < len-1; k++)
        swap(array, tlc_row, tlc_col + k,  trc_row + k, trc_col); // swap top of square with right side, mod corners

    for (int k=1; k < len-1; k++)
        swap(array, tlc_row, tlc_col + k, brc_row, brc_col - k); // inverted swap top of square with bottom, mod corners

    for (int k=1; k < len-1; k++)
        swap(array, tlc_row, tlc_col + k, blc_row - k, blc_col); // inverted swap top of square with left side, mod corners 

    // rotate corners 90 degrees
    swap(array, tlc_row, tlc_col, trc_row, trc_col); // swap top left corner with top right 
    swap(array, tlc_row, tlc_col, brc_row, brc_col); // swap top left with bottom right
    swap(array, tlc_row, tlc_col, blc_row, blc_col); // swap top left with bottlm left

}

