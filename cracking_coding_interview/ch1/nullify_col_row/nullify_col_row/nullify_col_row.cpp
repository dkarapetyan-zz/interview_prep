// if [i,j] in matrix is 0, zero out ith row and jth column

#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
const size_t ROWS=3;
const size_t COLUMNS=5;

typedef std::vector<std::vector<int> > matrix;


void nullptrify_matrix(matrix &my_array);
void nullptrify_row(matrix &my_array, size_t i);
void nullptrify_column(matrix &my_array, size_t j);

int main()
{
    std::srand(std::time(nullptr));

    matrix my_array; 

    // initialize and print matrix
    for (size_t i = 0; i < ROWS; i++)
    {
        my_array.push_back(std::vector<int>());
        for (size_t j = 0; j < COLUMNS; j++)
        {
            my_array[i].push_back(rand()%10); 
            std::cout << my_array[i][j] << " ";

            if (j == COLUMNS-1)
            {
                std::cout << "\n";
            }

        }
    }


    nullptrify_matrix(my_array);

    std::cout << "\n";

    // print nullptrified matrix
    for (size_t i = 0; i < ROWS; i++)
    {
        for (size_t j = 0; j < COLUMNS; j++)
        {
            std::cout << my_array[i][j] << " ";
            if (j == COLUMNS-1)
                std::cout << "\n";
        }
    }

    return 0;
}





void nullptrify_matrix(matrix &my_array)
{
    size_t rows = my_array.size();
    size_t cols = my_array[0].size();
    std::vector<std::pair<int, int> > zero_array(cols);
    size_t k = 0;
    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < cols; j++)
        {
            if (my_array[i][j] == 0)
            {
                zero_array[k].first = i;
                zero_array[k++].second = j;
            }
        }
    }

    for (size_t i = 0; i < k; i++)
    {
        nullptrify_row(my_array, zero_array[i].first);
        nullptrify_column(my_array, zero_array[i].second);
    }
}



void nullptrify_row(matrix &my_array, size_t i)
{
    if (i > my_array.size() -1)
    {
        std::cout << "Row index chosen is greater than number of rows in matrix.";
    }
    else
    {
        for (size_t j = 0, length = my_array[0].size(); j < length; j++)
            my_array[i][j] = 0;
    }
}

void nullptrify_column(matrix &my_array, size_t j)
{
    if (j > my_array[0].size() -1)
    {
        std::cout << "Column index chosen is greater than number of columns in matrix.";
    }
    else
    {
        for (size_t i = 0, height = my_array.size(); i < height; i++)
            my_array[i][j] = 0;
    }
}

