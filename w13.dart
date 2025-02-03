void main(List<String> args) {
  kasr(1);
}

void kasr(a) {
  double sum = 0;
  int i = 0;

  while (sum <= a) {
    i++;
    sum += 1 / i;
  }
  print("Sum = $sum\n");
  print(i);
}