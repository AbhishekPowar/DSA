package foundation.RecursionandBacktracking.IntroductiontoRecursion;

import java.util.Scanner;

public class P5_Power_logarithmic {
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
        if (n == 2)
            return x * x;
        return ((n & 1) == 0) ? power(power(x, n / 2), 2) : power(power(x, n / 2), 2) * x;
    }
}
