import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String T = br.readLine();
		int tLength = T.length();
		int result1=0;
		StringBuilder result = new StringBuilder();

		int [] a = new int [1000001];
		for(int i=0;i<tLength;i++)
		{	
			if(T.charAt(i) == 49)
				a[i] =1;
			else if (T.charAt(i) ==48)
				a[i] =0;	
			else 
				System.exit(0);
		}
		// 3개씩 떨어질
		if(tLength%3 ==0) {
			for(int i =0;i<tLength;i+=3) {
				result1=a[i]*4 +a[i+1]*2+a[i+2]*1;// a[0]*4+a[1]*2+a[2]*1
				result.append(result1);
			}
		}
		//맨 앞이 2개 
		else if (tLength%3 ==2)
		{
			result1 = a[0]*2+a[1]*1;
			result.append(result1);
			for(int i =2;i<tLength;i+=3) {
				result1=a[i]*4 +a[i+1]*2+a[i+2]*1;// a[2]*4+a[3]*2+a[4]*1
				result.append(result1);
			}
			
		}
		else {
			result1 = a[0]*1;
			result.append(result1);
			for(int i =1;i<tLength;i+=3) {
				result1=a[i]*4 +a[i+1]*2+a[i+2]*1;// a[1]*4+a[2]*2+a[3]*1
				result.append(result1);
			}
			
		}

		System.out.println(result);
		
	}

}


