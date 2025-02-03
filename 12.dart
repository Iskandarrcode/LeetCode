void main(List<String> args) {
  kattasi(26, 26, 26);
}

void kattasi(int a, int b, int c) {
  if (a > b && a > c) {
    print("Eng katta son: $a");
  }
  if (b > a && b > c) {
    print("Eng katta son: $b");
  }
  if (c > a && c > b) {
    print("Eng katta son: $c");
  }
  if (a == b && a == c) {
    print("Uchala son ham teng:");
  }
}