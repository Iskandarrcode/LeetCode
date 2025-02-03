void main(List<String> args) {
  birliklar(100, 5);
}


void birliklar(son, n) {
  switch (n) {
    case 1: print("$son kilogram -> $son kilogram ga teng:");
      break;
    case 2: print("$son milligram -> ${son / 1000000} kilogram ga teng:");
      break;
    case 3: print("$son gramm -> ${son / 1000} kilogram ga teng:");
      break;
    case 4: print("$son tonna -> ${son * 1000} kilogram ga teng:");
      break;
    case 5: print("$son sentener -> ${son * 100} kilogram ga teng:");
      break;
  }

}