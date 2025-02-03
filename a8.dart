import 'dart:io';

void main(List<String> args) {
    var count = 0;
    print("Input List elements: ");
    String ? input_nums = stdin.readLineSync();
    if (input_nums != null) {
        List ls = input_nums.split(" ");
        for (int i = 0; i < ls.length; i++) {
            int num_int = int.tryParse(ls[i]) ?? 0;
            if (num_int % 2 != 0) {
                count++;
                stdout.write(ls[i] + " ");
            }
        }
        print("\nOdd number: $count");
    }
    else {
        print("Input is null");
    }
}