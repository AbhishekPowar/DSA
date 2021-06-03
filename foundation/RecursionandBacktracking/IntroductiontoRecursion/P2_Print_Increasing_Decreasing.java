package foundation.RecursionandBacktracking.IntroductiontoRecursion;

import java.util.Scanner;

public class P2_Print_Increasing_Decreasing {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        pdi(n);
    }

    public static void pdi(int n){
        printDecreasing(n);
        printIncreasing(n);
    }

    public static void printIncreasing(int n){
        if(n>1)printIncreasing(n-1);
        System.out.println(n);
    }

    public static void printDecreasing(int n){
        System.out.println(n);
        if (n>1)printDecreasing(n-1);
    }
}
