#include "lists.h"


int is_palindrome(listint_t **head)
{
	listint_t *nl, *p;

	if (head == NULL || *head == NULL)
		return (1);
	p = *head;
	while (p)
	{
		add_node(&nl, &p->n);
		p = p->next;
	}

/**
 * comparelist - function that compare list
 * @head1: first list
 * @head2: second list
 * Return: return
 */

int comparelist(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1 == temp2)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}


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
void reverse(listint_t **head_ref)
{
	listint_t *prev = NULL, *next = NULL;
	while (*head_ref != NULL)
	{
		next = (*head_ref)->next;
		(*head_ref)->next = prev;
		prev = *head_ref;
		*head_ref = next;
	}
	*head_ref = prev;
	return (head_ref);
}


/**
 * is_palindrome - check if the singly list is a palindrome
 * @head: double pointer to the first node
 * Return: 0 if it is not a palindrome and 1 if yes
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *second_half, *prev = head;
	listint_t *midnode = NULL;

	if (head != NULL && head->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev->next = NULL;
		reverse(second_half);
		result = comparelist(head, second_half);
		if (midnode != NULL)
		{
			prev->next = midnode;
			midnode->next = second_half;
		}
		else
			prev->next = second_half;
	}
return (0);
}
