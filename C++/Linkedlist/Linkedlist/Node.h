#pragma once

template <class T>
class Node {
private:
    T data;
    Node<T>* next;

public:
    Node(T d);
    T getData() const;
    Node<T>* getNext() const;
    void setData(T data);
    void setNext(Node<T>* next);
};
