using System;

namespace retizkovy_graf
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1) Počet vrcholů
            int pocet = Convert.ToInt32(Console.ReadLine());

            // 2) Matice sousednosti
            int[,] matrix = new int[pocet + 1, pocet + 1];

            // 3) Načtení hran
            string[] dvojice = Console.ReadLine().Split(' ');

            foreach (string d in dvojice)
            {
                string[] xy = d.Split('-');
                int a = Convert.ToInt32(xy[0]);
                int b = Convert.ToInt32(xy[1]);

                matrix[a, b] = 1;
                matrix[b, a] = 1;
            }

            // 4) Načtení start a cíl
            string[] vstup = Console.ReadLine().Split(' ');
            int start = Convert.ToInt32(vstup[0]);
            int cil = Convert.ToInt32(vstup[1]);

            // 5) BFS BEZ QUEUE, fronta ručně:
            int[] queue = new int[pocet + 1];
            int head = 0;
            int tail = 0;

            bool[] visited = new bool[pocet + 1];
            int[] pred = new int[pocet + 1];

            queue[tail++] = start;
            visited[start] = true;
            pred[start] = -1;

            while (head < tail)
            {
                int v = queue[head++];

                for (int i = 1; i <= pocet; i++)
                {
                    if (matrix[v, i] == 1 && !visited[i])
                    {
                        visited[i] = true;
                        pred[i] = v;
                        queue[tail++] = i;
                    }
                }
            }

            // 6) Cesta neexistuje
            if (!visited[cil])
            {
                Console.WriteLine("neexistuje");
                return;
            }

            // 7) Rekonstrukce cesty BEZ List<>
            int[] cesta = new int[pocet + 1];
            int len = 0;

            int t = cil;
            while (t != -1)
            {
                cesta[len++] = t;
                t = pred[t];
            }

            // 8) Výpis cesty v opačném směru
            for (int i = len - 1; i >= 0; i--)
            {
                Console.Write(cesta[i] + " ");
            }
        }
    }
}