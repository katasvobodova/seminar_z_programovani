using System.Numerics;

namespace honzuv_projekt
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            int a = 2147483647;
            a += 1;
            a++;
            a = a + 1;
            uint b;
            char c = 'c';
            bool d;
            string s;
            float f;
            double g;
            long l;

            Console.WriteLine($"delka promenne typu int je {sizeof(int)}");
            Console.WriteLine($"c je {(int)0b01111100}");
        }
    }
}
