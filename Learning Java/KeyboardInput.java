import java.io.*;

class KeyboardInput {

    public static void main(String args[]) throws IOException 
    {
        
        int ch; //1. Declare a variable called "ch" of type char

        char answer = 25; // 2.Declare and Define a variable of type Char called answer with value 'T'

        System.out.println("Press a key followed by Enter:"); // 2. Print Statement
        while(true)
        {
            ch = System.in.read();//3. Read the value
            int difference = answer - ch;
            boolean lessCondition = (difference <= 10);
            boolean greatCondition = (difference  <= 20);
            //System.out.println(condition1);
            if(lessCondition)  // 4. Compare the value in the system with value from user
            {
                System.out.println(" You've guessed lower");
            }
            else if (greatCondition)
            {
                System.out.println(" You've guessed higher");
            }
            else
            {
                System.out.println("You're right");
                //System.out.println("Your Key is:" +ch);
                break;
                
            }
        }

        

    }
    
}