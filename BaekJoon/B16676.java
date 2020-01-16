import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		if(N<=10)
			System.out.println(1);
		else if(N<=110)
			System.out.println(2);
		else if(N<=1110)
			System.out.println(3);
		else if(N<=11110)
			System.out.println(4);
		else if(N<=111110)
			System.out.println(5);
		else if(N<=1111110)
			System.out.println(6);
		else if(N<=11111110)
			System.out.println(7);
		else if(N<=111111110)
			System.out.println(8);
		else if(N<=1111111110)
			System.out.println(9);
    }
}
		
