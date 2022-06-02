namespace PG {
	public class CSGBoundarySceneCreateCommand
	{
		public const string CommandNameLabel = "CSGBoundarySceneCreate";
		public const string NewIdLabel = "NewId";
	}

	public class CSGBoundarySceneUpdateCommand
	{
		public const string CommandNameLabel = "CSGBoundarySceneUpdate";
		public const string IdLabel = "Id";
		public const string BoundingBoxLabel = "BoundingBox";
		public const string NameLabel = "Name";
	}

	public class EmitterSceneCreateCommand
	{
		public const string CommandNameLabel = "EmitterSceneCreateCommand";
		public const string NewIdLabel = "NewId";
	}

	public class EmitterSceneUpdateCommand
	{
		public const string CommandNameLabel = "EmitterSceneUpdateCommand";
		public const string IdLabel = "Id";
		public const string ParticleSystemIdLabel = "ParticleSystemId";
		public const string ParticleRadiusLabel = "ParticleRadius";
		public const string StiffnessLabel = "Stiffness";
		public const string ViscosityLabel = "Viscosity";
		public const string InitialVelocityLabel = "InitialVelocity";
		public const string DensityLabel = "Density";
		public const string NameLabel = "Name";
		public const string StartStepLabel = "StartStep";
		public const string EndStepLabel = "EndStep";
		public const string IntervalLabel = "Interval";
		public const string TemperatureLabel = "Temperature";
		public const string HeatDiffuseCoeLabel = "HeatDiffuseCoe";
		public const string DragForceCoeLabel = "DragForceCoe";
		public const string DragHeatCoeLabel = "DragHeatCoe";
		public const string LifeLimitLabel = "LifeLimit";
	}

	public class FluidSceneCreateCommand
	{
		public const string CommandNameLabel = "FluidSceneCreateCommand";
		public const string NewIdLabel = "NewId";
	}

	public class FluidSceneToPSCommand
	{
		public const string CommandNameLabel = "FluidSceneToPSCommand";
		public const string FluidIdLabel = "FluidId";
		public const string ParticleSystemIdLabel = "ParticleSystemId";
	}

	public class FluidSceneUpdateCommand
	{
		public const string CommandNameLabel = "FluidSceneUpdateCommand";
		public const string IdLabel = "Id";
		public const string ParticleSystemIdLabel = "ParticleSystemId";
		public const string ParticleRadiusLabel = "ParticleRadius";
		public const string StiffnessLabel = "Stiffness";
		public const string ViscosityLabel = "Viscosity";
		public const string DensityLabel = "Density";
		public const string TemperatureLabel = "Temperature";
		public const string HeatDiffuseCoeLabel = "HeatDiffuseCoe";
		public const string DragForceCoeLabel = "DragForceCoe";
		public const string DragHeatCoeLabel = "DragHeatCoe";
		public const string LifeLimitLabel = "LifeLimit";
		public const string IsBoundary = "IsBoundary";
		public const string NameLabel = "Name";
	}

	public class FluidSimulationCommand
	{
		public const string CommandNameLabel = "FluidSimulationCommand";
		public const string SolverIdLabel = "SolverId";
	}

	public class FluidVolumeExportCommand
	{
		public const string CommandNameLabel = "FluidVolumeExportCommand";
		public const string VolumeIdLabel = "VolumeId";
		public const string FilePathLabel = "FilePath";
	}

	public class FluidVolumeSceneCreateCommand
	{
		public const string CommandNameLabel = "FluidVolumeSceneCreateCommand";
		public const string NewIdLabel = "NewId";
	}

	public class MeshBoundarySceneCreateCommand
	{
		public const string CommandNameLabel = "MeshBoundarySceneCreate";
		public const string NewIdLabel = "NewId";
	}

	public class MeshBoundarySceneUpdateCommand
	{
		public const string CommandNameLabel = "MeshBoundarySceneUpdate";
		public const string IdLabel = "Id";
		public const string MeshIdLabel = "MeshId";
		public const string NameLabel = "Name";
	}

	public class MVPVolumeConvertCommand
	{
		public const string CommandNameLabel = "MVPVolumeConvertCommand";
		public const string VolumeParticleSystemIdLabel = "VolumeParticleSystemId";
		public const string MassParticleSystemIdLabel = "MassParticleSystemId";
		public const string TriangleMeshIdLabel = "TriangleMeshId";
		public const string ParticleRadiusLabel = "ParticleRadius";
		public const string ThresholdLabel = "Threshold";
	}

	public class PhysicsCommandFactory
	{
	}

	public class PhysicsSolverCreateCommand
	{
		public const string CommandNameLabel = "PhysicsSolverCreateCommand";
		public const string NewIdLabel = "NewId";
	}

	public class PhysicsSolverExportCommand
	{
		public const string CommandNameLabel = "PhysicsSolverExportCommand";
		public const string FluidIdsLabel = "FluidIds";
		public const string FilePathLabel = "FilePath";
		public const string DoExportMicroLabel = "DoExportMicro";
		public const string AsBinaryLabel = "AsBinary";
	}

	public class PhysicsSolverUpdateCommand
	{
		public const string CommandNameLabel = "PhysicsSolverUpdateCommand";
		public const string IdLabel = "Id";
		public const string FluidSceneIdsLabel = "FluidSceneIds";
		public const string EmitterSceneIdsLabel = "EmitterSceneIds";
		public const string CSGBoundarySceneIdsLabel = "CSGBoundarySceneIds";
		public const string EffectLengthLabel = "EffectLength";
		public const string ExternalForceLabel = "ExternalForce";
		public const string BuoyancyForceLabel = "BuoyancyForce";
		public const string TimeStepLabel = "TimeStep";
		public const string NameLabel = "Name";
	}

	public class SPHVolumeConvertCommand
	{
		public const string CommandNameLabel = "SPHVolumeConvertCommand";
		public const string ParticleSystemIdLabel = "ParticleSystemId";
		public const string VolumeIdLabel = "VolumeId";
		public const string ParticleRadiusLabel = "ParticleRadius";
		public const string CellLengthLabel = "CellLength";
		public const string ThresholdLabel = "Threshold";
		public const string IsIsotropicLabel = "IsIsotoropic";
	}

}
