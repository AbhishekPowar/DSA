package foundation.RecursionandBacktracking.IntroductiontoRecursion;

import java.util.Scanner;

public class P0_Print_Decreasing {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        printDecreasing(n);
    }

    public static void printDecreasing(int n){
        System.out.println(n);
        if (n>1)printDecreasing(n-1);
    }
}
