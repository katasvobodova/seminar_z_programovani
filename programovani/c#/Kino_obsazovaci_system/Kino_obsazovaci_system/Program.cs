namespace Kino_obsazovaci_system
{
    using System;
    class Program
    {
        // Ze zadání
        const int POCET_RAD = 8;
        const int SEDADLA_V_RADE = 10;

        const int ZAKLADNI_CENA = 180;
        const int VIP_PRIPLATEK = 70;


        static void Main()
        {
            // true = volné sedadlo, false = obsazené sedadlo
            bool[,] salon = new bool[POCET_RAD, SEDADLA_V_RADE];
            for (int i = 0; i < POCET_RAD; i++)
            {
                for (int j = 0; j < SEDADLA_V_RADE; j++)
                {
                    salon[i, j] = true;
                }
            }

            while (true)
            {
                Console.WriteLine("Vaše možnosti: \n 1 - Zobrazit kinosál \n 2 - Rezervovat sedadlo \n 3 - Ukončit program");
                Console.WriteLine("1 - Zobrazit kinosál");
                Console.WriteLine("2 - Rezervovat sedadlo");
                Console.WriteLine("3 - Ukončit program");
                Console.Write("Volba: ");

                string volba = Console.ReadLine();

                if (volba == "1")
                {
                    // Zobrazení sálu
                    Console.WriteLine("\nKinosál (O = volné, X = obsazené)");

                    for (int r = 0; r < POCET_RAD; r++)
                    {
                        Console.Write($"Řada {r + 1}: ");

                        for (int s = 0; s < SEDADLA_V_RADE; s++)
                        {
                            Console.Write(salon[r, s] ? "O " : "X ");
                        }
                        Console.WriteLine();
                    }
                    Console.WriteLine();
                }
                else if (volba == "2")
                {
                    Console.Write("Zadej řadu: ");
                    int rada = int.Parse(Console.ReadLine());

                    Console.Write("Zadej sedadlo: ");
                    int sedadlo = int.Parse(Console.ReadLine());

                    // kontrola zda je v sále uvedené místo
                    if (rada < 1 || rada > POCET_RAD ||
                        sedadlo < 1 || sedadlo > SEDADLA_V_RADE)
                    {
                        Console.WriteLine("❌ Sedadlo neexistuje.\n");
                        continue;
                    }

                    // kontrola volnosti sedadla
                    if (!salon[rada - 1, sedadlo - 1])
                    {
                        Console.WriteLine("❌ Sedadlo je obsazené.\n");
                        continue;
                    }

                    // rezervace
                    salon[rada - 1, sedadlo - 1] = false;

                    // výpočet ceny
                    int cena = ZAKLADNI_CENA;
                    if (rada >= 7)
                    {
                        cena += VIP_PRIPLATEK;
                    }

                    Console.WriteLine($"Rezervace hotova cena: {cena} Kč\n");
                }
                else if (volba == "3")
                {
                    Console.WriteLine("Program ukončen.");
                    break;
                }
                else
                {
                    Console.WriteLine("Zadej jednu z možností :-( \n");
                }
            }
        }
    }


