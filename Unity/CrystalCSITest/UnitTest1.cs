using Microsoft.VisualStudio.TestTools.UnitTesting;
using CrystalCSI;

namespace CrystalCSITest
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            CSI.CreateCommand("Mock");
            CSI.SetArgInt("lhs", 3);
            CSI.SetArgInt("rhs", 2);
            CSI.Execute();
            var result = CSI.GetResultInt("value");
            Assert.AreEqual(5, result);
        }
    }
}
