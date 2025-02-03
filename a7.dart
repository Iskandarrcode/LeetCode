import 'dart:io';
void main(List<String> args) {

    String? nums = stdin.readLineSync();
    if (nums != null) {
        List ls = nums.split(" ");
        print(ls);
        for (int i = ls.length - 1; i >= 0; i--) {
            stdout.write(ls[i]);
        }
    } else {
        print("Input is null.");
    }
   
}