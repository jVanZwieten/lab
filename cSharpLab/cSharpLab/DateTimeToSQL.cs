using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cSharpLab
{
    static class DateTimeToSQL
    {
        internal static void Run()
        {
            DateTime todayDate = new DateTime(2018, 10, 05);

            for (int i = 0; i < 4; i++)
            {
                DateTime targetDate = todayDate.AddDays(-i);
                string sqlDate = targetDate.ToString("yyyy-MM-dd");

                Console.WriteLine(sqlDate);
            }
        }
    }
}
