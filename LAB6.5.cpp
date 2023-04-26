#include <iostream>
#include <string>
#include <algorithm>
#include <list>

using namespace std;

//task1
void intersect(int list1[], int size1, int list2[], int size2, int result[], int &resultSize) {
    int i = 0, j = 0, k = 0;
    while (i < size1 && j < size2) {
        if (list1[i] == list2[j]) {
            result[k] = list1[i];
            i++;
            j++;
            k++;
        } else if (list1[i] < list2[j]) {
            i++;
        } else {
            j++;
        }
    }
    resultSize = k;
}

//task2
void findPalindromes(string input2[], int size2, string output2[], int &outputSize2) {
    int k = 0;
    for (int i = 0; i < size2; i++) {
        string str = input2[i];
        int left = 0, right = str.length() - 1;
        bool isPalindrome = true;
        while (left < right) {
            if (str[left] != str[right]) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }
        if (isPalindrome) {
            output2[k] = str;
            k++;
        }
    }
    outputSize2 = k;
}

//task 3
const int MAX_SIZE = 100;

int getPrimes(int input[], int size3, int output[]) {
    int max = input[0];
    for (int i = 1; i < size3; i++) {
        if (input[i] > max) {
            max = input[i];
        }
    }
    bool isPrime[MAX_SIZE + 1];
    for (int i = 0; i <= max; i++) {
        isPrime[i] = true;
    }
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i = 2; i * i <= max; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= max; j += i) {
                isPrime[j] = false;
            }
        }
    }
    int k = 0;
    for (int i = 0; i < size3; i++) {
        if (isPrime[input[i]]) {
            output[k] = input[i];
            k++;
        }
    }
    return k;
}

list<string> anagrams(string word, list<string> word_list) {
    list<string> output_list;

    sort(word.begin(), word.end());

    for (auto it = word_list.begin(); it != word_list.end(); it++) {
        string curr_word = *it;
        sort(curr_word.begin(), curr_word.end());

        if (curr_word == word) {
            output_list.push_back(*it);
        }
    }

    return output_list;
}


int main() {
    //task1
    int list1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
    int size1 = 16;
    int list2[] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26};
    int size2 = 13;
    int result[8];
    int resultSize;
    intersect(list1, size1, list2, size2, result, resultSize);
    for (int i = 0; i < resultSize; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    //task2
    string input[] = {"hello", "level", "world", "kapak"};
    int size = 4;
    string output[4];
    int outputSize;
    findPalindromes(input, size, output, outputSize);
    for (int i = 0; i < outputSize; i++) {
        cout << output[i] << " ";
    }
    cout << endl;
    //Task 3
    int input2[] = {2, 3, 4, 5, 6, 7, 8, 9};
    int size3 = 8;
    int output2[size3];
    int outputSize2 = getPrimes(input2, size3, output2);
    for (int i = 0; i < outputSize2; i++) {
        cout << output2[i] << " ";
    }
    cout << endl;
    //task 4
    string word = "tea";
    list<string> word_list = {"eat", "ate", "art", "tea", "rat", "tar", "far"};

    list<string> output_list = anagrams(word, word_list);

    for (auto it = output_list.begin(); it != output_list.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}
