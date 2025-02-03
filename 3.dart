void main(List<String> args) {
  print(lengthOfLongestSubstring("jljkljlk"));
}

int lengthOfLongestSubstring(String s) {
  List<int> lengths = [];
  int max = 0;
  String str = s.replaceAll(" ", "");

  if (str.isNotEmpty) {
    for (var i = 0; i < str.length; i++) {
      for (var j = i + 1; j < str.length; j++) {
        if (str[i] == str[j]) {
          lengths.add(j - i);
          break;
        }
      }
    }
    lengths.sort();
    max = lengths.last;
    return max;
  }
  return 0;
}
