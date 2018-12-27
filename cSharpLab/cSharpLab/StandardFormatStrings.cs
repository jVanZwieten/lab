using System;
using System.Collections.Generic;

namespace cSharpLab
{
    static class StandardFormatStrings
    {
        internal static void Run()
        {
            var outputs = prepareOutputs();
            foreach (string output in outputs)
                Console.WriteLine(output);
        }

        private static List<string> prepareOutputs()
        {
            var outputs = new List<string>
            {
                noFraction.ToString(),
                noFraction.ToString("G29"),
                fraction.ToString(),
                fraction.ToString("G29")
            };

            return outputs;
        }

        const decimal noFraction = 2.00M;
        const decimal fraction = 12.125M;
    }
}
