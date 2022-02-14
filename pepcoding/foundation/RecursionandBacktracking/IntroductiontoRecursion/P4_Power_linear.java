package foundation.RecursionandBacktracking.IntroductiontoRecursion;

import java.util.Scanner;

public class P4_Power_linear {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int n = sc.nextInt();
        sc.close();

        int ans = power(x, n);
        System.out.println(ans);
    }

    public static int power(int x, int n) {
        if (n == 0)
            return 1;

        if (n == 1)
            return x;
        else
            return x * power(x, n - 1);

    }

}
