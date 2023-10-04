#pragma once
#include <string>
#include "Node.cpp"

template <class T>
class Linkedlist {
private:
	Node<T>* head;
	Node<T>* tail;
	int listSize;

public:
	Linkedlist();
	void pushFront(T);
	void pushBack(T);

	void popFront();
	void popBack();

	bool isEmpty() const;
	int size() const;

	void treaversal() const;

};


//element access
//- front
//- back
//- middle
//
//search and modification
//- contains
//- remove
//- insertAt
//- RemoveFrom
//
//Traversal
//
//Destructor
//
//Reverse