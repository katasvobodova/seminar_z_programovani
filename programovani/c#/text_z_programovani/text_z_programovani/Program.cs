using System.ComponentModel.Design;

namespace text_z_programovani
{
    internal class Program
    {
        static void Main()//string[] args
        {
            vstup = Console.ReadLine();
            //Když se v programu nachází q, program se vypne
            // Ted by se to melo rozdelit, ale to nevim jak se dela, nejdrive podle ", " na souřadnice, potom podle ";" na jednotlivé souřadnice, potom bz se to spočítalo jako dole
            a = int(1); //prvni bod
            b = int(2);
            c = int(3); //druhy bod
            d = int(4);
            e = int(5); //treti bod
            f = int(6);
            delka1 = Math.Sqrt((a - c) * (a - c) + (b - d) * (b - d)); // Prvni a druhy
            delka2 = Math.Sqrt((c - e) * (c - e) + (d - f) * (d - f)); // Druhy a treti
            delka3 = Math.Sqrt((a - e) * (a - e) + (b - f) * (b - f)); // Treti a prvni
            if((a - c) ; (b - d)) = (c * (a - e) ; c * (b - f)):// když jeden vektor je násobkem toho druhého
            {
                Console.WriteLine("Tyto tři body netvoří trujúhelník");
            }
            else():
            {
                Console.WriteLine(delka1);
                Console.WriteLine(delka2);
                Console.WriteLine(delka3);
            }
        }
    }
}
