import 'dart:io';
void main(List<String> args) {
  gem_prg(2, 3);
}

void gem_prg(a, d) {
  print("Progressiya nechata haddan tashkil topsin: ");
  int n = int.parse(stdin.readLineSync()!);
  List ls = [a];

  for (int i = 0; i < n - 1; i++) {
    ls.add(ls[i] * d);
  }
  print(ls);

}
