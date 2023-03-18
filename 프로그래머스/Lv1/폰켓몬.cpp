#include <algorithm>
#include <map>
#include <utility>
#include <vector>
using namespace std;

bool compByValue(const pair<int, int>& a, const pair<int, int>& b) {
  return a.second < b.second;
}

int solution(vector<int> nums) {
  int size = nums.size();
  int answer = size / 2;
  map<int, int> counter;
  pair<map<int, int>::iterator, bool> ret;

  /* nums 에 들어있는 숫자들 개수 세어 map 에 저장 */
  for (int i = 0; i < size; ++i) {
    ret = counter.insert(make_pair(nums[i], 0));
    if (ret.second == false) ++counter[nums[i]];
  }
  /* map 의 <key, value> 쌍을 다시 벡터로 옮겨 value 오름차순으로 정렬 */
  vector<pair<int, int>> sortedNums(counter.begin(), counter.end());
  sort(sortedNums.begin(), sortedNums.end(), compByValue);

  /* 중복되는 숫자 개수 제거 */
  vector<pair<int, int>>::reverse_iterator rit = sortedNums.rbegin();
  vector<pair<int, int>>::reverse_iterator rite = sortedNums.rend();
  while (rit != rite) {
    if (rit->second == 1) break;
    answer -= rit->second - 1;
    ++rit;
  }
  return answer;
}
