// decide if two strings are anagrams or not
// by comparing hash tables for each string

#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>

bool is_anagram(std::string string1, std::string string2);

int main()
{

    std::string string1, string2;
    std::cout << "Enter a string \n";
    std::cin >> string1;
    std::cout << "Enter another string \n";
    std::cin >> string2;
    std::cout << is_anagram(string1, string2);

    return 0;
}

bool is_anagram(std::string string1, std::string string2)
{
    std::unordered_multimap<char, int> table1;
    auto table2 = table1;
    auto len1 = string1.size();
    auto len2 = string2.size();

    if (len1 != len2)
    {
        return false;
    }

    else
    {
        for (size_t i =0; i < len1; i++)
        {
            table1.insert(std::pair<char, size_t>(string1[i], 0));
            table2.insert(std::pair<char, size_t>(string2[i], 0));
        }
    }

    return (table1 == table2);
}

