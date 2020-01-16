import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int C = sc.nextInt();
		int K = sc.nextInt();
		int P = sc.nextInt();
		
		int result =0;
		for(int i =1;i<=C;i++)
			result += K*i+P*i*i;
		
		System.out.println(result);

	}

}
