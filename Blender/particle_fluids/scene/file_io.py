from scene.scene_labels import TXTFileImportCommand, TXTFileExportCommand, STLFileImportCommand, STLFileExportCommand, PCDFileImportCommand, PLYFileExportCommand
from scene.scene import *
import CrystalPLI

class FileIO :
    def import_txt(scene, particle_system_id, file_path) :
        create_scene_command(TXTFileImportCommand.CommandNameLabel)
        set_arg_int(TXTFileImportCommand.IdLabel, particle_system_id)
        set_arg_string(TXTFileImportCommand.FilePathLabel, file_path)
        is_ok = execute_command(scene.world)
        return is_ok

    def export_txt(scene, particle_system_ids, file_path) :
        create_scene_command(TXTFileExportCommand.CommandNameLabel)
        set_arg_int_vector(TXTFileExportCommand.IdsLabel, particle_system_ids)
        set_arg_string(TXTFileExportCommand.FilePathLabel, file_path)
        is_ok = execute_command(scene.world)
        return is_ok

    def import_pcd(scene, particle_system_id, file_path) :
        create_scene_command(PCDFileImportCommand.CommandNameLabel)
        set_arg_int(PCDFileImportCommand.ParticleSystemIdLabel, particle_system_id)
        set_arg_string(PCDFileImportCommand.FilePathLabel, file_path)
        is_ok = execute_command(scene.world)
        return is_ok

    def import_stl(scene, triangle_mesh_id, file_path) :
        create_scene_command(STLFileImportCommand.CommandNameLabel)
        set_arg_int(STLFileImportCommand.TriangleMeshIdLabel, triangle_mesh_id)
        set_arg_string(STLFileImportCommand.FilePathLabel, file_path)
        is_ok = execute_command(scene.world)
        return is_ok

    def export_stl(scene, triangle_mesh_id, file_path) :
        create_scene_command(STLFileExportCommand.CommandNameLabel)
        set_arg_bool(STLFileExportCommand.IsBinaryLabel, True)
        set_arg_int_vector(STLFileExportCommand.IdsLabel, triangle_mesh_id)
        set_arg_string(STLFileExportCommand.FilePathLabel, file_path)
        is_ok = execute_command(scene.world)
        return is_ok