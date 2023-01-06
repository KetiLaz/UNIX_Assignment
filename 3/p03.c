#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{

	char seq[500];
	int length;
	float cg = 0;
	float percentage;
	int i;

	scanf("%s", seq);
	length = strlen(seq);

	for (i=0; i <length; i++)
	{
		if(seq[i] == 'C' || seq[i] == 'G')
		{
			cg++;			
		}		
	}
	
	percentage = (cg / length) * 100;
	printf("The percentage of CGs is: %f\n", percentage);
}
