using System;
using System.IO;

namespace cSharpLab
{
    internal static class WriteTextToFile
    {
        const string outputPath = @"..\..\..\output";
        const string outputFileName = "testOutput.txt";

        internal static void Run()
        {
            string testText = $"{DateTime.Now}: test text.";
            File.AppendAllLines($"{outputPath}\\{outputFileName}", new string[] { testText });
        }
    }
}
