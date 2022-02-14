package foundation.RecursionandBacktracking.RecursionInArrays;

import java.util.Scanner;

public class P4_Last_Index {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int key = sc.nextInt();
        sc.close();

        int ans = lastIndex(arr, N-1, key);
        System.out.println(ans);
    }

    public static int lastIndex(int[] arr, int idx, int x) {

        if (arr[idx] == x) {
            return idx;
        } else if (idx > 1) {
            return lastIndex(arr, idx - 1, x);
        } else {
            return -1;
        }
    }
}