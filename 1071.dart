void main(List<String> args) {
  String str1 = "ABABAB";
  String str2 = "ABAB";
  print(solution(str1, str2));

}

solution(String str1, String str2) {
  if (str1.length > str2.length) {
    if (str1.contains(str2) && str2.length % 2 != 0) {
      return str2;
    }
    else {
      for (var i = 0; i < str1.length; i++) {
        
      }
    }

  }

  if (str2.length > str1.length) {
    if (str2.contains(str1) && str1.length % 2 != 0) {
      return str1;
    }
  }

  
}