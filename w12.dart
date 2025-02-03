void main(List<String> args) {
  summ(45);
}

void summ(n) {
  int sum = 0, i = 0;

  while (sum <= n) {
    i++;
    sum += i;
  }
  print("Sum = ${sum - i}\n");
  print(i-1);
}