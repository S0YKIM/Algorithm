#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
  vector<int> answer;
  int size = arr.size();
  int num = arr.front();

  for (int i = 0; i < size; ++i) {
    if (answer.size() == 0 || arr[i] != num) {
      answer.push_back(arr[i]);
      num = arr[i];
    }
  }
  return answer;
}
