using System;
using System.Collections.Generic;
using System.Text;

namespace CrystalCSI
{
    public class Fluid
    {
        private int id;
        private int particleSystemId;
        private float pressureCoe;
        private float viscosityCoe;
        private float particleRadius;

        public int Id { get { return id; } }

        public void Create()
        {
            CSI.CreatePhysicsCommand(PG.FluidSceneCreateCommand.CommandNameLabel);
            CSI.Execute();
            this.id = CSI.GetResultInt(PG.FluidSceneCreateCommand.NewIdLabel);            
        }

        public void Update()
        {
            CSI.CreateCommand(PG.FluidSceneUpdateCommand.CommandNameLabel);
            CSI.SetArgInt(PG.FluidSceneUpdateCommand.IdLabel, this.id);
            CSI.SetArgInt(PG.FluidSceneUpdateCommand.ParticleSystemIdLabel, this.particleSystemId);
            CSI.SetArgFloat(PG.FluidSceneUpdateCommand.StiffnessLabel, this.pressureCoe);
            CSI.SetArgFloat(PG.FluidSceneUpdateCommand.ViscosityLabel, this.viscosityCoe);
            CSI.SetArgFloat(PG.FluidSceneUpdateCommand.ParticleRadiusLabel, this.particleRadius);
        }
    }
}
