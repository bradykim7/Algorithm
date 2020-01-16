import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for(int i=0;i<N;i++) {
			for(int k=N-i-2;k>=0;k--)
				System.out.print(" ");
			for(int j=0;j<2*i+1;j++)
				System.out.print("*");
			System.out.println();
		}

	}

}


