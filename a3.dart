import 'dart:io';
void main(List<String> args) {
  arif_prg(7, 5);
}

void arif_prg(int a, int d) {
    print("Progressiya nechta haddan iborat bo'lsin: ");
    int n = int.parse(stdin.readLineSync()!);
    List ls = [a];
     for (int i = 0; i < n - 1; i++) {
        ls.add(ls[i] + d);
    }
    print(ls);
}