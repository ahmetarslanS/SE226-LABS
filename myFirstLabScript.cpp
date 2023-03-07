#include <iostream>

using namespace std;

int main() {

    string name;
    cout << "What is your name?\n";
    cin >> name;
    cout << "Hello " << name << endl;

    string id;
    cout << "What is your Student ID?\n";
    cin >> id;
    cout << "Your ID is " << id << endl;

    int var1, var2;

    cout << "Enter the first number. " << endl;
    cin >> var1;
    cout << "Enter the second number. " << endl;
    cin >> var2;

    int sum = var1 + var2;
    int diff = var1 - var2;
    int prod = var1 * var2;

    cout << "First value: " << var1 << "\nSecond value: " << var2 << endl;
    cout << "Summation: " << sum << "\nDifference: " << diff
         << "\nProduct: " << prod << endl;

    string studentName;
    int lab, mid, final;
    cout << "Enter your name." << endl;
    cin >> studentName;
    cout << "Enter your Lab Score." << endl;
    cin >> lab;
    cout << "Enter your Midterm result." << endl;
    cin >> mid;
    cout << "Enter your Final result." << endl;
    cin >> final;

    double lastScore = ((lab * 0.25) + (mid * 0.35) + (final * 0.4));
    cout << "Name: " << studentName << "\nLab: " << lab << "\nMidterm: " << mid << "\nFinal: " << final << endl;
    cout << "Last Score: " << lastScore << endl;

    cout << "*\n**\n***\n**\n*" << endl;

    return 0;
}
