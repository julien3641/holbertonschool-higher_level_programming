#include "lists.h"

/**
 * count_node - count the number of nodes
 * @head: pointer to a list
 * Return: return the number of nodes
 */

int count_node(listint_t **head)
{
	int count = 0;
	listint_t *temp;

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		count++;
	}
	return (count);
}

/**
 * reverse - reverse the order of the nodes
 * @head_ref: double pointer to a list
 */
void reverse(struct Node **head_ref)
{
	struct Node *prev = NULL;
	struct Node *current = *head_ref;
	struct Node *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}
