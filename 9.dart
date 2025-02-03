void main(List<String> args) {
  print(isPalindrome(121));
}

bool isPalindrome(int x) {
  String palindrom = x.toString();
  for (var i = 0; i < palindrom.length; i++) {
    if (palindrom[i] != palindrom[palindrom.length - i - 1]) {
      return false;
    }
  }
  return true;
}
