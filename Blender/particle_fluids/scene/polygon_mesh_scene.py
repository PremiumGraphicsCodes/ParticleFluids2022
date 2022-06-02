from scene.scene_labels import *
from scene.scene import *
from CrystalPLI import *

class PolygonMeshScene :
    def __init__(self, scene) :
        self.scene = scene
        self.id = -1

    def create_empty_polygon_mesh_scene(self, name, layer) :
        create_scene_command(PolygonMeshCreateCommand.CommandNameLabel)
        set_arg_string(PolygonMeshCreateCommand.NameLabel, name)
        is_ok = execute_command(self.scene.world)
        self.id = get_result_int(PolygonMeshCreateCommand.NewIdLabel)
        return is_ok

    def create_polygon_mesh_scene(self, name, positions, normals, texcoords, layer) :
        create_scene_command(PolygonMeshCreateCommand.CommandNameLabel)
        set_arg_string(PolygonMeshCreateCommand.NameLabel, name)
        set_arg_vector3dd_vector(PolygonMeshCreateCommand.PositionsLabel, positions)
        set_arg_vector3dd_vector(PolygonMeshCreateCommand.NormalsLabel, normals)
        is_ok = execute_command(self.scene.world)
        self.id = get_result_int(PolygonMeshCreateCommand.NewIdLabel)
        return is_ok

    def add_verticies(self, positionIds, normalIds, texCoordIds) :
        create_scene_command(PolygonMeshAddVerticesCommand.CommandNameLabel)
        set_arg_int(PolygonMeshAddVerticesCommand.PolygonMeshIdLabel, self.id)
        set_arg_int_vector(PolygonMeshAddVerticesCommand.PositionIdsLabel, positionIds)
        set_arg_int_vector(PolygonMeshAddVerticesCommand.NormalIdsLabel, normalIds)
        set_arg_int_vector(PolygonMeshAddVerticesCommand.TexCoordIdsLabel, texCoordIds)
        is_ok = execute_command(self.world)
        return is_ok

    def add_faces(self, vertexIds) :
        create_scene_command(PolygonMeshAddFacesCommand.CommandNameLabel)
        set_arg_int(PolygonMeshAddFacesCommand.PolygonMeshIdLabel, self.id)
        set_arg_int_vector(PolygonMeshAddFacesCommand.VertexIdsLabel, vertexIds)
        is_ok = execute_command(self.world)
        return is_ok

    def export_obj_file(self, file_path) :
        create_scene_command(OBJFileExportCommand.CommandNameLabel)
        set_arg_int_vector(OBJFileExportCommand.IdsLabel, [id])
        set_arg_string(OBJFileExportCommand.FilePathLabel, file_path)
        is_ok = execute_command(self.scene.world)
        return is_ok

    def import_obj_file(self, file_path) :
        create_scene_command(OBJFileImportCommand.CommandNameLabel)
        set_arg_string(OBJFileImportCommand.FilePathLabel, file_path)
        is_ok = execute_command(self.scene.world)
        self.id = get_result_int(OBJFileImportCommand.NewIdLabel)
        return is_ok


