// rotate square picture 90 degrees clockwise

#include <iostream>
#include <ctime>
#include <vector>
#include <utility>
const int N=5;

template <class T>
using matrix = std::vector<std::vector <T> >; 

void rotate_picture(matrix<int> &my_matrix);
void rotate_rec(matrix<int> &my_matrix, int i, int j, int len);


int main()
{
    srand(time(nullptr));
    matrix<int> my_matrix(N, std::vector<int> (N));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            my_matrix[i][j] = rand()%10; 
    }

    // print matrix
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            std::cout <<  my_matrix[i][j] << " ";
            if (j == N-1)
                std::cout << "\n";
        }
    }

    rotate_picture(my_matrix);
    std::cout << "\n";

    // print rotated matrix
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            std::cout << my_matrix[i][j] << " ";
            if (j == N-1)
                std::cout << "\n";
        }
    }
    return 0;
}

void rotate_picture(matrix<int> &my_matrix)
{
    int i = 0;
    int k = 0;
    int len = my_matrix[0].size();
    while(len > 0)
    {
        rotate_rec(my_matrix, i+k, i+k, len);
        len-=2;
        k++;
    }
}


void rotate_rec(matrix<int> &my_matrix, int i, int j, int len)
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
        std::swap<int>(my_matrix[tlc_row][tlc_col + k], my_matrix[trc_row + k][trc_col]); // swap top of square with right side, mod corners

    for (int k=1; k < len-1; k++)
        std::swap<int>(my_matrix[tlc_row][tlc_col + k], my_matrix[brc_row][brc_col - k]); // inverted swap top of square with bottom, mod corners

    for (int k=1; k < len-1; k++)
        std::swap<int>(my_matrix[tlc_row][tlc_col + k], my_matrix[blc_row - k][blc_col]); // inverted swap top of square with left side, mod corners 

    // rotate corners 90 degrees
    std::swap<int>(my_matrix[ tlc_row][tlc_col], my_matrix[ trc_row][ trc_col]); // swap top left corner with top right 
    std::swap<int>(my_matrix[ tlc_row][tlc_col], my_matrix[brc_row][brc_col]); // swap top left with bottom right
    std::swap<int>(my_matrix[tlc_row][tlc_col], my_matrix[blc_row][blc_col]); // swap top left with bottlm left
}

