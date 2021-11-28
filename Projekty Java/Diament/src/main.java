import java.util.Scanner;

public class main{
    public static void diament(int a ) {
        int n = a*2-2; //wielkość diamentu
        int h = n / 2; // współrzędne znaku
        for (int i = -h; i <= h; i++) {
            for (int j = -h; j <= h; j++) {
                if (Math.abs(i) + Math.abs(j) == h) System.out.print("#");
                else System.out.print("-");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Wielkość Diamentu ");
        int x = s.nextInt();
        diament(x);




    }


}