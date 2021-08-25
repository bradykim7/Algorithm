import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		// 노잼 단어 제시 
		String m = sc.next();
		char [] m_result = new char [m.length()];
		String answer = "No Jam";
		
		for(int i =0; i<m.length();i++) {
			m_result[i] = m.charAt(i);
		}
		// 몇개 입력 
		int N = sc.nextInt();
		
		double result = 0;
		for(int i =0;i <N;i++) {
			String w = sc.next();
			double g = sc.nextDouble();
			
			int num =0;
			for(int j=0;j<w.length();j++) {
				if(m_result[num]==w.charAt(j))
					num+=1;
				//모든알파벳 포함 시 계산 
				if(num == m_result.length) {
					if(result < g / (w.length() - m.length())) {
							result = g / (w.length() - m.length());
							answer = w;
					}
					break;
				}
									
			}
			
		}

		System.out.println(answer);
	}

}
