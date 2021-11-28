import java.util.Scanner;

public class main {
    public static void main() {
        Scanner inputScanner = new Scanner(System.in);
        System.out.println("podaj liczbe do tablicy kwardatowej");
        int x = inputScanner.nextInt();
        int[][] jodelka = new int[x][];
        int etap = 1;

        for (int i = 0; i < jodelka.length; ++i) {
            System.out.println();
            jodelka[i] = new int[x];
            for (int j = 0; j < jodelka[i].length; ++j) {
                if (j == 0 || i == 0) jodelka[i][j] = 1;
                else {
                    if (i > j) {
                        jodelka[i][j] = etap;
                        etap++;
                    } else {
                        jodelka[i][j] = i + 1;
                        etap = 2;
                    }
                }
                System.out.print(jodelka[i][j] + " ");
            }

        }
    }
    public static void main(String[] args) {
        main();
    }
}
