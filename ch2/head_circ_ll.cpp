// return head of corrupted circular linked list
// two functions
#include <unordered_map>
using std::unordered_map;

node * return_head(list const &my_list)
{

    unordered_map<int> my_map;
    for (auto i = my_list.gethead(); i < my_list.size; ++i)
    {
        my_map.insert(std::pair<node *, int>(i, 0))
            if (my_map.count(i) > 1)
            {
                return i;
            }


    }
}



