using System;
using System.Diagnostics;

namespace cSharpLab
{
    internal static class EventLogHelper
    {
        const string exampleSource = "test source2";

        internal static void Example()
        {
            Log("Example logging has begun.");

            var testNumber = 101;
            var testDigit = 1;
            var result = testNumber % Math.Pow(10, testDigit) > 0;

            Log($"{testNumber} {(result ? "has" : "does not have")} significant digits right of the test digit" +
                $"\n Example Logging complete.");
        }

        static void Log(string info, string source)
        {
            if (!EventLog.SourceExists(source))
                EventLog.CreateEventSource(source, "Application");

            using (var log = new EventLog() { Source = source })
                log.WriteEntry(info);
        }

        static void Log(string info)
        {
            EventLog.WriteEntry(".NET Runtime",
                info,
                EventLogEntryType.Information,
                1000);
        }
    }
}
