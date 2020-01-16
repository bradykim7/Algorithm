import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for(int i=0;i<N;i++) {
			for(int j=N-i;j>0;j--) {
				System.out.print("*");
			}
			System.out.println();
		}

	}

}


