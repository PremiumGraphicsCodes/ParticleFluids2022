using System;
using System.Collections.Generic;
using System.Text;

namespace CrystalCSI
{
    public class ParticleSystem
    {
        private int id;

        public void Create()
        {
            CSI.CreateCommand(PG.ParticleSystemCreateCommand.NameLabel);
            //CSI.SetArgFloat(PG.ParticleSystemCreateCommand.PositionsLabel);
            CSI.Execute();
            this.id = CSI.GetResultInt(PG.ParticleSystemCreateCommand.NewIdLabel);
        }

    }
}
