import 'dart:io';

void main(List<String> args) {
  fibbonacci();
}

void fibbonacci() {

    print("Nechta Fibonacci sondan iborat List chop etilsin: ");
    int n = int.parse(stdin.readLineSync()!);
    List ls = [0, 1];
    for (int i = 0; i < n-2; i++) {
        ls.add(ls[i] + ls[i+1]);
    }
    print(ls);

}