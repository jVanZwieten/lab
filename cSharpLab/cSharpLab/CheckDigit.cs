using System;

namespace cSharpLab
{
    internal static class CheckDigit
    {
        const decimal sampleDecimal=1.25M;
        const int decimalPlace = 1;

        internal static void Run()
        {
            Console.WriteLine($"Argument: {sampleDecimal} has n={decimalPlace} decimal place: {CheckDecimalPlace(sampleDecimal, decimalPlace)}");
        }

        static bool CheckDecimalPlace(decimal sampleDecimal, int decimalPlace)
        {
            double mod = Math.Pow(10, (1 - decimalPlace));
            decimal modulus = sampleDecimal % (decimal)mod;
            return Math.Abs(modulus) > 0;
        }
    }
}
