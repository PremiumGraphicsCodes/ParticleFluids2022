from physics.physics_labels import FluidVolumeSceneCreateCommand, FluidVolumeExportCommand
from scene.scene import Scene
from CrystalPLI import *

class VolumeScene :
    def __init__(self, scene) :
        self.scene = scene
        self.id = 0
        self.name = ""

    def create(self) :
        create_physics_command(FluidVolumeSceneCreateCommand.CommandNameLabel)
        execute_command(self.scene.world)
        self.id = get_result_int(FluidVolumeSceneCreateCommand.NewIdLabel)

    def export(self, file_path) :
        create_physics_command(FluidVolumeExportCommand.CommandNameLabel)
        set_arg_int(FluidVolumeExportCommand.VolumeIdLabel, self.id)
        set_arg_string(FluidVolumeExportCommand.FilePathLabel, file_path)
        execute_command(self.scene.world)
