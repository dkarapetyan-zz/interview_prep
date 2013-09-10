// delete node in middle of linked list
#include <cstdlib>
void del_mid_node(linkedlist *my_list, node *my_node)
{
    // if linked list is only one element

    if (my_node->next == nullptr)
    {
        free(my_node);
        free(my_list);
    }
    else
    {

        node *prev_node;
        for (prev_node = my_list->head; prev_node->next !=my_node ; prev_node = prev_node->next){}

        node *temp = prev_node->next;
        prev_node->next = prev_node->next->next;
        free temp;
    }
}
