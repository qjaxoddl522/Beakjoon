#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int N = int.Parse(reader.ReadLine());
        Queue<int> queue = new Queue<int>();
        bool[] isQueue = new bool[N];

        int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
        for (int i=N-1; i>=0; i--) {
            isQueue[i] = input[i] == 0;
        }

        input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
        for (int i=N-1; i>=0; i--) {
            if (isQueue[i])
                queue.Enqueue(input[i]);
        }
        
        int M = int.Parse(reader.ReadLine());
        input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
        for (int i=0; i<M; i++) {
            queue.Enqueue(input[i]);
            writer.Write(queue.Dequeue() + " ");
        }

        writer.Flush();
    }
}