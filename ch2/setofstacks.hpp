#include <iostream>
#include <vector>
#include <memory>
#include <utility>
using std::unique_ptr;
using std::vector;

class node
{
    private:

        unique_ptr<node> next;
        int data;

    public:
        // constructors
        node();
        node(int);
        node(int, unique_ptr<node>&);


        // accessor and mutator members
        void set_next(unique_ptr<node>&);
        void set_data(int );

        unique_ptr<node> &get_next();
        int get_data() const;



};  



class linkedlist
{
    private:

        size_t current_size;
        unique_ptr<node> head;

    public:


        // constructors

        linkedlist();
        linkedlist(int);



        // accessor and mutator members
        unique_ptr<node> &get_head();
        void set_head(unique_ptr<node>& );
        size_t size();



        // other members

        node pop();
        void push(int);


};

class setofstacks
{
    private:

        vector<linkedlist> vec_of_stacks;
        size_t head;
        static size_t max_size;
        size_t current_size;

    public:
        //constructors and deconstructors

        setofstacks();

        //accessors and mutators
        node pop();
        void push(int);
        size_t size();
        vector<linkedlist>  &get_stacks();


};

node::node(int _data)
{
    data = _data;
    next = nullptr;
}
node::node(int _data, unique_ptr<node> &_next)
{
    data = _data;
    next = std::move(_next);
}

int node::get_data() const
{
    return data;
}

unique_ptr<node> &node::get_next() 
{
    return next;
}

void node::set_data(int _data)
{
    data = _data;
}

void node::set_next(unique_ptr<node> &_next)
{
    next = std::move(_next);
}


linkedlist::linkedlist()
{
    head = nullptr;
    current_size = 0;
}

linkedlist::linkedlist(int data)
{
    unique_ptr<node> new_node(new node(data));
    head = std::move(new_node);
    current_size=1;
}



unique_ptr<node> &linkedlist::get_head()
{
    return head;
}

node linkedlist::pop()
{
    unique_ptr<node> temp = std::move(head);
    head = std::move(head->get_next());
    current_size-=1;
    return std::move(*temp);
}

void linkedlist::push(int data)
{
    unique_ptr<node> new_node(new node(data, head)); 
    head = std::move(new_node);
    current_size+=1;
}

void linkedlist::set_head(unique_ptr<node> &new_head)
{
    head = std::move(new_head);
}
size_t linkedlist::size()
{
    return current_size;
}

size_t setofstacks::max_size = 3;

setofstacks::setofstacks()
{
    current_size = 0;
    head = 0; 
}

size_t setofstacks::size()
{
    return current_size;
}
void setofstacks::push(int data)
{
    linkedlist my_list(data);

    if (vec_of_stacks.size() ==0)
    {
        vec_of_stacks.push_back(std::move(my_list));
        ++current_size;
    }

    else if (vec_of_stacks[head].size() >= max_size)
    {
        vec_of_stacks.push_back(std::move(my_list));
        ++head;
        ++current_size;
    }
    else
    {
        vec_of_stacks[head].push(data);
    }

}

node setofstacks::pop()
{
    if (vec_of_stacks[head].size() == 0)
    {
        if (head !=0)
        {
            --head;
        }
        if (current_size !=0)
        {
            --current_size;
        }
        return vec_of_stacks[head].pop();
    }

    else
    {
        return vec_of_stacks[head].pop();
    }
}

vector<linkedlist> &setofstacks::get_stacks() 
{
    return vec_of_stacks;
}


