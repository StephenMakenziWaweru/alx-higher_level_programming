#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to start of linked list.
 * 
 * Return: 0 if not a palindrome, else return 1.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *node, *prev;
	int failed = 0;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	node = slow;
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	fast = *head;
	node = prev;
	while (prev)
	{
		if (fast->n != prev->n)
		{
			failed = 1;
			break;
		}
		fast = fast->next;
		prev = prev->next;
	}
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	return (!failed);
}
