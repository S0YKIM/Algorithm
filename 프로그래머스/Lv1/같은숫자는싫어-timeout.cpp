#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
  vector<int> answer = arr;
  vector<int>::reverse_iterator rit = answer.rbegin() + 1;
  vector<int>::reverse_iterator rite = answer.rend();
  int num = answer.back();

  while (rit != rite) {
    if ((*rit) == num)
      answer.erase(rit.base());
    else
      num = *rit;
    ++rit;
  }
  return answer;
}
