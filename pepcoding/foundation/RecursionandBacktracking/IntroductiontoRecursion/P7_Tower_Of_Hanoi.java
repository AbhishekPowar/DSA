package foundation.RecursionandBacktracking.IntroductiontoRecursion;
import java.util.Scanner;

public class P7_Tower_Of_Hanoi {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t1id = sc.nextInt();
	int t2id = sc.nextInt();
        int t3id = sc.nextInt();
        sc.close();

        toh(n, t1id, t2id, t3id);
    }

    public static void toh(int n, int t1id, int t2id, int t3id) {
        if (n == 1) {
            System.out.printf("%d[%d -> %d]\n", n, t1id, t3id);

        } else {

            toh(n - 1, t1id, t3id, t2id);
            System.out.printf("%d[%d -> %d]\n", n, t1id, t3id);
            toh(n - 1, t2id, t1id, t3id);
        }
    }
}
