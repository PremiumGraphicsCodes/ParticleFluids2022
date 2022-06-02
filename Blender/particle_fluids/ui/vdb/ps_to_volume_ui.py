# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from ui.model.bl_particle_system import BLParticleSystem
from ui.model.bl_triangle_mesh import BLTriangleMesh
from physics.surface_builder import SurfaceBuilder
from CrystalPLI import Vector3dd, Vector3ddVector
from scene.particle_system_scene import ParticleSystemScene
from scene.triangle_mesh_scene import TriangleMeshScene
from scene.file_io import FileIO
from scene.scene import *
from bpy.app.handlers import persistent
import os
import glob
import subprocess
import threading

from CrystalPLI import World
from scene.scene import Scene
from bpy_extras.io_utils import ImportHelper

world = World()
scene = Scene(world)

progress = 0.0

class VDBConverter :
    def __init__(self) :
        self.__running = False
        self.__import_directory = ""
        #self.__export_directory = ""
        self.__current_index = 0
        self.__particle_radius = 1.0
        self.__cell_length = 0.5
        self.__files = []

    def is_running(self) :
        return self.__running

    def set_import_directory(self, dir) :
        self.__import_directory = dir

    #def set_export_directory(self, dir) :
    #    self.__export_directory = dir

    def set_particle_radius(self, rad) :
        self.__particle_radius = rad

    def set_cell_length(self, length) :
        self.__cell_length = length

    def run(self):
        count = len(self.__files)
        start = self.__current_index
        for i in range(start, count) :
            if self.__running :
                file = self.__files[i]
                self.convert(file)
                self.__current_index = i

    def get_progress(self) :
        return self.__current_index / float(len(self.__files))

    def start(self):
        self.__current_index = 0
        self.__running = True
        dir_path = bpy.path.abspath(self.__import_directory)
        path = os.path.join(dir_path, "*.ply")
        self.__files = glob.glob(path)

        thread = threading.Thread(target=self.run)
        thread.start()

    def pause(self):
        self.__running = False

    def stop(self):
        self.__running = False
        self.__current_index = 0
        self.__files = []

    def resume(self):
        self.__running = True
        thread = threading.Thread(target=self.run)
        thread.start()

    def convert(self, file_name) :
        print("converting " + file_name)

        #ps_file_path = os.path.join(self.__import_directory, file_name)
        basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]
        dir_path = bpy.path.abspath(self.__import_directory)
        export_file_path = os.path.join(dir_path, basename_without_ext + ".vdb") #basename_without_ext + ".stl")
        
        addon_dirpath = os.path.dirname(__file__)
        tool_path = os.path.join(addon_dirpath, '../../vdb/VDBTool')

        params = []
        params.append(tool_path)
        params.append("-i")
        params.append(str(file_name))
        params.append("-o")
        params.append(str(export_file_path))
        params.append("-r")
        params.append(str(self.__particle_radius))
        params.append("-v")
        params.append(str(self.__cell_length))
            
        result = subprocess.run(params, shell=True)

        global progress
        progress = self.get_progress()
        #if result != -1 :
            #for o in self.tmp_volumes :
            #    bpy.data.objects.remove(o)                

            #bpy.ops.object.volume_import(filepath=export_file_path, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            #self.tmp_volumes = bpy.context.selected_objects


runner = VDBConverter()

class PARTICLE_FLUIDS_OT_PSToVolumeStartOperator(bpy.types.Operator) :
    bl_idname = "pg.particlesystemsequencemeshingoperator"
    bl_label = "ParticleSystem"
#    bl_description = "Hello"
 
    def execute(self, context) :
        prop = context.scene.ps_to_volumeproperty
        global runner
        runner.set_particle_radius(prop.particle_radius_prop)
        runner.set_cell_length(prop.cell_length_prop)
        runner.set_import_directory(prop.import_directory_prop)
        #runner.set_export_directory(prop.export_directory_prop)
        runner.start()
        return {'FINISHED'}

class PARTICLE_FLUIDS_OT_PSToVolumePauseOperator(bpy.types.Operator) :
    bl_idname = "pg.particlesystemsequencemeshingpauseoperator"
    bl_label = "ParticleSystem"

    def execute(self, context) :
        global runner
        runner.pause()
        return {'FINISHED'}

class PARTICLE_FLUIDS_OT_PSToVolumeResumeOperator(bpy.types.Operator) :
    bl_idname = "pg.particlesystemsequencemeshingresumeoperator"
    bl_label = "ParticleSystem"

    def execute(self, context) :
        global runner
        runner.resume()
        return {'FINISHED'}

class PARTICLE_FLUIDS_OT_PSToVolumeCancelOperator(bpy.types.Operator) :
    bl_idname = "pg.particlesystemsequencemeshingcanceloperator"
    bl_label = "ParticleSystem"

    def execute(self, context) :
        global runner
        runner.stop()
        return {'FINISHED'}

class PARTICLE_FLUIDS_PSToVolumeProperty(bpy.types.PropertyGroup) :        
    particle_radius_prop : bpy.props.FloatProperty(
        name="particle_radius",
        description="ParticleRadius",
        default=1.0,
        min = 0.0,
        max = 100.0,
        )

    cell_length_prop : bpy.props.FloatProperty(
        name="cell_length",
        description="CellLength",
        default=0.5,
        min = 0.0,
        max = 100.0,
    )

    import_directory_prop : bpy.props.StringProperty(
        name="import_directory",
        description="",
        default="//",
        subtype='DIR_PATH')

    #export_directory_prop : bpy.props.StringProperty(
    #    name="export_directory",
    #    description="ExportDirectory",
    #    default="//",
    #    maxlen=1024,
    #    subtype='DIR_PATH',
    #)

        
class PARTICLE_FLUIDS_PT_PSToVolumePanel(bpy.types.Panel):
    bl_label = "PSToVolume"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VDBTools"
    bl_context = "objectmode"

    def draw(self, context):
        prop = context.scene.ps_to_volumeproperty
        self.layout.prop(prop, "particle_radius_prop", text="ParticleRadius")
        self.layout.prop(prop, "cell_length_prop", text="CellLength")
        self.layout.prop(prop, "import_directory_prop", text="ImportDir")
        #self.layout.prop(prop, "export_directory_prop", text="ExportDir")

        self.layout.separator()
        row = self.layout.row(align=False)
        row.operator(PARTICLE_FLUIDS_OT_PSToVolumeStartOperator.bl_idname, text="Start", icon = "PLAY")
        if runner.is_running() :            
            row.operator(PARTICLE_FLUIDS_OT_PSToVolumePauseOperator.bl_idname, text="Pause", icon="PAUSE")
        else :
            row.operator(PARTICLE_FLUIDS_OT_PSToVolumeResumeOperator.bl_idname, text="Resume", icon="PLAY")
        row.operator(PARTICLE_FLUIDS_OT_PSToVolumeCancelOperator.bl_idname, text="Cancel", icon="CANCEL")
        self.layout.separator()

        row = self.layout.row()
        global progress
        row.label(text="Progress")
        row.label(text=str(progress * 100.0))

classes = [
    PARTICLE_FLUIDS_OT_PSToVolumeStartOperator,
    PARTICLE_FLUIDS_OT_PSToVolumePauseOperator,
    PARTICLE_FLUIDS_OT_PSToVolumeResumeOperator,
    PARTICLE_FLUIDS_OT_PSToVolumeCancelOperator,
    PARTICLE_FLUIDS_PT_PSToVolumePanel,
    PARTICLE_FLUIDS_PSToVolumeProperty,
]

class PARTICLE_FLUIDS_PSToVolumeUI :
    def register():
        for c in classes:
            bpy.utils.register_class(c)
        bpy.types.Scene.ps_to_volumeproperty = bpy.props.PointerProperty(type=PARTICLE_FLUIDS_PSToVolumeProperty)

    def unregister():
        for c in classes:
            bpy.utils.unregister_class(c)
        del bpy.types.Scene.ps_to_volumeproperty