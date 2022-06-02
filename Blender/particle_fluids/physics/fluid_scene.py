from physics.physics_labels import *
from scene.scene import Scene
from CrystalPLI import *
from scene.scene_labels import *

class FluidScene :
    def __init__(self, scene) :
        self.scene = scene
        self.id = 0
        self.source_particle_system_id = 0
        self.particle_radius = 1.0
        self.density = 1.0
        self.stiffness = 0.25
        self.viscosity = 10.0
        self.is_boundary = False
        self.temperature = 300.0
        self.heat_diffuse = 1.0
        self.drag_force = 0.0
        self.drag_heat = 0.0
        self.lifetime = -1
        self.name = ""

    def create(self) :
        create_physics_command(FluidSceneCreateCommand.CommandNameLabel)
        execute_command(self.scene.world)
        self.id = get_result_int(FluidSceneCreateCommand.NewIdLabel)

    def send(self) :
        create_physics_command(FluidSceneUpdateCommand.CommandNameLabel)
        set_arg_int(FluidSceneUpdateCommand.IdLabel, self.id)
        set_arg_int(FluidSceneUpdateCommand.ParticleSystemIdLabel, self.source_particle_system_id)
        set_arg_float(FluidSceneUpdateCommand.ParticleRadiusLabel, self.particle_radius)
        set_arg_float(FluidSceneUpdateCommand.DensityLabel, self.density)
        set_arg_float(FluidSceneUpdateCommand.StiffnessLabel, self.stiffness)
        set_arg_float(FluidSceneUpdateCommand.ViscosityLabel, self.viscosity)
        set_arg_bool(FluidSceneUpdateCommand.IsBoundary, self.is_boundary)
        set_arg_string(FluidSceneUpdateCommand.NameLabel, self.name)
        set_arg_float(FluidSceneUpdateCommand.TemperatureLabel, self.temperature)
        set_arg_float(FluidSceneUpdateCommand.HeatDiffuseCoeLabel, self.heat_diffuse)
        set_arg_float(FluidSceneUpdateCommand.DragForceCoeLabel, self.drag_force)
        set_arg_float(FluidSceneUpdateCommand.DragHeatCoeLabel, self.drag_heat)
        set_arg_int(FluidSceneUpdateCommand.LifeLimitLabel, self.lifetime)
        is_ok = execute_command(self.scene.world)
        return is_ok

    def get_positions(self) :
        create_scene_command(ParticleSystemGetCommand.CommandNameLabel)
        set_arg_int(ParticleSystemGetCommand.PSIdLabel, self.id)
        is_ok = execute_command(self.scene.world)
        return get_result_vector3dd_vector(ParticleSystemGetCommand.PositionsLabel)
