void main(List<String> args) {
  amallar(6, 3, 4);
}

void amallar(a, b, n) {
  switch (n) {
    case 1: print("$a + $b = ${a + b}");
      break;
    case 2: print("$a - $b = ${a - b}");
      break;
    case 3: print("$a / $b = ${a / b}");
      break;
    case 4: print("$a * $b = ${a * b}");
  }
  
}