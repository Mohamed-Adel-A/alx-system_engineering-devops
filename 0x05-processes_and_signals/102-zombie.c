#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

/**
 * infinite_while - function that is allways working
 *
 * Return: int (0)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


int main(void)
{
	pid_t pid;
	int i;

	for (i = 0 ; i < 5 ; i++)
	{
		pid = fork();

		if (pid > 0)
		{
			printf("Zombie process created, PID: %i/n", pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}

