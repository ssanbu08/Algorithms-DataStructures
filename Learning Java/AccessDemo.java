

class AccessDemo {

    public static void main(String args[]){
        MyClass obj = new MyClass();

        obj.setAlpha(-99);
        System.out.println("obj.alpha is "+ obj.getAlpha());

        obj.alpha = 10;
    }
    
}
