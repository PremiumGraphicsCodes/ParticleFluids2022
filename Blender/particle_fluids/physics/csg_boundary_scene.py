from physics.physics_labels import *
from scene.scene import Scene
from CrystalPLI import *

class CSGBoundaryScene :
    def __init__(self, scene) :
        self.scene = scene
        self.id = 0
        self.name = ""
        self.bounding_box = Box3dd()

    def create(self) :
        create_physics_command(CSGBoundarySceneCreateCommand.CommandNameLabel)
        execute_command(self.scene.world)
        self.id = get_result_int(FluidSceneCreateCommand.NewIdLabel)

    def send(self) :
        create_physics_command(CSGBoundarySceneUpdateCommand.CommandNameLabel)
        set_arg_int(CSGBoundarySceneUpdateCommand.IdLabel, self.id)
        set_arg_string(CSGBoundarySceneUpdateCommand.NameLabel, self.name)
        set_arg_box3dd(CSGBoundarySceneUpdateCommand.BoundingBoxLabel, self.bounding_box)
        is_ok = execute_command(self.scene.world)
        return is_ok
    
    def delete(self) :
        self.scene.delete(self.id, False)
