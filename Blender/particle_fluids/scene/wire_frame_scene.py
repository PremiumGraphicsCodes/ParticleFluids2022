from scene.scene_labels import *
from scene.scene import *
from CrystalPLI import *

class WireFrameScene :
    def __init__(self, scene) :
        self.scene = scene
        self.id = -1

    def create_empty_wire_frame_scene(self, name, line_width, color, layer) :
        create_scene_command(WireFrameCreateCommand.WireFrameCreateLabel)
        set_arg_string(WireFrameCreateCommand.NameLabel, name)
        set_arg_float(WireFrameCreateCommand.LineWidthLabel, line_width)
        set_arg_color4f(WireFrameCreateCommand.ColorLabel, color)
        execute_command(self.scene.world)
        self.id = get_result_int(WireFrameCreateCommand.NewIdLabel)
     
