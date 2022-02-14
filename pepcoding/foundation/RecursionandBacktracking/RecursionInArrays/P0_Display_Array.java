package foundation.RecursionandBacktracking.RecursionInArrays;

import java.util.Scanner;

public class P0_Display_Array {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        displayArr(arr, N - 1);

    }

    public static void displayArr(int[] arr, int idx) {
        if (idx > 0) {
            displayArr(arr, idx - 1);
        }
        System.out.println(arr[idx]);
    }
}
