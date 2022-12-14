#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: list to check
  * Return: 0 if there's no cycle, 1 if there is
  */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);
	current = list->next;

	while (current != NULL)
	{
		if (current == list)
			return (1);
		current = current->next;
	}
	return (0);
}
