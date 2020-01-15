import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import javax.imageio.IIOException;

public class Main {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
		int	T = Integer.parseInt(br.readLine()); //Int

		
		int  [] result  = new int[T];
		
		for (int i =0; i<result.length;i++) {
				String line = br.readLine();
				int [] num = new int [6];//x1, y1, r1, x2, y2, r2;
				StringTokenizer st = new StringTokenizer(line);
				for (int j = 0; st.hasMoreTokens(); j++) {
					num[j] = Integer.parseInt(st.nextToken());
				}
				
				int pointlength = (num[3]-num[0])*(num[3]-num[0]) + (num[4]-num[1])*(num[4]-num[1]);
				int rlength1=  (num[5]+num[2])*(num[5]+num[2]);
				int rlength2=  (num[5]-num[2])*(num[5]-num[2]);

				if (num[0]==num[3] && num[1]==num[4] && num[2]==num[5])
					result[i] =-1;
				else if(pointlength == rlength1 || pointlength == rlength2)
					result[i] =1;
				else if(pointlength <rlength2 || pointlength > rlength1)
					result[i] =0;
				else 
					result[i]=2;

		}
		for(int i=0; i<result.length;i++)
			System.out.println(result[i]);;
	}
	

}
