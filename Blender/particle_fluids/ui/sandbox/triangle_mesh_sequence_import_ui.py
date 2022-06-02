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
from bpy.app.handlers import persistent
from ui.bl_triangle_mesh import BLTriangleMesh
from CrystalPLI import Vector3dd, Vector3ddVector
from scene.file_io import FileIO
import os

from CrystalPLI import World
from scene.scene import Scene

world = World()
scene = Scene(world)

class TriangleMeshSequenceImporter :
    def __init__(self) :
        self.tm = None
        self.__running = False

    def init(self):
        global scene
        if self.tm == None :
            self.tm = BLTriangleMesh(scene)
            self.tm.mesh.create_empty("")
            self.tm.convert_to_polygon_mesh("")               

    def start(self):
        if self.tm == None :
            self.init()

        self.__running = True

    def stop(self):
        self.__running = False

    def step(self, time_step):
        dir_path = bpy.context.scene.tm_seq_import_prop.path

        file_path = os.path.join(dir_path, "mesh" + str(time_step) + ".stl")

        self.tm.mesh.import_stl(file_path)
#        triangles = self.tm.mesh.get_triangles()
        self.tm.update()

    def is_running(self):
        return self.__running

animator = TriangleMeshSequenceImporter()

@persistent
def on_frame_changed_tm_mesh_seq_import(scene):
    if animator.is_running() :
        animator.step(scene.frame_current)

class TriangleMeshSequenceImportOperator(bpy.types.Operator):
    bl_idname = "pg.trianglemeshsequenceimportoperator"
    bl_label = "ParticleSystem"
    bl_description = "Hello"

    def execute(self, context) :
        if not animator.is_running() :
            animator.start()
        else :
            animator.stop()
        return {'FINISHED'}

class TriangleMeshSequenceImportProperties(bpy.types.PropertyGroup):
    path : bpy.props.StringProperty(
        name="",
        description="Path to Directory",
        default="tmp_stl",
        maxlen=1024,
        subtype='DIR_PATH')


class TriangleMeshSequenceImportPanel(bpy.types.Panel):
    bl_label = "TMSeqImport"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VDBTools"
    bl_context = "objectmode"

    def draw(self, context):
        op = TriangleMeshSequenceImportOperator
        if not animator.is_running():
            self.layout.operator(op.bl_idname,text="ImportStart", icon='PLAY')
        else:
            self.layout.operator(op.bl_idname,text="ImportStop", icon='PAUSE')
        layout = self.layout
        col = layout.column(align=True)
        col.prop(context.scene.tm_seq_import_prop, "path", text="")

        #print (scn.my_tool.path)


classes = [
    TriangleMeshSequenceImportProperties,
    TriangleMeshSequenceImportOperator,
    TriangleMeshSequenceImportPanel,
]

class TriangleMeshSequenceImportUI :
    def register():
        for c in classes:
            bpy.utils.register_class(c)
        bpy.types.Scene.tm_seq_import_prop = bpy.props.PointerProperty(type=TriangleMeshSequenceImportProperties)
        bpy.app.handlers.frame_change_pre.append(on_frame_changed_tm_mesh_seq_import)

    def unregister():
        for c in classes:
            bpy.utils.unregister_class(c)
        del bpy.types.Scene.tm_seq_import_prop