void main(List<String> args) {
  tekshir(12, 10);
}

void tekshir(int a, int b) {
  if (a != b) {
    if (a > b) {
      b = a;
    }
    else {
      a = b;
    }
    print(a);
    print(b);
  }
  else {
    a = 0;
    b = 0;
    print(a);
    print(b);
  }
}