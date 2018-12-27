using System;
using System.Linq;

namespace cSharpLab
{
    static class Luhn
    {
        internal static void Run()
        {
            foreach (string testCC in testCCs)
                Console.WriteLine(testCC + " LuhnCheck " + LuhnCheck(testCC));
            Console.ReadLine();
        }

        static readonly string[] testCCs =
        {
            "4266841537822247",
            "4599540745620587",
            "4266841464731387",
            "79927398713"
        };

        static bool LuhnCheck(string ccNumber)
        {
            int[] digits = ccNumber.ToCharArray()
                .Select(digit => (int)char.GetNumericValue(digit)).ToArray();
            Array.Reverse(digits);
            int checksum = digits.Select((digit, i) => IsEven(i) ? LuhnOperation(digit) : digit)
                .Sum();
            return checksum % 10 == 0;
        }

        // Because of 0 based indexing, indexes of even elements will be odd.
        private static bool IsEven(int i)
        {
            return i % 2 == 1;
        }

        private static int LuhnOperation(int digit)
        {
            int x = digit * 2;
            if (x > 9)
                x -= 9;
            return x;
        }
    }
}
