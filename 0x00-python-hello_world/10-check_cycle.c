#include "lists.h"

/**
 * check_cycle - checks if there a loop in a linked list
 * @list: head of the linked least
 * Return: 1 if there is a loop, 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL, *curr = NULL;

	while (list)
	{
		curr = list, tmp = list;
		while (curr)
		{
			curr = curr->next;
			if (curr == tmp)
				return (1);
		}
		list = list->next;
	}
	return (0);

}
