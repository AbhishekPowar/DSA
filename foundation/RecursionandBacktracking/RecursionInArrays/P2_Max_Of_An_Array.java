package foundation.RecursionandBacktracking.RecursionInArrays;

import java.util.Scanner;

public class P2_Max_Of_An_Array {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();

        int arrMax = maxOfArray(arr, N-1);
        System.out.println(arrMax);
    }

    public static int maxOfArray(int[] arr, int idx) {
        if(idx==0) return arr[0];
        return Integer.max(arr[idx], maxOfArray(arr, idx-1));
    }
}