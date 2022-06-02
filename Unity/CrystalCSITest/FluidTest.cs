using Microsoft.VisualStudio.TestTools.UnitTesting;
using CrystalCSI;

namespace CrystalCSITest
{
    [TestClass]
    public class FluidTest
    {
        [TestMethod]
        public void TestMethod1()
        {
            var fluid = new Fluid();
            fluid.Create();
            Assert.AreEqual(1, fluid.Id);
        }
    }
}
