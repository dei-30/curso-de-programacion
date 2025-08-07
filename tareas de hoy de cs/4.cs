using System;
using System.Collections.Generic;

public class Program
{
    public static void Main(string[] args)
    {
        ExplicarListas();
    }

    static void ExplicarListas()
    {
        
        List<string> lista_de_nombres = new List<string>
        {
            "Victor Nava",
            "Mariana Quintero",
            "Elio Bracho",
            "Luis Quintero",
            "Julio Pacheco",
            "Darwin Villalobos",
            "Nestor Soto",
            "Santiago Vilchez",
            "Leomar Ferrer",
            "Isaac Bracho",
            "Dixon Gonzales",
            "Victor Pimentel",
            "Manuel Carvajal",
            "Abraham Quintero",
            "Mathias Tremont"
        };
        
        Console.WriteLine("Contenido inicial de la lista ");
        ImprimirLista(lista_de_nombres);

        Console.WriteLine("\nAgregando un nombre a la lista...");
        lista_de_nombres.Add("Daniel Espitia");
        
        Console.WriteLine("\nLista después de agregar un nombre");
        ImprimirLista(lista_de_nombres);

        Console.WriteLine("\nQuitando 'Daniel Espitia' de la lista...");
        lista_de_nombres.Remove("Daniel Espitia");
        
        Console.WriteLine("\nLista después de quitar un nombre");
        ImprimirLista(lista_de_nombres);
    }
    
    
    static void ImprimirLista(List<string> lista)
    {
        foreach (string nombre in lista)
        {
            Console.WriteLine(nombre);
        }
    }
}   
            
            
            
            