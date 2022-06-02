from physics.physics_labels import EmitterSceneCreateCommand, EmitterSceneUpdateCommand
from scene.scene import Scene
from CrystalPLI import *
from scene.scene_labels import ParticleSystemGetCommand

class EmitterScene :
    def __init__(self, scene) :
        self.__scene = scene
        self.__id = 0
        self.__source_particle_system_id = 0
        self.__particle_radius = 1.0
        self.__density = 1.0
        self.__stiffness = 0.25
        self.__viscosity = 10.0
        self.__start_step = 0
        self.__end_step = 100
        self.__interval = 5
        self.__initial_velocity = Vector3df(0,0,0)

        self.__temperature = 300.0
        self.__heat_diffuse = 1.0
        self.__drag_force = 0.0
        self.__drag_heat = 0.0
        self.__lifetime = -1

    def get_id(self) :
        return self.__id

    def set_source_ps_id(self, ps_id) :
        self.__source_particle_system_id = ps_id

    def set_particle_radius(self, particle_radius) :
        self.__particle_radius = particle_radius

    def set_stiffness(self, stiffness) :
        self.__stiffness = stiffness

    def set_viscosity(self, viscosity):
        self.__viscosity = viscosity

    def set_start_step(self, start) :
        self.__start_step = start

    def set_end_step(self, end) :
        self.__end_step = end

    def set_interval(self, interval) :
        self.__interval = interval

    def set_initial_velocity(self, v) :
        self.__initial_velocity = Vector3df(v[0],v[1],v[2])

    def set_temperature(self, v) :
        self.__temperature = v

    def set_heat_diffuse(self, v) :
        self.__heat_diffuse = v

    def set_drag_force(self, v) :
        self.__drag_force = v

    def set_drag_heat(self, v) :
        self.__drag_heat = v

    def set_lifetime(self, v) :
        self.__lifetime = v

    def create(self) :
        create_physics_command(EmitterSceneCreateCommand.CommandNameLabel)
        execute_command(self.__scene.world)
        self.__id = get_result_int(EmitterSceneCreateCommand.NewIdLabel)

    def send(self) :
        create_physics_command(EmitterSceneUpdateCommand.CommandNameLabel)
        set_arg_int(EmitterSceneUpdateCommand.IdLabel, self.__id)
        set_arg_int(EmitterSceneUpdateCommand.ParticleSystemIdLabel, self.__source_particle_system_id)
        set_arg_float(EmitterSceneUpdateCommand.ParticleRadiusLabel, self.__particle_radius)
        set_arg_float(EmitterSceneUpdateCommand.DensityLabel, self.__density)
        set_arg_float(EmitterSceneUpdateCommand.StiffnessLabel, self.__stiffness)
        set_arg_float(EmitterSceneUpdateCommand.ViscosityLabel, self.__viscosity)
        set_arg_int(EmitterSceneUpdateCommand.StartStepLabel, self.__start_step)
        set_arg_int(EmitterSceneUpdateCommand.EndStepLabel, self.__end_step)
        set_arg_int(EmitterSceneUpdateCommand.IntervalLabel, self.__interval)
        set_arg_vector3df(EmitterSceneUpdateCommand.InitialVelocityLabel, self.__initial_velocity)
        set_arg_float(EmitterSceneUpdateCommand.TemperatureLabel, self.__temperature)
        set_arg_float(EmitterSceneUpdateCommand.HeatDiffuseCoeLabel, self.__heat_diffuse)
        set_arg_float(EmitterSceneUpdateCommand.DragForceCoeLabel, self.__drag_force)
        set_arg_float(EmitterSceneUpdateCommand.DragHeatCoeLabel, self.__drag_heat)
        set_arg_int(EmitterSceneUpdateCommand.LifeLimitLabel, self.__lifetime)
        is_ok = execute_command(self.__scene.world)
        return is_ok

    def get_positions(self) :
        create_scene_command(ParticleSystemGetCommand.CommandNameLabel)
        set_arg_int(ParticleSystemGetCommand.PSIdLabel, self.__id)
        is_ok = execute_command(self.__scene.world)
        return get_result_vector3dd_vector(ParticleSystemGetCommand.PositionsLabel)
