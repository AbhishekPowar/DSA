package foundation.RecursionandBacktracking.RecursionInArrays;

import java.util.Scanner;

public class P3_First_Index {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int key = sc.nextInt();
        sc.close();

        int ans = firstIndex(arr, 0, key);
        System.out.println(ans);
    }

    public static int firstIndex(int[] arr, int idx, int x) {

        if (arr[idx] == x) {
            return idx;
        } else if (idx < arr.length-1) {
            return firstIndex(arr, idx + 1, x);
        } else {
            return -1;
        }
    }
}