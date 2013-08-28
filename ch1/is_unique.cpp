// check to see if string has all unique characters

#include <iostream>
#include <string>
#include <unordered_map>

bool is_unique(std::string my_string);

int main()
{
    std::string my_string;
    std::cout << "Please enter a string.\n";
    std::cin >> my_string;
    std::cout << is_unique(my_string);
    return 0;
}


bool is_unique(std::string my_string)    
{
    std::unordered_multimap<char, int> my_table;
    for (size_t i = 0, j = my_string.size(); i< j; i++)
    {
        my_table.insert(std::pair<char, int>(my_string[i],0));

        if (my_table.count(my_string[i]) > 1)
        {
            return false;
        }

    }

    return true;
}
