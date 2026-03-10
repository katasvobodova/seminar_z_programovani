using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        try
        {
            string[] prvniRadek = Console.ReadLine().Split();//Nacitani mest a silnic
            int pocetMest = int.Parse(prvniRadek[0]);
            int pocetSilnic = int.Parse(prvniRadek[1]);
            List<(int cil, int delka, int placena)>[] graf =
                new List<(int, int, int)>[pocetMest];
            for (int i = 0; i < pocetMest; i++)
                graf[i] = new List<(int, int, int)>();
            for (int i = 0; i < pocetSilnic; i++)
            {
                string[] radek = Console.ReadLine().Split();

                int mestoA = int.Parse(radek[0]);
                int mestoB = int.Parse(radek[1]);
                int delka = int.Parse(radek[2]);
                int placena = int.Parse(radek[3]); // 0 = zdarma, 1 = placená
                graf[mestoA].Add((mestoB, delka, placena));
                graf[mestoB].Add((mestoA, delka, placena));
            }

            string[] posledniRadek = Console.ReadLine().Split(); //Start a cil
            int start = int.Parse(posledniRadek[0]);
            int cil = int.Parse(posledniRadek[1]);

            int[,] vzdalenost = new int[pocetMest, 2];//Dijkstruv alg.
            bool[,] navstiveno = new bool[pocetMest, 2];
            (int mesto, int stav)[,] predchudce =
                new (int, int)[pocetMest, 2];
            for (int i = 0; i < pocetMest; i++)
                for (int s = 0; s < 2; s++)
                    vzdalenost[i, s] = int.MaxValue;
            vzdalenost[start, 0] = 0;
            predchudce[start, 0] = (-1, -1);
            for (int krok = 0; krok < 2 * pocetMest; krok++)
            {
                int aktualniMesto = -1;
                int aktualniStav = -1;
                int nejmensiVzdalenost = int.MaxValue;
                for (int m = 0; m < pocetMest; m++)
                {
                    for (int s = 0; s < 2; s++)
                    {
                        if (!navstiveno[m, s] &&
                            vzdalenost[m, s] < nejmensiVzdalenost)
                        {
                            nejmensiVzdalenost = vzdalenost[m, s];
                            aktualniMesto = m;
                            aktualniStav = s;
                        }
                    }
                }
                if (aktualniMesto == -1)
                    break;
                navstiveno[aktualniMesto, aktualniStav] = true;
                foreach (var silnice in graf[aktualniMesto])
                {
                    int dalsiMesto = silnice.cil;
                    int delkaSilnice = silnice.delka;
                    int jePlacena = silnice.placena;
                    int novyStav = aktualniStav + jePlacena;
                    if (novyStav > 1)
                        continue;
                    if (vzdalenost[aktualniMesto, aktualniStav] + delkaSilnice
                        < vzdalenost[dalsiMesto, novyStav])
                    {
                        vzdalenost[dalsiMesto, novyStav] =
                            vzdalenost[aktualniMesto, aktualniStav] + delkaSilnice;

                        predchudce[dalsiMesto, novyStav] =
                            (aktualniMesto, aktualniStav);
                    }
                }
            }

            int cilovyStav =
                vzdalenost[cil, 0] <= vzdalenost[cil, 1] ? 0 : 1;

            int nejkratsiVzdalenost = vzdalenost[cil, cilovyStav];

            List<int> cesta = new List<int>();
            int m2 = cil;
            int s2 = cilovyStav;

            while (m2 != -1)
            {
                cesta.Add(m2);
                var p = predchudce[m2, s2];
                m2 = p.mesto;
                s2 = p.stav;
            }
            cesta.Reverse();
            Console.WriteLine(string.Join("->", cesta));
            Console.WriteLine($"vzdálenost: {nejkratsiVzdalenost}");
        }
        catch
        {
            Console.WriteLine("Neplatný vstup");
        }
    }
}

