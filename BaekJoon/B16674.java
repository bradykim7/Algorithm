import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		int two=0;
		int zero=0;
		int one=0;
		int eight=0;
		int other = 0;
		
		for(int i=0;i<input.length();i++) {
			if(input.charAt(i) == 50)
				two+=1;
			else if(input.charAt(i) == 48)
				zero+=1;
			else if(input.charAt(i) == 49)
				one+=1;
			else if(input.charAt(i) == 56)
				eight+=1;
			else 
				other +=1;
		}
		
		if(other != 0) {
			System.out.println("0");
			return;
		}
		else {
			if(two >=1 && zero >=1 && one >= 1 && eight >=1) {
				if(two==zero && zero ==one && one ==eight) {
					System.out.println("8");
					return;

				}
				System.out.println("2");
				return;
			}
			System.out.println("1");
			return;
			
		}		
	}

}





