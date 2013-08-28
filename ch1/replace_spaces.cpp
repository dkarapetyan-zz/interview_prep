// replace spaces in string with '%20'

#include <iostream>
#include <string>


void replace_spaces(std::string &my_string); 


int main()
{
    std::string my_string;
    std::cout << "Please enter a my_string.\n";
    std::getline(std::cin,my_string);

    replace_spaces(my_string);
    std::cout << my_string;

    return 0;
}


void replace_spaces(std::string &my_string)
{
    std::string new_my_string;

    for (size_t i = 0; i < my_string.size(); i++)
    {
        if (my_string[i] == ' ')
        {
            new_my_string+="%20";
        }
        else
        {
            new_my_string+=my_string[i];
        }
    }
    my_string = new_my_string;
}

