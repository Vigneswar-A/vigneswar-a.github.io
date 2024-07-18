class MyCircularQueue {
    int *array;
    int front;
    int count;
    int limit;
    
public:
    MyCircularQueue(int k) {
        array = new int[k];
        count = 0;
        limit = k;
        front = 0;
    }
    
    bool enQueue(int value) {
        if(isFull())
            return false;
        array[(front+count)%limit] = value;
        count++;  
        return true;
    }
    
    bool deQueue() {
        if(count == 0)
            return false;
        count--;
        front = (front+1)%limit;
        return true;
    }
    
    int Front() {
        if (isEmpty())
            return -1;
        return array[front];
    }
    
    int Rear() {
        if (isEmpty())
            return -1;
        return array[(front+count-1)%limit];
    }
    
    bool isEmpty() {
        return count == 0;
    }
    
    bool isFull() {
        return count == limit;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */