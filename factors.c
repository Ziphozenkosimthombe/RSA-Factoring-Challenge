#include <stdio.h>

int main()
{
        long long int num = 239809320265259;
        long int factor_1 = 2;
        long int factor_2;

        while (num % factor_1)
        {
                if (factor_1 <= num)
                {
                        factor_1++;
                }
                else
                {
                        return (-1);
                }
        }

        factor_2 = num / factor_1;
        printf("%lld = %ld * %ld\n", num, factor_2, factor_1);
        return (0);
}
