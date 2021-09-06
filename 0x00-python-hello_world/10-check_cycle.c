#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: pointer to start of linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *previous = list;

	while (current && current->next)
	{
		previous = previous->next;
		current = current->next->next;
		if (current == previous)
			return (1);
	}

	return (0);
}
