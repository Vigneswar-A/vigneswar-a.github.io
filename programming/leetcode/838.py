class Node{
    int value;
    Node* next;
    Node(int val, Node* nxt = nullptr){
        value = val;
        next = nxt;
    }
    friend class MyLinkedList;
};

class MyLinkedList {
    Node *head;
    Node *tail;
    int count;
    
public:
    MyLinkedList() {
        head = nullptr;
        tail = nullptr;
        count = 0;
    }
    
    int get(int index) {
        if (index >= count){
            return -1;
        }
        Node* currnode = head;
        for(int i = 0; i < index; i++)
            currnode = currnode->next;
        return currnode->value;
    }
    
    void addAtHead(int val) {
        head = new Node(val, head);
        count++;
        if (tail == nullptr)
            tail = head;
    }
    
    void addAtTail(int val) {
        if (head == nullptr){
            addAtHead(val);
            return;
        }
        count++;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    void addAtIndex(int index, int val) {
        
        if (index == 0){
            addAtHead(val);
            return;
        }
        
        if (index == count){
            addAtTail(val);
            return;
        }
        
        else if (index > count)
            return;
        
        Node* currnode = head;
        for(int i = 0; i < index-1; i++)
            currnode = currnode->next;
        currnode->next = new Node(val, currnode->next);
        count++;
    }
    
    void deleteAtIndex(int index) {   
        if (index >= count)
            return;
                
        if (index == 0 && head != nullptr){
            head = head->next;
            count--;
            return;
        }
        Node* currnode = head;
        for(int i = 0; i < index-1; i++)
            currnode = currnode->next;
        
        if (index == count-1)
            tail = currnode;

        currnode->next = currnode->next->next;
        count--;
    }
    
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */