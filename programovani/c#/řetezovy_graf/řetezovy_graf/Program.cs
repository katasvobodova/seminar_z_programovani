namespace řetízkový_graf
{
    internal class Program
    {

        static void Main(string[] args)
        {
            int pocetLidi = Convert.ToInt32(Console.ReadLine());
            int[,] graf = new int[pocetLidi, pocetLidi];
            string vstupniData = Console.ReadLine();
            string[] dvojice = vstupniData.Split();//
                                                   // Source - https://stackoverflow.com/a
                                                   // Posted by iTURTEV, modified by community. See post 'Timeline' for change history
                                                   // Retrieved 2025-11-11, License - CC BY-SA 3.0



            double[,] matrix = new double[pocetLidi, pocetLidi];



            for (int i = 0; i < dvojice.Length; i++)
            {
                dvojice[i].Split('-');

                matrix[dvojice[0], dvojice[1]] = input;
            }
        }

    }
}

    }
}