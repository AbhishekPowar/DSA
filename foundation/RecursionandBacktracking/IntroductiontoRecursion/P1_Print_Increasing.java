package foundation.RecursionandBacktracking.IntroductiontoRecursion;

import java.util.Scanner;

public class P1_Print_Increasing {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        printIncreasing(n);
    }

    public static void printIncreasing(int n){
        if(n>1)printIncreasing(n-1);
        System.out.println(n);
    }
}
