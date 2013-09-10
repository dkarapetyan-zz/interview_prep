#include <iostream>
#include <forward_list>

void del_mid(std::forward_list<int> my_list, std::forward_list<int>::iterator my_it);






int main()
{
    std::forward_list<int> my_list = {1,5,8,9};
    del_mid(my_list, ++my_list.begin());
    for (auto i = my_list.cbegin(); i != my_list.cend(); ++i)
    {
        std::cout << *i << " ";
    }
    
    return 0;
}


void del_mid(std::forward_list<int> &my_list, std::forward_list<int>::iterator &my_it)
{
    std::forward_list<int>::iterator prev_it;

    for (auto i = my_list.begin(); ; ++i)
    {
        if (std::next(i) == my_it)
        {
            prev_it = i;
            break;
        }
        prev_it.
        
    }
        

}

