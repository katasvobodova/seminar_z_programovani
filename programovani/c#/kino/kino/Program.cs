namespace kino
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
                bool[,] sal = new bool[POCET_RAD, SEDADLA_V_RADE];
                for (int i = 0; i < POCET_RAD; i++)
                {
                    for (int j = 0; j < SEDADLA_V_RADE; j++)
                    {
                        sal[i, j] = true;
                    }
                }

                while (true)
                {
                    Console.WriteLine("Vaše možnosti: \n 1 - Zobrazit kinosál \n 2 - Rezervovat sedadlo \n 3 - Ukončit program \n Volba:");
                    string volba = Console.ReadLine();
                    if (volba == "1")
                    {
                        Console.WriteLine("\nKinosál (O = volné, X = obsazené)");

                        for (int r = 0; r < POCET_RAD; r++)
                        {
                            Console.Write($"Řada {r + 1}: ");

                            for (int s = 0; s < SEDADLA_V_RADE; s++)
                            {
                                Console.Write(sal[r, s] ? "O " : "X ");
                            }
                            Console.WriteLine();
                        }
                        Console.WriteLine();
                    }
                    else if (volba == "2")
                    {
                        Console.Write("Zadej řadu: ");
                        if (!int.TryParse(Console.ReadLine(), out int rada))
                        {
                            Console.WriteLine("Neplatný vstup.\n");
                            continue;
                        }

                        Console.Write("Zadej sedadlo: ");
                        if (!int.TryParse(Console.ReadLine(), out int sedadlo))
                        {
                            Console.WriteLine("Neplatný vstup.\n");
                            continue;
                        }

                        // kontrola zda to sedadlo v kině je
                        if (rada < 1 || rada > POCET_RAD ||
                            sedadlo < 1 || sedadlo > SEDADLA_V_RADE)
                        {
                            Console.WriteLine("Takové sedadlo v kině není.\n");
                            continue;
                        }

                        // kontrola jestli je sedadlo volné
                        if (!sal[rada - 1, sedadlo - 1])
                        {
                            Console.WriteLine("Sedadlo je obsazené, vyberte si jiné.\n");
                            continue;
                        }

                        // rezervace
                        sal[rada - 1, sedadlo - 1] = false;

                        // výpočet ceny
                        int cena = ZAKLADNI_CENA;
                        if (rada >= 7)
                        {
                            cena += VIP_PRIPLATEK;
                        }

                        Console.WriteLine($"Rezervace hotová. Cena: {cena} Kč\n");
                    }
                    else if (volba == "3")
                    {
                        Console.WriteLine("Program ukončen.");
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Zadej jednu z možností.\n");
                    }
                }
            }
        }
    }
