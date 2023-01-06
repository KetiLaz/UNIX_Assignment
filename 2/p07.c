#include <stdio.h>
#include <math.h>

int main()
{
	char k;
	float total = 0;
	float all = 0;	
	
	while ( scanf("%c", &k) == 1 )
	{
		all ++;
		
		if (k == 'C' || k== 'c' || k=='G' || k=='g') 
		{
			total++;		
		}
	
	}
	
	float percentage = (total / all) * 100;

	printf("The percentage of CG in the sequence is %f\n", percentage);
}
