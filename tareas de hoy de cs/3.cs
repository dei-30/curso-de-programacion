using System;

namespace FundamentosDeCSharp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            ExplicarArrays();
        }

        public static void ExplicarArrays()
        {
            Console.WriteLine("Edades de mis amigos:");

            
            int[] Edades = new int[15];
            Edades[0] = 18;
            Edades[1] = 21;
            Edades[2] = 24;
            Edades[3] = 21;
            Edades[4] = 15;
            Edades[5] = 17;
            Edades[6] = 21;
            Edades[7] = 17;
            Edades[8] = 16;
            Edades[9] = 15;
            Edades[10] = 16;
            Edades[11] = 17;
            Edades[12] = 13;
            Edades[13] = 14;
            Edades[14] = 13;

            
            for (int i = 0; i < Edades.Length; i++)
            {
                Console.WriteLine($"La edad del #{i} es: {Edades[i]}");
            }
        }
    }
}