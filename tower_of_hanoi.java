public class tower_of_hanoi {
    public static void hanoi(int n,String s,String h,String d) {
        if (n == 1) {
            System.out.println(n + " moved from " + s + " to " + d);
            return;
        }
        hanoi(n - 1, s, d, h);
        System.out.println(n+" moved from "+s+" to "+d);
        hanoi(n - 1, h, s, d);
    }
    public static void main(String[] args) {
        hanoi(3, "start", "help", "destination");
    }
}