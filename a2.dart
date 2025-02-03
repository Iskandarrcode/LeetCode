import 'dart:math';
import 'dart:io';

void main(List<String> args) {
  List ls = [];
  print("Arrayni nechta elementi bo'lsin: ");
  int n = int.parse(stdin.readLineSync()!);
  for (int i = 0; i <= n; i++) {
    ls.add(pow(2, i));
  }
  print(ls);
}


// void main() {
//   print('Enter a number: ');
//   int n = int.parse(stdin.readLineSync()!);
//   print('You entered: $n');
// }
