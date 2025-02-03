void main(List<String> args) {
  ortacha(8, 7, 9);
}

void ortacha(int a, int b, int c) {
  if (a > b && b > c || b > a && b < c) {
    print("O'rtacha son $b");
  }
  if (b > c && c > a || c > b && c < a) {
    print("O'rtacha son $c");
  }
  if (c > a && a > b || a < b && a > c) {
    print("O'rtacha son $a");
  }
}