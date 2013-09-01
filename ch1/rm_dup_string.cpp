//remove duplicate characters in a string

#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
using std::string;
using std::cin;
using std::cout;
using std::getline;
using std::pair;


void rm_dup(string &my_string);



int main()
{
    string my_string;
    cout << "Please enter a my_string \n";
    getline(cin, my_string);
    rm_dup(my_string);
    cout << my_string;
    return 0;
}


void rm_dup(string &my_string)
{
    std::unordered_multimap<char, size_t> my_table;
    size_t last = 0; 
    size_t len = my_string.size();

    for (size_t i = 0; i < len; i++)
    {
        my_table.insert(std::pair<char, size_t>(my_string[i],0));
        if (my_table.count(my_string[i]) == 1)
        {
            my_string[last++] = my_string[i];
        }
    }
    my_string.erase(last, len -1);
} 
