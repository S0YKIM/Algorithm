#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
  int answer = 0;
  int size = sizes.size();
  int maxWidth = 0;
  int maxHeight = 0;
  for (int i = 0; i < size; ++i) {
    if (sizes[i][0] >= sizes[i][1]) {
      maxWidth = max(maxWidth, sizes[i][0]);
      maxHeight = max(maxHeight, sizes[i][1]);
    } else {
      maxWidth = max(maxWidth, sizes[i][1]);
      maxHeight = max(maxHeight, sizes[i][0]);
    }
  }
  answer = maxWidth * maxHeight;
  return answer;
}
