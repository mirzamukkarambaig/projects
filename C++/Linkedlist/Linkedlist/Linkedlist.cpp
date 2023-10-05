#include <iostream>
#include "Linkedlist.h"

template <class T>
Linkedlist<T>::Linkedlist() : head(nullptr), tail(nullptr), listSize(0) {}

template <class T>
void Linkedlist<T>::pushFront(T data) {
    Node<T>* temp = new Node<T>(data);

    if (this->isEmpty()) {
        head = tail = temp;
    }
    else {
        temp->setNext(head);
        head = temp;
    }
    listSize++;
}

template <class T>
void Linkedlist<T>::pushBack(T data) {
    Node<T>* temp = new Node<T>(data);

    if (this->isEmpty()) {
        head = tail = temp;
    }
    else {
        tail->setNext(temp);
        tail = temp;
    }
    listSize++;
}

template <class T>
bool Linkedlist<T>::isEmpty() const{
    return head == nullptr;
}

template <class T>
void Linkedlist<T>::popFront() {
    if (isEmpty()) {
        std::cout << "List is empty! \n";
    }

    Node<T>* temp = head;      
    head = head->getNext();

    if (head == nullptr) {     
        tail = nullptr;        
    }
    listSize--;
    delete temp;               

    std::cout << "First element removed! \n";
}

template <class T>
void Linkedlist<T>::popBack() {
    if (isEmpty()) {
        std::cout << "List is empty! \n";
    }

    if (head == tail) {
        delete head;
        head = tail = nullptr;
    }
    else {
        Node<T>* temp = head;
        while (temp->getNext()->getNext() != nullptr) {
            temp = temp->getNext();
        }
        delete temp->getNext();
        temp->setNext(nullptr);
        tail = temp;             
    }
    listSize--;
    std::cout << "Last element removed! \n";
}


template <class T>
int Linkedlist<T>::size() const {
    return this->listSize;
}

template <class T>
void Linkedlist<T>::treaversal() const {
    Node<T>* temp = head;
    int index = 1;

    while (temp != nullptr) {
        
        std::cout << "Index: " << index << ", data: " << temp->getData() << std::endl;

        index++;
        temp = temp->getNext();
    }

    std::cout << "List Size: " << this->listSize << std::endl;
}

template<class T>
void Linkedlist<T>::getHead() const
{
    std::cout << "Head: " << this->head->getData() << std::endl;
}

template<class T>
void Linkedlist<T>::getTail() const
{
    std::cout << "Tail: " << this->tail->getData() << std::endl;
}

template<class T>
void Linkedlist<T>::getMedian() const
{
    Node<T>* temp = head;
    for (int i = 0; i < (listSize / 2); i++) {
        temp = temp->getNext();
    }

    std::cout << "Median: " << temp->getData() << std::endl;
}
