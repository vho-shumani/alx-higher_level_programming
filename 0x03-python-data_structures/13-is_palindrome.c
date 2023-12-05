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
 * reverse_listint - reverses a listint_t linked list.
 * @head: linked list
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp = *head, *next = *head;

	if (*head == NULL)
	{
		return (NULL);
	}
	tmp = tmp->next;
	(*head)->next = NULL;
	while (tmp != NULL)
	{
		next = tmp->next;
		tmp->next = *head;
		*head = tmp;
		tmp = next;
	}
	return (*head);
}
/**
 *is_palindrome - determine linked list is palindrome.
 *@head: pointer to linked list
 *Return: 1 if is palindrome, 0 if is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	size_t count = 1, i = 1;

	if (*head == NULL)
		return (1);
	while (count < list_len(tmp))
	{
		tmp = tmp->next;
		count++;
	}
	reverse_listint(&tmp);
	while (tmp->next != NULL)
	{
		if (tmp->n != (*head)->n)
			return (0);
		tmp = tmp->next;
		(*head) = (*head)->next;
		i++;
	}
	if (tmp->n != (*head)->n)
		return (0);
	return (1);
}
