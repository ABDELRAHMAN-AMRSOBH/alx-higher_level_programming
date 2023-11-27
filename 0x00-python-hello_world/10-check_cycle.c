#include "lists.h"

/**
 * check_cycle - checks if list is in cycle
 * @list: the start of list
 * Return: 1 or 0
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast)
	{
		if (fast->next)
			fast = fast->next->next;
		else
			return (0);
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
