from scene.scene_labels import *
from CrystalPLI import *

class Scene :
    def __init__(self, world) :
        self.world = world

    def clear(self, layer) :
        create_scene_command(ClearCommand.CommandNameLabel)
        return execute_command(self.world)

    def delete(self, id, isItem):
        create_scene_command(DeleteCommand.CommandNameLabel)
        set_arg_int(DeleteCommand.IdLabel, id)
        return execute_command(self.world)   

