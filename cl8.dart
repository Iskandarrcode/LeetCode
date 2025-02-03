void main(List<String> args) {
  var ob = Talaba("Iskandar", "Iskandarov", 5);
  var ob2 = Talaba("Azamat", "Nematov", 3);
  var ob3 = Talaba("Nemat", "Akbarov", 4);
  List ls = [ob, ob2, ob3];

  void baholar(List ls) {
    var sum = ls[0];
    for (var i = 1; i < ls.length; i++) {
      if ( sum.baho < ls[i].baho) {
        sum = ls[i];
      }
    }
    print(sum.ism);
    print(sum.familiya);
    print(sum.baho);
  }

  baholar(ls);

}

class Talaba {
  String ism;
  String familiya;
  int baho;

  Talaba(this.ism, this.familiya, this.baho) {}
}