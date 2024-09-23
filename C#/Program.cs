using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int[] NM = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse);
        int N = NM[0]; int M = NM[1];
        
        List<int>[] graph = new List<int>[N+1];
        for (int i=1; i<N+1; i++) {
            graph[i] = new List<int>();
        }
        for (int i=0; i<M; i++) {
            int[] line = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse);
            graph[line[0]].Add(line[1]);
            graph[line[1]].Add(line[0]);
        }
        
        int answer = 0;
        int minBacon = int.MaxValue;
        Queue<(int node, int dist)> q = new Queue<(int, int)>();
        for (int i=1; i<N+1; i++) {
            int bacon = 0;
            bool[] visited = new bool[N+1];
            q.Enqueue((node: i, dist: 0));
            while (q.Count > 0) {
                var v = q.Dequeue();
                if (visited[v.node])
                    continue;
                visited[v.node] = true;
                bacon += v.dist;
                
                foreach (var next in graph[v.node]) {
                    q.Enqueue((node: next, dist: v.dist+1));
                }
            }
            if (bacon < minBacon) {
                answer = i;
                minBacon = bacon;
            }
        }
        writer.WriteLine(answer);
        
        reader.Close();
        writer.Flush();
        writer.Close();
    }
}