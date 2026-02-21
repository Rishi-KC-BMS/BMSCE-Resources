import java.util.Scanner;

class Subject {
    int subjectMarks;
    int credits;
    int grade;
    
    public Subject() {
        this.subjectMarks = 0;
        this.credits = 0;
        this.grade = 0;
    }
}

class Student {
    String name;
    String usn;
    double SGPA;
    Scanner s;
    Subject[] subject;
    
    public Student() {
        s = new Scanner(System.in);
        subject = new Subject[8];
        for (int i = 0; i < 8; i++) {
            subject[i] = new Subject();
        }
    }

    public void getStudentDetails() {
        System.out.print("Enter student name: ");
        name = s.nextLine();
        System.out.print("Enter student USN: ");
        usn = s.nextLine();
    }

    public void getMarks() {
        for (int i = 0; i < 8; i++) {
            System.out.print("Enter marks for subject " + (i + 1) + ": ");
            subject[i].subjectMarks = s.nextInt();
            System.out.print("Enter credits for subject " + (i + 1) + ": ");
            subject[i].credits = s.nextInt();
            
            subject[i].grade = (subject[i].subjectMarks / 10) + 1;
            
            if (subject[i].grade == 11) {
                subject[i].grade = 10;
            }
            if (subject[i].grade <= 4) {
                subject[i].grade = 0; 
            }
        }
    }
    public void computeSGPA() {
        int effectiveScore = 0;
        int totalCredits = 0;
        
        for (int i = 0; i < 8; i++) {
            effectiveScore += (subject[i].grade * subject[i].credits);
            totalCredits += subject[i].credits;
        }
        
        SGPA = (double) effectiveScore / totalCredits;
    }


    public void display() {
        System.out.println("\nStudent Details:");
        System.out.println("Name: " + name);
        System.out.println("USN: " + usn);
        System.out.println("SGPA: " + SGPA);
    }
}

public class Main {
      public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of students: ");
        int n = scanner.nextInt();
        scanner.nextLine();

        Student[] students = new Student[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter details for student " + (i + 1) + ":");
            students[i] = new Student();
            students[i].getStudentDetails();
            students[i].getMarks();
            students[i].computeSGPA();
        }

        System.out.println("\n--- Student Results ---");
        for (int i = 0; i < n; i++) {
            students[i].display();
        }

        scanner.close();
    }
}
