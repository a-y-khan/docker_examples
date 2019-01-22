#include <iostream>

int min(const int a, const int b)
{
    return (a < b) ? a : b;
}

int binomialCoeff(const int n, const int k)
{
    int C[n+1][k+1];
    for (int i = 0; i <= n; ++i)
    {
        for (int j = 0; j <= min(i, k); ++j)
        {
            // base case
            if (j == 0 || j == i)
            {
                C[i][j] = 1;
            }
            else
            {
                C[i][j] = C[i-1][j-1] + C[i-1][j];
            }
        }
    }
    return C[n][k];
}

int main()
{
    int n = 5, k = 2;
    int coeff = binomialCoeff(n, k);
    std::cout << "Value of binomial coefficient C(" << n << ", " << k << ") = " << coeff << std::endl;
    return 0;
}
