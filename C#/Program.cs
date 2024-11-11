#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int N = int.Parse(reader.ReadLine());
        int[] arr = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse);

        int[] dp = new int[N];
        for (int i=0; i<N; i++) {
            dp[i] = 1;
        }
        for (int i=1; i<N; i++) {
            for (int j=0; j<i; j++) {
                if (arr[i] < arr[j]) {
                    dp[i] = Math.Max(dp[i], dp[j]+1);
                }
            }
        }

        writer.WriteLine(dp.Max());
        writer.Flush();
    }
}