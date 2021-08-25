import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<=i;j++)
				System.out.print("*");
			for(int j=1;j<2*N-1-2*i;j++) {
				// j =1 i=0 10-1-0 9
				// j=1 i=1  10-1-1 8
				System.out.print(" ");
			}
			for(int j=0;j<=i;j++)
				System.out.print("*");
			System.out.println("");
		}
		
		for(int i=0;i<N-1;i++) {
			for(int j=N-i-1;j>0;j--)
				System.out.print("*");
			//2 4 6 8 
			for(int j=0;j<2+2*i;j++) {
				System.out.print(" ");
			}
			for(int j=N-i-1;j>0;j--)
				System.out.print("*");
			System.out.println("");
		}
	}

}
