import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String N = sc.next();
		
		for(int i=0;i<N.length();i++) {
			if(i%10 ==0 && i!=0)
				System.out.println("");
			System.out.print(N.charAt(i));
		}

	}

}
