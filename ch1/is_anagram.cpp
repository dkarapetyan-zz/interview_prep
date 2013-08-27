// decide if two strings are anagrams or not
// by comparing hash tables for each string

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <array>
const int SIZE = 1000;

bool is_anagram(std::string string1, std::string string2);

int main()
{
    std::string string1; 
    std::string string2;
    std::cout << "Enter a string \n";
    std::cin >> string1;
    std::cout << "Enter another string \n";
    std::cin >> string2;
    auto i = is_anagram(string1, string2);

    std::cout << i; 

    return 0;
}

bool is_anagram(std::string string1, std::string string2)
{
    std::array<int,SIZE> da_array1; 
    std::array<int,SIZE> da_array2;
    da_array1.fill(0);
    da_array2 = da_array1;
    auto len1 = string1.size();
    auto len2 = string2.size();

    if (len1 != len2)
    {
        return false;
    }

    else 
    {
        for (size_t i = 0; i < len1; i++)
        {
            da_array1[(int)string1[i]]+=1;
            da_array2[(int)string2[i]]+=1;
        }

    }

    return (da_array1 == da_array2);
}

