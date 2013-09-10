// add numbers in two linked lists--express new number as a linked list
//
#include <iostream>
#include <list>
using std::list;
using std::cout;

list<int> add_linked_list(list<int> const &list1, list<int> const &list2);


int main()
{
    list<int> list1 = {7,8};
    list<int> list2 = {1,2,2};

    auto total_list = add_linked_list(list1, list2);
    for (auto i = total_list.cbegin(); i!= total_list.cend(); i++)
        cout << *i << " ";


    return 0;
}



list<int> add_linked_list(list<int> const &list1, list<int> const &list2)
{
    auto num1 = 0, num2 = 0;
    for (auto i = list1.rbegin(), j = list2.rbegin(); i!=list1.rend() || j!=list2.rend(); )
    {

        if (i != list1.rend())
        {
            num1 = (num1 * 10 + *i);
            i++;
        }
        if (j != list2.rend())
        {
            num2 = (num2 * 10 + *j);
            j++;
        }
    }

    auto total = num1 + num2;

    list<int> total_list;
    for (; total !=0; total/=10)
    {
        total_list.push_front(total%10);

    }
    return total_list;

}
