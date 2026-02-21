
public class prints {

    public class printMessage<T> {
        T message;

        printMessage(T message) {
            this.message = message;
        }

        void display() {
            System.out.println(message);
        }

    }

    public static void main(String[] args) {

        printing<Integer> p1 = new printing<Integer>(5);
        printing<String> p2 = new printing<String>("Hello");
        p1.display();
        p2.display();
    }

}
