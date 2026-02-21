class MessageThread extends Thread {
    private String message;
    private int interval; 

    MessageThread(String message, int interval) {
        this.message = message;
        this.interval = interval;
    }

    public void run() {
        try {
            while (true) {
                System.out.println(message);
                Thread.sleep(interval);
            }
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MessageThread t1 = new MessageThread("BMS College of Engineering", 10000);
        MessageThread t2 = new MessageThread("CSE", 2000);

        t1.start();
        t2.start();
    }
}
