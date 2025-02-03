void main(List<String> args) {
  tekshir(5, 5);
}

void tekshir(int a, int b){
  int sum = a + b;
  if (a != b){
    a = sum;
    b = sum;
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