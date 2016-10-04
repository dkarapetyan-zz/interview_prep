/*remove duplicate entries from singly linked list*/
#include <unordered_map>
#include <iostream>
#include <list>

    template <typename T>
void rm_dup(std::list<T> &my_list)
{
    std::unordered_map<T, int> my_table;
    for (auto p = my_list.cbegin(); p !=my_list.cend(); p++)
    {
        if (my_table.find(*p) == my_table.cend())
        {
            my_table.insert(std::pair<T, int>(*p, 0));
        }

        else
        {
            my_list.erase(p);
        }
    }
}

int main()
{
    std::list<int> my_list;
    std::list<std::string> my_list2;
    my_list.push_back(5);
    my_list.push_back(9);
    my_list.push_back(5);
    my_list2.push_back("hello");
    my_list2.push_back("goodbye");
    my_list2.push_back("hello");

    rm_dup(my_list);
    rm_dup(my_list2);

    for (auto p = my_list.cbegin(); p!=my_list.cend(); p++)
    {
        std::cout << *p << " ";
    }

    for (auto p = my_list2.cbegin(); p!=my_list2.cend(); p++)
    {
        std::cout << *p << " ";
    }
    return 0;
}
