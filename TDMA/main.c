/*

2022.04.01
*/

#define ND 128

#include <stdio.h>
#include "TDMA.h"

int main(void)
{
    double A[ND][3];
    double d[ND];
    double phi[ND];

    // read A and b from file
    FILE *fp1 = fopen("A.txt", "r");
    FILE *fp2 = fopen("d.txt", "r");
    if (fp1 == NULL || fp2 == NULL)
    {
        printf("Can't open files.\n");
        return -1;
    }
    for (int i = 0; i < ND * 3; i++)
    {
        fscanf(fp1, "%lf", &A[0][0] + i);
    }
    for (int i = 0; i < ND; i++)
    {
        fscanf(fp2, "%lf", &d[0] + i);
    }
    fclose(fp1);
    fclose(fp2);
    solCTDMA(ND, A, d, phi);
    FILE *fp3 = fopen("phi.txt", "w");
    for (int i = 0; i < ND; i++)
    {
        fprintf(fp3, "%.15E\n", *(phi + i));
    }
    fclose(fp3);
    return 0;
}