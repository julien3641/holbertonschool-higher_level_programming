#include "lists.h"

/**
 * insert_node - insert a node at the good place
 * @head: pointer to a pointer on the first node
 * @number: integer to be include in the new node
 * Return: The address of the new node or NULL if fail
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp = *head;


	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
        new_node->n = number;
	while (tmp && tmp->next && tmp->next->n < number)
		tmp = tmp->next;

	new_node->next = tmp->next;
	tmp->next = new_node;
	return (new_node);
}
