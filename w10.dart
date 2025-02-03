void main(List<String> args) {
  shart(730);
}

void shart(n) {
  int i = 0;
  int sum = 1;
  while (sum <= n) {
    sum = sum * 3;
    i++;
  }
  print(i-1);
}