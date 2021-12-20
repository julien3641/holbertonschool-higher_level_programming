#include "lists.h"

/**
 * check_cycle - check if there is a cycle
 * the node1 is going on 1 step by 1 step
 * as the second one is going on 2 steps by 2 steps
 * and so if both are equal the program stop because there is a cycle
 * @list: list
 * Return: 0 on failure and 1 on success
 */

int check_cycle(listint_t *list)
{

	listint_t *node2 = list;

	while (list && list->next && node2 && node2->next)
	{
		list = list->next;
		node2 = node2->next->next;
		if (list == node2)
			return (1);
	}
	return (0);
}
