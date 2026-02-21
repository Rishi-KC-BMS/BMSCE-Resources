import java.util.*;
class quadratic 
{
    public static void main(String[] args)
    {

        int a,b,c,d;
        double r1,r2;
        System.out.println("\nRishi Kumar Chourasia - 1BF24CS253\n");
        Scanner in = new Scanner(System.in);

        System.out.print("Enter value of coefficient a - ");
        a = in.nextInt();
        System.out.println();

        System.out.print("Enter value of coefficient b - ");
        b = in.nextInt();
        System.out.println();

        System.out.print("Enter value of coefficient c - ");
        c = in.nextInt();
        System.out.println();

        if(a == 0)
        {
            System.out.println("Not a Quadratic Equation");
        }

        else
        {
            d= b*b - 4*a*c;

            if(d==0)
            {
                r1 = (-b)/(2*a);
                System.out.println("Roots are real and equal -> "+r1);
            }

            else if(d>0)
            {
                r1 = ((-b) + (Math.sqrt(d)))/(double)(2*a);
                r2 = ((-b) - (Math.sqrt(d)))/(double)(2*a);
                System.out.println("Roots are real and distinct-> "+r1+" and "+r2);
            }

            else
            {
            r1 = (-b)/(2*a);
            r2 = Math.sqrt(-d)/(2*a);
            System.out.println("Roots are imaginary -> "+r1+" and "+r2);
            }

            }
        }
    }
