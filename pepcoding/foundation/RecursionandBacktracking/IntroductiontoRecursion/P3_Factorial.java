package foundation.RecursionandBacktracking.IntroductiontoRecursion;

import java.util.Scanner;

public class P3_Factorial {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
	sc.close();

        int fact = factorial(n);
        System.out.println(fact);
    }

    public static int factorial(int n) {
        if (n < 2)
            return 1;
        else
            return n * factorial(n - 1);
    }
}
