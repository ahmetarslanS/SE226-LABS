#include <iostream>
#include <cmath>

using namespace std;

double sum_series(double n, int x) {
    if (x == 0) {
        return 1;
    }
    double term = pow(n, x) / tgamma(x + 1);
    return term + sum_series(n, x - 1);
}

//sum_series function overloaded.
double sum_series() {
    double n;
    cout << "Enter the value of n: ";
    cin >> n;

    int x;
    cout << "Enter the value of x: ";
    cin >> x;

    if (x == 0) {
        return 1;
    }

    double term = pow(n, x) / tgamma(x + 1);
    return term + sum_series(n, x - 1);
}

int main() {
    double n;
    int x;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "Enter the value of x: ";
   cin >> x;
    double result1 = sum_series(n, x);
    cout << "Result is : e^" << n << " = " << result1 <<endl;

    double result2 = sum_series();
    cout << "Result is : e^n = " << result2 <<endl;
    return 0;
}
