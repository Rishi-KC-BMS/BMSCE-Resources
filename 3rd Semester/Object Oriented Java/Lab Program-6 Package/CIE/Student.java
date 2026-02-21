package CIE;

import java.util.Scanner;

public class Student {
    protected String usn;
    protected String name;
    protected int sem;

    public void inputStudentDetails() {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter USN: ");
        usn = in.nextLine();
        System.out.print("Enter Name: ");
        name = in.nextLine();
        System.out.print("Enter Semester: ");
        sem = in.nextInt();
    }

    public void displayStudentDetails() {
        System.out.println("USN: " + usn);
        System.out.println("Name: " + name);
        System.out.println("Semester: " + sem);
    }
}
