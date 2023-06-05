#include "lists.h"

/**
 * check_cycle - check for a cycle in a list
 * @list: list
 * Return: cycle ? 1 : 0
 */
int check_cycle(listint_t *list)
{
	listint_t *back = list;
	listint_t *front = list;

	if (list == NULL || list->next == NULL)
		return (0);
	for (;;)
	{
		if (front->next && front->next->next)
		{
			back = back->next;
			front = (front->next)->next;
			if (back == front)
				return (1);
		}
		else return (0);
	}
}
