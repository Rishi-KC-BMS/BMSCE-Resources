import java.util.Scanner;

class InputScanner 
{
    Scanner in = new Scanner(System.in);
}

abstract class Shape extends InputScanner 
{
    int x, y;

    abstract void printArea();

    void inputDimensions(int shapecode) 
    {
        if(shapecode==1)
        {
                System.out.print("Enter length: ");
                x = in.nextInt();
                System.out.print("Enter breadth: ");
                y = in.nextInt();
        }

        else if(shapecode==2)
        {
                System.out.print("Enter base: ");
                x = in.nextInt();
                System.out.print("Enter height: ");
                y = in.nextInt();
        }

        else if(shapecode==3)
        {
                System.out.print("Enter radius: ");
                x = in.nextInt();
        }
        else
        {
                System.out.println("Error");
        }
    }
}

class Rectangle extends Shape {
    void printArea() {
        double area = x * y;
        System.out.println("Area of Rectangle: " + area);
    }
}

class Triangle extends Shape {
    void printArea() {
        double area = 0.5 * x * y;
        System.out.println("Area of Triangle: " + area);
    }
}

class Circle extends Shape {
    void printArea() {
        double area = Math.PI * x * x;
        System.out.println("Area of Circle: " + area);
    }
}

public class Shapemain 
{
    public static void main(String[] args) 
    {
        Rectangle rect = new Rectangle();
        Triangle tri = new Triangle();
        Circle cir = new Circle();

        System.out.println("\nRectangle");
        rect.inputDimensions(1);
        rect.printArea();

        System.out.println("\nTriangle");
        tri.inputDimensions(2);
        tri.printArea();

        System.out.println("\nCircle");
        cir.inputDimensions(3);
        cir.printArea();
    }
}
