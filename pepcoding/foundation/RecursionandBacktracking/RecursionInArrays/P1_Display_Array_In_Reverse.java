package foundation.RecursionandBacktracking.RecursionInArrays;

import java.util.Scanner;

public class P1_Display_Array_In_Reverse {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        displayArrReverse(arr, N - 1);
    }

    public static void displayArrReverse(int[] arr, int idx) {
        System.out.println(arr[idx]);
        if (idx > 0) {
            displayArrReverse(arr, idx - 1);
        }
    }

}