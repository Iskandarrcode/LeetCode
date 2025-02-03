void main(List<String> args) {
  summ(55);
}

void summ(n) {
  double sum = 0;
  int i = 0;
  while (sum <= n) {
    i++;
    sum += i;
  }
  print("Sum = $sum\n");
  print(i);
}