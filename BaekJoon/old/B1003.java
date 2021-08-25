import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int T;
		
		Scanner sc = new Scanner(System.in);
		
		int result[][] = new int [41][2]; // made fibo[T][0], [T][1]
		result[0][0] =1;
		result[0][1] =0;
		result[1][0] =0;
		result[1][1] =1;		
		
		for(int i =2 ; i< 41;i++) {
			result[i][0] = result[i-2][0] + result[i-1][0];
			result[i][1] = result[i-2][1] + result[i-1][1];
		}
		
		T = sc.nextInt();
		int n[] = new int [T];

		
		for(int i =0; i < T ;i++) {
			 n[i]= sc.nextInt();
			 if(n[i] >41 || n[i] <0) {
				sc.close();
				System.exit(0);
			 }
		}
		for(int i =0;i <T; i++) {
			 System.out.println(result[n[i]][0]+" "+result[n[i]][1]);
		}

		sc.close();


	}

}


