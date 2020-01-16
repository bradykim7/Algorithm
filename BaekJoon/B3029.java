import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int [] time = new int[6]; // hh:mm:ss , hh:mm:ss
		String input  =null;
		String [] no2 =null;
		int [] result =new int[3];
		// 입력 받기 
		for(int i=0; i<2;i++) {
			input =br.readLine();
			no2 = input.split(":");
			for(int j =0;j<3;j++) {
				if(i ==0)
					time[j] = Integer.parseInt(no2[j]);
				else 
					time[j+3] = Integer.parseInt(no2[j]);						
			}				
		}
		//계산 
		for(int i=0;i<result.length;i++)
			result[i]= time[i+3]- time[i];

		if(result[2]<0) {
			result[2] = 60+result[2];
			result[1] -= 1;
		}
		if(result[1]<0) {
			result[1] = 60+result[1];
			result[0] -= 1;
		}
		
		if(result[0]<0) {
			result[0] = 24+result[0];
		}

		if(result[0]==0 && result[1]==0 &&result[2]==0)
			System.out.println("24:00:00");
		else if(result[0]<0 || result[1] <0 || result[2]<0)
			System.exit(0);
		else 
			System.out.format("%02d:%02d:%02d",result[0],result[1],result[2]);

	}

}
