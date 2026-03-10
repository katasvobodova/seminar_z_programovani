using System;

namespace RetizkovyGraf
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int pocetLidi = Convert.ToInt32(Console.ReadLine());
            int[,] sousednost = new int[pocetLidi + 1, pocetLidi + 1];

            // načtení dvojic sousednosti
            string[] dvojice = Console.ReadLine().Split(' ');
            foreach (string d in dvojice)
            {
                string[] casti = d.Split('-');
                int a = Convert.ToInt32(casti[0]);
                int b = Convert.ToInt32(casti[1]);
                sousednost[a, b] = 1;
                sousednost[b, a] = 1;
            }

            // načtení startu a cíle
            string[] vstup = Console.ReadLine().Split(' ');
            int start = Convert.ToInt32(vstup[0]);
            int cil = Convert.ToInt32(vstup[1]);

            // BFS
            int[] fronta = new int[pocetLidi + 1];
            int zacatek_fronty = 0;
            int konec = 0;

            bool[] navstiveno = new bool[pocetLidi + 1];
            int[] predchudce = new int[pocetLidi + 1];

            fronta[konec++] = start;
            navstiveno[start] = true;
            predchudce[start] = -1;

            while (zacatek_fronty < konec)
            {
                int prozkoumavana_osoba = fronta[zacatek_fronty++];

                for (int i = 1; i <= pocetLidi; i++)
                {
                    bool jsouPropojeni = (sousednost[prozkoumavana_osoba, i] == 1);
                    bool jesteNenavstiven = (!navstiveno[i]);

                    if (jsouPropojeni && jesteNenavstiven)
                    {
                        navstiveno[i] = true;
                        predchudce[i] = prozkoumavana_osoba;
                        fronta[konec++] = i;
                    }
                }
            }

            // výstup
            if (!navstiveno[cil])
            {
                Console.WriteLine("neexistuje");
                return;
            }

            // rekonstrukce cesty
            int[] cesta = new int[pocetLidi + 1];
            int delka = 0;
            int aktualni_vrchol = cil;

            while (aktualni_vrchol != -1)
            {
                cesta[delka++] = aktualni_vrchol;
                aktualni_vrchol = predchudce[aktualni_vrchol];
            }

            for (int i = delka - 1; i >= 0; i--)
            {
                Console.Write(cesta[i] + " ");
            }
        }
    }
}
