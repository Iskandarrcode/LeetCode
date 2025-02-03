void main(List<String> args) {
    var singiltonObject = singiltonClass();
    singiltonObject.printer();
}

class singiltonClass {
  singiltonClass._privateConstructor();

  static final _instance = singiltonClass._privateConstructor();


    factory singiltonClass () {
        return _instance;
    }

    void printer() {
        print("Hello world");
    }

}