/*
Tri-diagonal matrix algorithms.
solTDMA solves strcit Tri-diagonal equtaions;
solTDMA_0 is for the condition when first element is 0;
solCTDMA suits when matrix is cyclic.
2022.04.01
*/

//Tri-diagonal matrix algorithm

void solTDMA(unsigned int Dim,const double A[][3], const double d[], double phi[])
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

//Tri-diagonal matrix algorithm if first element=0
void solTDMA_0(unsigned int Dim,const double A[][3], const double d[], double phi[])
{
    double A_0[Dim-1][3];
    double d_0[Dim-1];
    double phi_0[Dim-1];

    phi[1] = d[0] / A[0][2];
    d_0[0] = d[1] - phi[1] * A[1][1];
    d_0[1] = d[2] - phi[1] * A[2][0];
    for (int i = 2; i < Dim - 1;i++)
    {
        d_0[i] = d[i + 1];
    }
    for (int i = 0; i < Dim - 1; i++)
    {
        if (i==0)
        {
            A_0[i][1]=A[1][0];
            A_0[i][2] = A[1][2];
        }
        else
        {
            for (int j = 0; j < 3;j++)
            {
                A_0[i][j] = A[i+1][j];
            }
        }
    }
    A_0[1][0] = 0;

    solTDMA(Dim - 1, A_0, d_0, phi_0);
    phi[0] = phi_0[0];
    for (int i = 2; i < Dim; i++)
    {
        phi[i] = phi_0[i - 1];
    }
    return;
}

void solCTDMA(unsigned int Dim,const double A[][3], const double d[], double phi[])
{
    double A_c[Dim][3];
    double y[Dim];
    double u[Dim];
    double q[Dim];
    double vTy;
    double vTq;

    for (int i = 0; i < Dim; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            A_c[i][j] = A[i][j];
        }
    }
    //A_c[0][0] = 0;
    //A_c[0][1] = 0;
    A_c[Dim - 1][1] = A[Dim - 1][1] - A[0][0] * A[Dim - 1][2] / A[0][1];
    //A_c[Dim-1][2] = 0;

    u[0] = A[0][1];
    u[Dim-1] = A[Dim-1][2];
    for (int i = 1; i < Dim-1; i++)
    {
        u[i] = 0;
    }

    solTDMA_0(Dim, A_c, d, y);
    solTDMA_0(Dim, A_c, u, q);
    vTy = y[0] + y[Dim - 1] * A[0][0] / A[0][1];
    vTq = q[0] + q[Dim - 1] * A[0][0] / A[0][1];
    for (int i = 0; i < Dim; i++)
    {
        phi[i] = y[i] - q[i] * vTy / (1 + vTq);
    }
    return;
}
