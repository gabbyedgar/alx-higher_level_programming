#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - insert a node to a sorted list
 * @head: sorted list
 * @number: number to insert
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	if (*head == NULL)
	{
		node->n = number;
		node->next = *head;
		*head = node;
		return (node);
	}
	else if (number <= (*head)->n)
	{
		node->n = number;
		node->next = *head;
		*head = node;
		return (node);
	}
	else
	{
		temp = *head;
		while (node && node->next && node->next->n < number)
		node = node->next;

	temp->next = node->next;
	node->next = temp;
	return (temp);
	}
	return (NULL);
}
