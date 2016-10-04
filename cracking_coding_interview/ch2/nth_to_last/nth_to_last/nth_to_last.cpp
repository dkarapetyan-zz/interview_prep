#include <iostream>
#include <forward_list>
#include <iterator>

using std::forward_list;
using std::cout;
using std::distance;


template <class T>
typename forward_list<T>::const_iterator nth_to_last(forward_list<T> const &my_list, long n);

int main()
{
    forward_list<int> my_list = {5,3,6,8};
    forward_list<std::string> my_list2 = {"hello","goodbye","dinner"};

    cout << *nth_to_last<int>(my_list, 4) << " \n";
    cout << *nth_to_last<std::string>(my_list2, 1) << " \n";

    return 0;
}

    template <class T>
typename forward_list<T>::const_iterator nth_to_last(forward_list<T> const &my_list, long n)
{
    if (my_list.empty() == true || n <=0 || n > distance(my_list.begin(), my_list.end()))
    {
        return my_list.cend();
    }
    else if (n == 1)
    {
        return my_list.cbegin();
    }
    else
    {
        return ++nth_to_last(my_list, n-1);
    }
}
