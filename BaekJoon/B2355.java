import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub		
		long a, b;
		long sum = 0;
		Scanner sc = new Scanner(System.in);
		a= sc.nextInt();
		b= sc.nextInt();		
		

		// a , b 가 같을
		if(a == b) {
			sum = a;
		}
		else if(b>a) {
			sum = (b*(b+1)-a*(a-1))/2;
				
		}
		else if(a>b) {
			sum = (a*(a+1)-b*(b-1))/2;
		}

		System.out.println(sum);
		
	}

}


