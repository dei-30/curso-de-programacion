using System;

public class presentarAwiguitos
{
    public static void Main(string[] args)
    {
        string[] amigos = new string[3]; // Corrected line
        
        amigos[0] = "darwin 40 años";
        amigos[1] = "netol 17 años";
        amigos[2] = "dickerson 15 años";
        
        Console.WriteLine("mis amigos son:");
        Console.WriteLine(amigos[0]);
        Console.WriteLine(amigos[1]);
        Console.WriteLine(amigos[2]);
    }
}

        