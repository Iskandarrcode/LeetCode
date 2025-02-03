void main(List<String> args) {
  kasrlar();
}


void kasrlar() {
  double sum = 0, kop = 1;
  int n = 2, a = 1;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      a = a * j;
    }
    kop = kop * a;
    sum += a;
    a = 1;
  }

  print("S = ${sum / kop}");
}