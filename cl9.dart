void main(List<String> args) {
  var ob = Human("Iskandar", 22, "Flutter developer(Android, Ios)", 1.76, 70, true);
  ob.get_name();
  ob.get_age();
  ob.get_profession();
  ob.get_height();
  ob.get_weight();
  ob.get_single();
}

class Human {
  String name;
  int age;
  String profession;
  double height;
  int weight;
  bool single;

  Human(this.name, this.age, this.profession, this.height, this.weight, this.single) {}

  void get_name() {
    print("Name: $name\n");
  }

  void get_age() {
    print("Age: $age\n");
  }

  void get_profession() {
    print("Profession: $profession\n");
  }

  void get_height() {
    print("Height: $height\n");
  }

  void get_weight() {
    print("Weight: $weight\n");
  }

  void get_single() {
    print("Single: $single\n");
  }

}