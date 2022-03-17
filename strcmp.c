#include<stdio.h>

int ft_strcmp(char *a, char *b)
{
	return(*a == *b && *b == '\0')? 0 : (*a == *b)? ft_strcmp(++a , ++b): 1;
}

int main()
{
	char *a = "geeksfotgeeks";
	char *b = "geeksfotgeeksi";
	if(ft_strcmp(a, b) == 0)
		printf("String are same ");
	else
		printf("String are not same ");

	getchar();
	return 0;
}
