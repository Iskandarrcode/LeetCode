import 'dart:io';

void main(List<String> args) {
    var count = 0;
    String ? input_n = stdin.readLineSync();

    if (input_n != null) {
        List ls = input_n.split(" ");
        for (int i = ls.length - 1; i >= 0; i--) {
            int nums = int.tryParse(ls[i]) ?? 0;
            if (nums % 2 == 0) {
                count ++;
                stdout.write(ls[i] + " ");
            }
        }
        print("\nNumber of pair: $count");
    }
}