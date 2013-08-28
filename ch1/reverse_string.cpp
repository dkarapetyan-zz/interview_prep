// reverse string in place

#include <iostream>
#include <utility>
#include <string>

void reverse(std::string &my_string);

int main()
{
    std::string my_string;
    std::cout << "Input a my_string. \n";
    std::getline(std::cin, my_string);
    reverse(my_string);
    std::cout << my_string;
    return 0;
}


void reverse(std::string &my_string)
{
    for (size_t i = 0, len = my_string.size(); i < len/2; i++)
        std::swap(my_string[i], my_string[len-i-1]);
}

