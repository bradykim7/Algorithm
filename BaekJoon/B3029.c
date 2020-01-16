#include <stdio.h>

int main(void){
	int ah, am, as;
	int bh, bm, bs;
	int ch, cm, cs;
	scanf("%d:%d:%d\n%d:%d:%d", &ah, &am, &as, &bh, &bm, &bs);
	if(as > bs){
		bs += 60;
		bm -= 1;
	}
	if(am > bm){
		bm += 60;
		bh -= 1;
	}
	if(ah > bh){
		bh += 24;
	}

	ch = bh-ah;
	cm = bm-am;
	cs = bs-as;
    if(ch==0 && cm==0 &&cs ==0)
        printf("24:00:00");
    else 
	    printf("%02d:%02d:%02d", ch, cm, cs);
	return 0;
}
