from physics.physics_labels import SPHVolumeConvertCommand, MVPVolumeConvertCommand
from scene.scene import Scene
from CrystalPLI import *

class SurfaceBuilder :
    def __init__(self, scene) :
        self.scene = scene
    
    def build_isotorpic(self, particle_system_id, volume_id, particle_radius, cell_length) :
        create_physics_command(SPHVolumeConvertCommand.CommandNameLabel)
        set_arg_int(SPHVolumeConvertCommand.ParticleSystemIdLabel, particle_system_id)
        set_arg_int(SPHVolumeConvertCommand.VolumeIdLabel, volume_id)
        set_arg_float(SPHVolumeConvertCommand.ParticleRadiusLabel, particle_radius)
        set_arg_float(SPHVolumeConvertCommand.CellLengthLabel, cell_length)
        set_arg_bool(SPHVolumeConvertCommand.IsIsotropicLabel, True)
        is_ok = execute_command(self.scene.world)
        return is_ok

    #def build_anisotorpic(self, particle_system_id, triangle_mesh_id, particle_radius, cell_length, threshold) :
    #    create_physics_command(SPHSurfaceConstructionCommand.CommandNameLabel)
    #    set_arg_int(SPHSurfaceConstructionCommand.ParticleSystemIdLabel, particle_system_id)
    #    set_arg_int(SPHSurfaceConstructionCommand.TriangleMeshIdLabel, triangle_mesh_id)
    #    set_arg_float(SPHSurfaceConstructionCommand.ParticleRadiusLabel, particle_radius)
    #    set_arg_float(SPHSurfaceConstructionCommand.CellLengthLabel, cell_length)
    #    set_arg_float(SPHSurfaceConstructionCommand.ThresholdLabel, threshold)
    #    set_arg_bool(SPHSurfaceConstructionCommand.IsIsotropicLabel, False)
    #    is_ok = execute_command(self.scene.world)
    #    return is_ok

    #def build_mvp_surface(self, volume_particle_system_id, mass_particle_system_id, triangle_mesh_id, particle_radius, threshold) :
    #    create_physics_command(MVPSurfaceConstructionCommand.CommandNameLabel)
    #    set_arg_int(MVPSurfaceConstructionCommand.VolumeParticleSystemIdLabel, volume_particle_system_id)
    #    set_arg_int(MVPSurfaceConstructionCommand.MassParticleSystemIdLabel, mass_particle_system_id)
    #    set_arg_int(MVPSurfaceConstructionCommand.TriangleMeshIdLabel, triangle_mesh_id)
    #    set_arg_float(MVPSurfaceConstructionCommand.ParticleRadiusLabel, particle_radius)
    #    set_arg_float(MVPSurfaceConstructionCommand.ThresholdLabel, threshold)
    #    is_ok = execute_command(self.scene.world)
    #    return is_ok