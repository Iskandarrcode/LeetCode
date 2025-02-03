void main(List<String> args) {
  katta(10, 7, 20);
  kichik(10, 7, 20);
}


void katta(int a, int b, int c) {
  if (a > b && a > c) {
    print("Eng kattasi: $a");
  }
  if (b > a && b > c) {
    print("Eng kattasi: $b");
  }
  if (c > a && c > b) {
    print("Eng kattasi: $c");
  }
}

void kichik(int a, int b, int c) {
  if (a < b && a < c) {
    print("Eng kichigi: $a");
  }
  if (b < a && b < c) {
    print("Eng kichigi: $b");
  }
  if (c < a && c < b) {
    print("Eng kichigi: $c");
  }
}