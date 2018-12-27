using System;

namespace cSharpLab
{
    class StringEscapeReplace
    {
        const string testString= @"UNIV. HOSP., LEVEL ""I"", DIR. 10                                  ";
        internal static void Run()
        {
            string output = testString.Replace("\"", "\"\"");
            Console.WriteLine(output);
        }
    }
}
