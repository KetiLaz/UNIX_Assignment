#include <stdio.h>
#include <math.h>

int main()
{
	char k;
	int total;
	total = 0;	

	while ( scanf("%c", &k) == 1 )
	{

		if (k == 'C' || k== 'c' || k=='G' || k=='g') 
		{
			total++;		
		}	
	}

	printf("The number of C is %d \n", total);
}
