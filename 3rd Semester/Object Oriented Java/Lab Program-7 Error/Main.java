import java.util.Scanner;

class WrongAge extends Exception 
{
    public WrongAge(String message) 
    {
        super(message);
    }
}

class Father 
{
    int fatherAge;

    Father(int age) throws WrongAge
    {
        if (age<0) 
        {
            throw new WrongAge("Father's age cannot be negative!");
        }
        this.fatherAge = age;
    }
    void display()
    {
        System.out.println("Father's age : "+fatherAge);
    }
}


class Son extends Father{
    int sonAge;

    Son(int fatherAge,int sonAge) throws WrongAge
    {
        super(fatherAge);

        if (sonAge>=fatherAge)
            {
            throw new WrongAge
            (
                "Son's age cannot be greater than or equal to father's age!"
            );
        }

        if (sonAge<0)
        {
            throw new WrongAge("Son's age cannot be negative!");
        }

        this.sonAge=sonAge;
    }
}

public class Main
{
    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        int s_age,f_age;
        System.out.println("Enter father's age : ");
        f_age = in.nextInt();
        System.out.println("Enter son's age : ");
        s_age = in.nextInt();
        try{
              Son s = new Son(f_age,s_age);
              System.out.println("Father and Son objects created successfully!");
              s.display();
        }
        catch(WrongAge e)
        {
            System.out.println("Wrong Age Error: " + e.getMessage());
        }
    }
}
