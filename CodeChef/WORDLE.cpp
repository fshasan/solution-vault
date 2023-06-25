#include <iostream>

using namespace std;

int main() {
  int n;
  char S[5], T[5], M[5];
  cin >> n;

  while (n != 0) {
    for (int i = 0; i < 5; i++) {
      cin >> S[i];
    }
    for (int i = 0; i < 5; i++) {
      cin >> T[i];
      if (S[i] == T[i]) {
        M[i] = 'G';
      } else {
        M[i] = 'B';
      }
    }

    for (int i = 0; i < 5; i++) {
      cout << M[i];
    }

    cout << '\n';

    n--;
  }

  return 0;
}
