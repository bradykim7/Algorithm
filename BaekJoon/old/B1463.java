import java.util.*;
import java.io.*;

public class Main {


	public static void main(String args[]) {
		Scanner sc  = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[] table = new int[1000001];

		for (int index = 2; index <= N; index++) {
			table[index] = table[index - 1] + 1;
			if (index % 2 == 0)
				table[index] = Math.min(table[index], table[index / 2] + 1);
			if (index % 3 == 0)
				table[index] = Math.min(table[index], table[index / 3] + 1);
		}

		System.out.println(table[N]);
	}
}
