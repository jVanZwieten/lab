using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cSharpLab
{
    enum Permission
    {
        Read,
        Write
    }

    static class EnumComparison
    {
        internal static void Run()
        {
            Permission? nullPermission = null;
            Permission? readPermission = Permission.Read;
            Permission? writePermission = Permission.Write;

            Console.WriteLine(nullPermission < Permission.Write);
        }
    }
}
