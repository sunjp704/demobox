/*
Guass elimination methods for cyclic banded matrix with bandwidth 4.
2022.04.06
*/

void solCQBM(unsigned int Dim, const double a[], const double b[], const double c[], const double d[], const double e[], double phi[])
{
    double P[Dim];
    double Q[Dim];

    P[0] = -A[0][2] / A[0][1];
    Q[0] = d[0] / A[0][1];

    for (int i = 1; i < Dim; i++)
    {
        P[i] = -A[i][2] / (A[i][1] + A[i][0] * P[i - 1]);
        Q[i] = (d[i] - A[i][0] * Q[i - 1]) / (A[i][1] + A[i][0] * P[i - 1]);
    }

    phi[Dim - 1] = Q[Dim - 1];

    for (int i = Dim - 2; i > -1; i--)
    {
        phi[i] = P[i] * phi[i + 1] + Q[i];
    }

    return;
}