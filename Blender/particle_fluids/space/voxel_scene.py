from space.space_labels import *
from scene.scene import *
from CrystalPLI import *

class GridData :
    def __init__(self) :
        self.res = []
        self.bb = Box3dd()
        self.values = []

class VoxelScene :    
    def __init__(self, scene) :
        self.scene = scene
        self.id = -1

    def create_empty_voxel(self, name) :
        resolution = [2,2,2]
        bb = Box3dd()
        return self.create_voxel(name, resolution, bb)

    def create_voxel(self, name, resolution, boundingBox) :
       create_space_command(VoxelSceneCreateCommand.CommandNameLabel)
       set_arg_int(VoxelSceneCreateCommand.ResolutionXLabel, resolution[0])
       set_arg_int(VoxelSceneCreateCommand.ResolutionYLabel, resolution[1])
       set_arg_int(VoxelSceneCreateCommand.ResolutionZLabel, resolution[2])
       set_arg_box3dd(VoxelSceneCreateCommand.BoundingBoxLabel, boundingBox)
       set_arg_string(VoxelSceneCreateCommand.NameLabel, name)
       is_ok = execute_command(self.scene.world)
       if not is_ok :
           return False
       self.id = get_result_int(VoxelSceneCreateCommand.NewIdLabel);
       return True

    def set_values(self, data):
        create_space_command(VoxelSetCommand.CommandNameLabel)
        set_arg_int(VoxelSetCommand.VoxelIdLabel, self.id)
        set_arg_box3dd(VoxelSetCommand.BoundingBoxLabel, data.bb)
        set_arg_int(VoxelSetCommand.ResolutionXLabel, data.res[0])
        set_arg_int(VoxelSetCommand.ResolutionYLabel, data.res[1])
        set_arg_int(VoxelSetCommand.ResolutionZLabel, data.res[2])
        set_arg_bool_vector(VoxelSetCommand.ValuesLabel, data.values)
        is_ok = execute_command(self.scene.world)
        return is_ok

    def get_values(self):
        value = []
        create_space_command(VoxelGetCommand.CommandNameLabel)
        set_arg_int(VoxelGetCommand.VoxelIdLabel, self.id)
        execute_command(self.scene.world)
        xres = get_result_int(VoxelGetCommand.ResolutionXLabel)
        yres = get_result_int(VoxelGetCommand.ResolutionYLabel)
        zres = get_result_int(VoxelGetCommand.ResolutionZLabel)
        bb = get_result_box3dd(VoxelGetCommand.BoundingBoxLabel)
        values = get_result_bool_vector(VoxelGetCommand.ValuesLabel)
        data = GridData()
        data.res = [xres, yres, zres]
        data.bb = bb;
        data.values = values
        return data

    def convert_to_ps(self, psId) :
        create_space_command(VoxelToPSCommand.CommandNameLabel)
        set_arg_int(VoxelToPSCommand.VoxelIdLabel, self.id)
        set_arg_int(VoxelToPSCommand.PSIdLabel, psId)
        is_ok = execute_command(self.scene.world)
        return is_ok

class Voxelizer :
    def __init__(self, scene) :
        self.scene = scene

    def voxelize(self, mesh_id, voxel_id, divide_length) :
        create_space_command(VoxelizerCommand.CommandNameLabel)
        set_arg_int(VoxelizerCommand.MeshIdLabel, mesh_id)
        set_arg_int(VoxelizerCommand.VoxelIdLabel, voxel_id)
        set_arg_float(VoxelizerCommand.DivideLengthLabel, divide_length)
        is_ok = execute_command(self.scene.world)
        return is_ok
