void main(List<String> args) {
  String text = "  this   is  a sentence ";

  var ob = LeetCode();
  ob.space(text);
}

class LeetCode {
  void space(String text) {
    int count = 0;
    String str = "";
    for (int i = 0; i < text.length; i++) {
      if (text[i] == " ") {
        count++;
      } else {}
    }
    print(count);
  }
}
