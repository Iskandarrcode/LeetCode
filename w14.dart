void main(List<String> args) {
  double sum = 0;
  int i = 0, n = 2;

  while (sum <= n) {
    i++;
    sum += 1 / i;
  }
  print("Sum = ${sum - 1 / i}\n");
  print(i-1);
}