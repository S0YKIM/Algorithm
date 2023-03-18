#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
  int answer = 0;
  vector<int>::iterator it = lost.begin();
  vector<int>::iterator ite = lost.end();
  vector<int>::iterator pos;

  /* 여벌 체육복이 있었는데 도난 당한 학생은 상쇄되었으므로 lost, reserve 모든
   * 리스트에서 제거 */
  while (it != ite) {
    pos = find(reserve.begin(), reserve.end(), *it);
    if (pos != reserve.end()) {
      it = lost.erase(it);
      reserve.erase(pos);
      --ite;
    }
    ++it;
  }
  /* 체육복을 도난 당한 학생 번호 앞-뒤 순서로 여분 체육복을 빌려줄 학생 탐색 */
  /* 여분 체육복 빌려주고나서는 lost 에서 도난당한 학생 제거, reserve 에서 여분
   * 체육복 있던 학생 제거 */
  it = lost.begin();
  ite = lost.end();
  while (it != ite) {
    pos = find(reserve.begin(), reserve.end(), *it - 1);
    if (pos != reserve.end()) {
      it = lost.erase(it);
      --ite;
      reserve.erase(pos);
      continue;
    }
    pos = find(reserve.begin(), reserve.end(), *it + 1);
    if (pos != reserve.end()) {
      it = lost.erase(it);
      --ite;
      reserve.erase(pos);
      continue;
    }
    ++it;
  }
  /* 전체 학생 수 - 아직 체육복 못 빌린 학생 수 */
  answer = n - lost.size();
  return answer;
}
