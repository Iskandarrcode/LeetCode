import 'dart:io';

void main(List<String> args) {
  int n = 5;
  int k = 1;
  int sum = 0;
  for (var i = 1; i <= n; i++) {
    stdout.write(" $k ");
    sum += k;
    if (i != n) {
      stdout.write("+");
    }
    k = k * 10 + 1;
  }
  print(" = $sum");
}
