import SEE.Externals;

class Main {
    public static void main(String args[]) {
        int n = 0;
        java.util.Scanner s = new java.util.Scanner(System.in);

        System.out.print("Enter number of students: ");
        n = s.nextInt();

        Externals arr[] = new Externals[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter details of student " + (i + 1));
            arr[i] = new Externals();
            arr[i].inputStudentDetails();
            arr[i].inputCIEmarks();
            arr[i].inputSEEmarks();
            arr[i].calculateFinalMarks();
        }

        System.out.println("\nFINAL MARKS ");
        for (int i = 0; i < n; i++) {
            System.out.println("\nStudent " + (i + 1) + ":");
            arr[i].displayFinalMarks();
        }
    }
}
