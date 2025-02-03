void main(List<String> args) {
  var ob = Bino(40, "Black");
  var ob2 = Bino(50, "White");
  var ob3 = Bino(60, "Yellow");
  var ob4 = Bino(30, "Blue");
  var ob5 = Bino(70, "Violet");

  List ls = [ob, ob2, ob3, ob4, ob5];

  ob.katta(ls);

}

class Bino {
  int balandligi;
  String rangi;

  Bino(this.balandligi, this.rangi) {}

    void katta(List ls) {
      for (int i = 1; i < ls.length; i++) {
        if (ls[i].balandligi > 50) {
          print(ls[i].rangi);
        }
      }
    }

}