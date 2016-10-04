//check if string2 is a counterclockwise rotation of string1

#include <string>
#include <iostream>

bool is_rotation(std::string string1, std::string string2);


int main()
{
    std::string string1, string2;
    std::cout << "Please input a string.\n";
    std::cin >> string1;

    std::cout << "Input string number two, please.\n";
    std::cin >> string2;

    std::cout <<  is_rotation(string1, string2);

    return 0;
}

bool is_rotation(std::string string1, std::string string2)
{
    bool q = false;

    if (string1.size() == string2.size())
    {
        if ((string2 + string2).find(string1) != static_cast<size_t>(-1)) 
            q = true;

    }

    return q;
}

