#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
  vector<int> answer;
  int size = commands.size();
  vector<int>::iterator it = array.begin();

  for (int i = 0; i < size; ++i) {
    const vector<int>& idx = commands[i];
    vector<int> newstr(it + idx[0] - 1, it + idx[1]);
    sort(newstr.begin(), newstr.end());
    answer.push_back(newstr[idx[2] - 1]);
  }
  return answer;
}
