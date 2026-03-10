using System;
using System.IO;

namespace binarni_vyhledavaci_strom
{
    internal class Program
    {
        static void Main(string[] args)
        {
            binarníVyhledávacíStrom<Student> strom =
                new binarníVyhledávacíStrom<Student>();

            foreach (string radek in File.ReadAllLines("studenti_shuffled.csv"))
            {
                string[] data = radek.Split(';');

                int id = int.Parse(data[0]);
                string jmeno = data[1];
                string trida = data[2];

                Student s = new Student(id, jmeno, trida);
                strom.Insert(id, s);
            }

            Console.Write("Zadej číselně ID studenta, kterého chceš najít: ");
            int hledaneId = int.Parse(Console.ReadLine());
            var nalezeny = strom.NalezeníPrvku(hledaneId);
            if (nalezeny != null)
                Console.WriteLine(nalezeny.Value);
            else
                Console.WriteLine("Student s ID, jež bylo vloženo asi není.");

            Console.WriteLine("\nStudent s nejnižším ID:");
            Console.WriteLine(strom.NalezeníMinima().Value);

            Console.Write("\nZadej ID nového studenta: ");
            int noveId = int.Parse(Console.ReadLine());
            Console.Write("Zadej jméno: ");
            string jmeno = Console.ReadLine();
            Console.Write("Zadej třídu: ");
            string trida = Console.ReadLine();
            Student mujStudent = new Student(noveId, jmeno, trida);
            strom.Insert(noveId, mujStudent);
            Console.WriteLine("Student byl vložen.");
        }
    }
    class Student
    {
        public int ID;
        public string Jméno;
        public string Třída;

        public Student(int id, string jmeno, string trida)
        {
            ID = id;
            Jméno = jmeno;
            Třída = trida;
        }

        public override string ToString()
        {
            return $"{Jméno} (ID: {ID}) ze třídy {Třída}";
        }
    }
    class binarníVyhledávacíStrom<T>
    {
        public Uzel<T> Kořen;
        public void Insert(int novýKlíč, T nováHodnota)
        {
            void _insert(Uzel<T> uzel, int klíč, T hodnota)
            {
                if (klíč < uzel.Key)
                {
                    if (uzel.LevýSyn == null)
                        uzel.LevýSyn = new Uzel<T>(klíč, hodnota);
                    else
                        _insert(uzel.LevýSyn, klíč, hodnota);
                }
                else if (klíč > uzel.Key)
                {
                    if (uzel.PravýSyn == null)
                        uzel.PravýSyn = new Uzel<T>(klíč, hodnota);
                    else
                        _insert(uzel.PravýSyn, klíč, hodnota);
                }
            }

            if (Kořen == null)
                Kořen = new Uzel<T>(novýKlíč, nováHodnota);
            else
                _insert(Kořen, novýKlíč, nováHodnota);
        }
        public Uzel<T> NalezeníPrvku(int klíč)
        {
            Uzel<T> aktuální = Kořen;

            while (aktuální != null)
            {
                if (klíč == aktuální.Key)
                    return aktuální;
                else if (klíč < aktuální.Key)
                    aktuální = aktuální.LevýSyn;
                else
                    aktuální = aktuální.PravýSyn;
            }

            return null;
        }
        public Uzel<T> NalezeníMinima()
        {
            Uzel<T> aktuální = Kořen;
            while (aktuální.LevýSyn != null)
                aktuální = aktuální.LevýSyn;

            return aktuální;
        }
        public void OdstraněníPrvku(int klíč)
        {
            Kořen = OdstraněníRec(Kořen, klíč);
        }

        private Uzel<T> OdstraněníRec(Uzel<T> uzel, int klíč)
        {
            if (uzel == null)
                return null;

            if (klíč < uzel.Key)
                uzel.LevýSyn = OdstraněníRec(uzel.LevýSyn, klíč);
            else if (klíč > uzel.Key)
                uzel.PravýSyn = OdstraněníRec(uzel.PravýSyn, klíč);
            else
            {
                if (uzel.LevýSyn == null)
                    return uzel.PravýSyn;
                if (uzel.PravýSyn == null)
                    return uzel.LevýSyn;

                Uzel<T> min = NajdiMinimum(uzel.PravýSyn);
                uzel.Key = min.Key;
                uzel.Value = min.Value;
                uzel.PravýSyn = OdstraněníRec(uzel.PravýSyn, min.Key);
            }

            return uzel;
        }

        private Uzel<T> NajdiMinimum(Uzel<T> uzel)
        {
            while (uzel.LevýSyn != null)
                uzel = uzel.LevýSyn;

            return uzel;
        }

        public void VypsáníStromu()
        {
            VypsáníRec(Kořen);
            Console.WriteLine();
        }

        private void VypsáníRec(Uzel<T> uzel)
        {
            if (uzel == null) return;

            VypsáníRec(uzel.LevýSyn);
            Console.Write($"{uzel.Key} ");
            VypsáníRec(uzel.PravýSyn);
        }
    }
    class Uzel<T>
    {
        public int Key;
        public T Value;

        public Uzel<T> LevýSyn;
        public Uzel<T> PravýSyn;

        public Uzel(int key, T value)
        {
            Key = key;
            Value = value;
        }
    }
}