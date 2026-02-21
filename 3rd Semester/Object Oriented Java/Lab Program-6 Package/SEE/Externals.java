package SEE;

import CIE.Internals;
import java.util.Scanner;

public class Externals extends Internals {

    protected int marksSEE[];       
    protected int finalMarks[];     

    public Externals() {
        marksSEE = new int[5];
        finalMarks = new int[5];
    }

    public void inputSEEmarks() {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter SEE marks for 5 subjects:");
        for (int i = 0; i < 5; i++) {
            System.out.print("SEE Mark " + (i + 1) + ": ");
            marksSEE[i] = s.nextInt();
        }
    }

    public void calculateFinalMarks() {
        for (int i = 0; i < 5; i++) {
            finalMarks[i] = marks[i] + marksSEE[i];  
        }
    }

    public void displayFinalMarks() {
        displayStudentDetails();
        System.out.println("Final marks (CIE + SEE):");
        for (int i = 0; i < 5; i++) {
            System.out.println("Subject " + (i + 1) + ": " + finalMarks[i]);
        }
    }
}

