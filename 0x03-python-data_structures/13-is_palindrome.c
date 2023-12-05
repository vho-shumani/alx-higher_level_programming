#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *list_len - determine the number of elements in linked list.
 *@h: linked list
 *Return: number of elements in linked list.
 */
size_t list_len(const listint_t *h)
{
	const listint_t *temp = h;
	size_t count = 0;

	while (temp != NULL)
	{
		temp = temp->next;
		count++;
	}
	return (count);
}
/**
 *is_palindrome - determine linked list is palindrome.
 *@head: pointer to linked list
 *Return: 1 if is palindrome, 0 if is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int *ptr = (int *)malloc(sizeof(listint_t) * list_len(tmp)), i = 0;

	if (ptr == NULL)
	{
		perror("mallac:");
	}
	if (*head == NULL)
	{
		return (1);
	}
	while (tmp != NULL)
	{
		ptr[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	for (int j = 0, x = i - 1; x >= j; j++, x--)
	{
		if (ptr[j] != ptr[x])
		{
			return (0);
		}
	}
	return (1);
}
