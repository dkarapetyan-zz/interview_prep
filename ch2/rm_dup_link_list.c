/*remove duplicate entries from singly linked list*/
#include <glib.h>
#include <stdio.h>
#include <stdbool.h>




void rm_dup(GSList *head)
{
    void *my_table = g_hash_table_new(NULL, NULL);
    for (GSList *p = head; p; p = p->next)
    {
        if (g_hash_table_lookup_extended(my_table, p->data, NULL, NULL) == false)
        {
            g_hash_table_insert(my_table, p->data, NULL);
        }

        else
            head = g_slist_delete_link(head, p);


    }

    g_hash_table_remove_all(my_table);
}

int main()
{
    GSList *my_list = NULL;
    my_list = g_slist_insert(my_list, GINT_TO_POINTER(5), 0);
    my_list = g_slist_insert(my_list, GINT_TO_POINTER(9), 0);
    my_list = g_slist_insert(my_list, GINT_TO_POINTER(5), 0);

    rm_dup(my_list);
    for (GSList *p = my_list; p; p = p->next)
    {
        printf("%d ", GPOINTER_TO_INT(p->data));    
    }

    return 0;
}
