#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	int nombre, i;
	if (*head == NULL)
		return (1);
	else
	{
		current = *head;
		nombre = 0;
		while (current != NULL)
		{
			nombre++;
			current = current->next;
		}
		moitie = nombre / 2;
		if (moitie % 2 == 1)
		{
			for (int i = 0; i < moitie; i++)
			{
				listA[i] = current->n;
				current = current->next;
			}
			moitie++;
			for (int i = 0; i < moitie; i++)
			{
				listB[i] = current->n;
				current = current->next;
			}
		}
		else
		{
			



	
