// if [i,j] in matrix is 0, zero out ith row and jth column

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define ROWS  3
#define COLUMNS 9

typedef struct indices
{
    size_t row;
    size_t column;
} indices;


void nullify_matrix(int **array, size_t rows, size_t cols);
void nullify_row(int **array, size_t i, size_t length);
void nullify_column(int **array, size_t j, size_t height);

int main()
{
    srand(time(NULL));

    int **array = malloc(sizeof(int *) * ROWS);
    // assign memory for pointers in matrix
    for (size_t i = 0; i < ROWS; i++)
        array[i] = malloc(sizeof(int) * COLUMNS);

    // initialize and print matrix
    for (size_t i = 0; i < ROWS; i++)
    {
        for (size_t j = 0; j < COLUMNS; j++)
        {
            array[i][j] = rand()%10; 
            printf("%d ", array[i][j]);

            if (j == COLUMNS-1)
                printf("\n");

        }
    }


    nullify_matrix(array, ROWS, COLUMNS);

    printf("\n");

    // print nullified matrix
    for (size_t i = 0; i < ROWS; i++)
    {
        for (size_t j = 0; j < COLUMNS; j++)
        {
            printf("%d ", array[i][j]);
            if (j == COLUMNS-1)
                printf("\n");
        }
    }

    // free memory in memory (stored on the heap)

    for (size_t i = 0; i < ROWS; i++)
        free(array[i]);

    free(array);


    return 0;
}





void nullify_matrix(int **array, size_t rows, size_t cols)
{
    indices *zero_array = malloc(sizeof(indices) * cols);
    size_t k = 0;
    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < cols; j++)
        {
            if (array[i][j] == 0)
            {
                zero_array[k].row = i;
                zero_array[k++].column = j;
            }

        }

    }

    for (size_t i = 0; i < k; i++)
    {
        nullify_row(array, zero_array[i].row, cols);
        nullify_column(array, zero_array[i].column, rows);
    }
    free(zero_array);
}



void nullify_row(int **array, size_t i, size_t length)
{
    for (size_t j = 0; j < length; j++)
        array[i][j] = 0;
}

void nullify_column(int **array, size_t j, size_t height)
{
    for (size_t i = 0; i < height; i++)
        array[i][j] = 0;
}

