#include <string>
#include <vector>

using namespace std;

int solution(vector<int> common) {
  int answer = 0;
  int size = common.size();

  int sub = common[1] - common[0];
  int div = common[1] / common[0];
  if (common[2] - common[1] == sub)
    answer = common[size - 1] + sub;
  else
    answer = common[size - 1] * div;
  return answer;
}
