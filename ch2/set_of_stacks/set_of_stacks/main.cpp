#include "setofstacks.hpp"
int main()
{
    setofstacks my_stacks;
    my_stacks.push(5);
    my_stacks.push(4);
    my_stacks.push(3);
    my_stacks.push(2);
    std::cout << my_stacks.get_stacks()[0].get_head()->get_data();
    std::cout << my_stacks.get_stacks()[1].get_head()->get_data();
    std::cout << my_stacks.size();

    return 0;
}
