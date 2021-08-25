ivimport java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String Ml = sc.next();
		String Mr = sc.next();
		String Tl = sc.next();
		String Tr = sc.next();

		if(Ml.equals(Mr)) {
			if(Ml.equals("R")) {
				if(Tl.equals("S") && Tr.equals("S"))
					System.out.println("MS");
				else if(Tl.equals("P") || Tr.equals("P"))
					System.out.println("TK");
				else 
					System.out.println("?");
			}
			else if(Ml.equals("S")){
				if(Tl.equals("P") && Tr.equals("P"))
					System.out.println("MS");
				else if(Tl.equals("R") || Tr.equals("R"))
					System.out.println("TK");
				else 
					System.out.println("?");			
			}
			else {
				if(Tl.equals("R") && Tr.equals("R"))
					System.out.println("MS");
				else if(Tl.equals("S") || Tr.equals("S"))
					System.out.println("TK");
				else 
					System.out.println("?");
				
			}
		}
		else if(Tl.equals(Tr)) {
			if(Tl.equals("R")) {
				if(Ml.equals("S") && Mr.equals("S"))
					System.out.println("TK");
				else if(Ml.equals("P") || Mr.equals("P"))
					System.out.println("MS");
				else 
					System.out.println("?");
			}
			else if(Tl.equals("S")){
				if(Ml.equals("P") && Mr.equals("P"))
					System.out.println("TK");
				else if(Ml.equals("R") || Mr.equals("R"))
					System.out.println("MS");
				else 
					System.out.println("?");			
			}
			else {
				if(Ml.equals("R") && Mr.equals("R"))
					System.out.println("TK");
				else if(Ml.equals("S") || Mr.equals("S"))
					System.out.println("MS");
				else 
					System.out.println("?");
				
			}
		}
		else 
			System.out.println("?");
		
			
	}

}
