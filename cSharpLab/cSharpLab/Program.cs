using System;

namespace cSharpLab
{
    class Program
    {
        static void Main(string[] args)
        {
            EnumComparison.Run();
            Terminate();
        }

        private static void Terminate()
        {
            Console.WriteLine("Press the `Any Key` to conitnue...");
            Console.ReadKey();
        }
    }
}
