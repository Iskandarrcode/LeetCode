void main(List<String> args) {
  birliklar(100, 5);
}


void birliklar(son, n) {
  switch (n) {
    case 1: print("$son detsimetr -> ${son / 10} metr ga teng:");
      break;
    case 2: print("$son kilometr -> ${son * 1000} metr ga teng:");
      break;
    case 3: print("$son metr -> $son metr ga teng:");
      break;
    case 4: print("$son millimetr -> ${son / 1000} metr ga teng:");
      break;
    case 5: print("$son santimetr -> ${son / 100} metr ga teng:");
      break;
  }

}