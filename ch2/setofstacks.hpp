#include <iostream>
#include <vector>


class node
{
    private:

        node *next;
        int data;

    public:
        // constructors
        node();
        node(int);
        node(int, node*);

        // accessor and mutator members
        void set_next(node *);
        void set_data(int );

        node *get_next();
        int get_data();



};  



class linkedlist
{
    private:

        size_t current_size;
        node *head;

    public:


        // constructors

        linkedlist();

        // accessor and mutator members
        node *get_head();
        void set_head(node *);
        size_t size();

        // destructor
        ~linkedlist();


        // other members

        node pop();
        void push(int);


};

class setofstacks
{
    private:

        std::vector<linkedlist> vec_of_stacks;
        size_t head;
        static size_t max_size;

    public:

        node pop();
        void push(int);


};

node::node(int data)
{
    this->data = data;
}
node::node(int data, node* next)
{
    this->data = data;
    this->next = next;
}

int node::get_data()
{
    return this->data;
}

node *node::get_next()
{
    return this->next;
}

void node::set_data(int data)
{
    this->data = data;
}

void node::set_next(node *next)
{
    this->next = next;
}


linkedlist::linkedlist()
{
    this->current_size = 0;
}
linkedlist::~linkedlist()
{
    for (auto p = head; p != nullptr; p=p->get_next())
    {
        delete p;    
    }
    delete this;
}

node* linkedlist::get_head()
{
    return this->head;
}

node linkedlist::pop()
{
    node *temp = this->head;
    this->head = this->head->get_next();
    this->current_size-=1;
    return *temp;
}

void linkedlist::push(int data)
{
    node *new_node = new node(data, head); 
    this->head = new_node;
    this->current_size+=1;
}

void linkedlist::set_head(node *head)
{
    this->head = head;
}
size_t linkedlist::size()
{
    return this->current_size;
}

size_t setofstacks::max_size = 3;

void setofstacks::push(int data)
{
    if (setofstacks::vec_of_stacks[head].size() > setofstacks::max_size)
    {
        linkedlist *new_list = new linkedlist();
        new_list->push(data);

        setofstacks::vec_of_stacks.push_back(*new_list);
        ++head;
    }

    else
    {
        setofstacks::vec_of_stacks[head].push(data);
    }
}

