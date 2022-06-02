from scene.scene_labels import *
from scene.scene import *
from CrystalPLI import *

class ParticleSystemScene :
    def __init__(self, scene) :
        self.scene = scene
        self.id = -1

    def create_empty(self, name) :
        positions = Vector3ddVector()
        color = ColorRGBAf()
        return self.create(positions,name,1.0, color)

    def create(self, positions, name, point_size, color) :
        create_scene_command(ParticleSystemCreateCommand.ParticleSystemAddLabel)
        set_arg_vector3dd_vector(ParticleSystemCreateCommand.PositionsLabel, positions)
        set_arg_string(ParticleSystemCreateCommand.NameLabel, name)
        set_arg_float(ParticleSystemCreateCommand.PointSizeLabel, point_size)
        set_arg_color4f(ParticleSystemCreateCommand.ColorLabel, color)
        is_ok = execute_command(self.scene.world)
        self.id = get_result_int(ParticleSystemCreateCommand.NewIdLabel)
        return is_ok

    def export_pcd_file(self, file_path) :
        create_scene_command(PCDFileExportCommand.CommandNameLabel)
        set_arg_int_vector(PCDFileExportCommand.IdsLabel, [self.id])
        set_arg_string(PCDFileExportCommand.FilePathLabel, file_path)
        is_ok = execute_command(self.scene.world)
        return is_ok

    def import_pcd_file(self, file_path) :
        create_scene_command(PCDFileImportCommand.CommandNameLabel)
        set_arg_string(PCDFileImportCommand.FilePathLabel, file_path)
        is_ok = execute_command(self.scene.world)
        self.id = get_result_int(PCDFileImportCommand.NewIdLabel)
        return is_ok

    def get_positions(self) :
        create_scene_command(ParticleSystemGetCommand.CommandNameLabel)
        set_arg_int(ParticleSystemGetCommand.PSIdLabel, self.id)
        is_ok = execute_command(self.scene.world)
        return get_result_vector3dd_vector(ParticleSystemGetCommand.PositionsLabel)

    def set_positions(self, positions):
        create_scene_command(ParticleSystemSetCommand.CommandNameLabel)
        set_arg_int(ParticleSystemSetCommand.IdLabel, self.id)
        set_arg_vector3dd_vector(ParticleSystemSetCommand.PositionsLabel, positions)
        is_ok = execute_command(self.scene.world)
        return is_ok