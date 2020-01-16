import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int [] Ai = new int [N];
		
		for(int i=0;i<N;i++) {
			Ai[i]=sc.nextInt();
		}
		Arrays.sort(Ai);
		long result =0;
		int num=1;
		for(int i =0;i<Ai.length;i++) {
			if(Ai[i]>=num) {
				result = result +Ai[i]-num;	
				num++;
			  }
				
		}
		System.out.println(result);

	}

}
