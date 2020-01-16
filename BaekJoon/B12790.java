import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int HP, MP, ATK, DEF;
		int HP1, MP1, ATK1, DEF1;
		int HP2, MP2, ATK2, DEF2;

		int T =sc.nextInt();
		int [] result = new int [T];
		for(int i=0;i<T;i++) {
			HP=sc.nextInt();
			MP=sc.nextInt();
			ATK=sc.nextInt();
			DEF=sc.nextInt();
			HP1=sc.nextInt();
			MP1=sc.nextInt();
			ATK1=sc.nextInt();
			DEF1=sc.nextInt();
			
			HP2 = HP +HP1;
			MP2 = MP +MP1;
			ATK2 = ATK +ATK1;
			DEF2 = DEF +DEF1;
			if(HP2 <1)
				HP2= 1;
			if(MP2 <1)
				MP2 =1;
			if(ATK2 < 0)
				ATK2= 0;
			result[i]= HP2+ 5*MP2 +2*ATK2 +2*DEF2;

		}
		for(int i=0;i<result.length;i++)
			System.out.print(result[i]+" ");
	}

}


