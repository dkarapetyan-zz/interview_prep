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
    std::string &&new_string = ""; // use rvalue move semantics

    for (size_t i = 0; i < my_string.size(); i++)
    {
        if (my_string[i] == ' ')
        {
            new_string+="%20";
        }
        else
        {
            new_string+=my_string[i];
        }
    }
// new_string moved, not copied, to my_string
// due to rvalue move semantics above
    my_string = new_string; 
}

