#include "Linkedlist.cpp"

int main() {
	Linkedlist<int> list;

	list.pushFront(1);
	list.pushFront(2);
	list.pushFront(3);
	list.pushBack(4);
	list.pushBack(5);
	list.pushBack(6);
	list.pushBack(7);
	list.pushBack(8);

	list.getHead();
	list.getTail();
	list.getMedian();

	list.treaversal();

	list.popFront();

	list.treaversal();

	list.popBack();

	list.treaversal();

	return 0;
}