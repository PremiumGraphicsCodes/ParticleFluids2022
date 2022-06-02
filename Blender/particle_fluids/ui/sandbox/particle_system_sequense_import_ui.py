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
from ui.bl_particle_system import BLParticleSystem
from CrystalPLI import Vector3dd, Vector3ddVector
from scene.file_io import FileIO
import os

from CrystalPLI import World
from scene.scene import Scene

world = World()
scene = Scene(world)

class ParticleSystemSequenceImporter :
    def __init__(self) :
        self.ps = None
        self.__running = False

    def build(self):
        global scene
        if self.ps == None :
            self.ps = BLParticleSystem(scene)
            self.ps.ps.create_empty("")
            self.ps.convert_to_polygon_mesh("")               

    def start(self):
        self.__running = True

    def stop(self):
        self.__running = False

    def step(self, frame):
        global scene
        file_path = os.path.join("tmp_txt", "macro" + str(frame) + ".pcd")
        FileIO.import_pcd(scene, self.ps.ps.id, file_path)
        self.ps.update()

    def is_running(self):
        return self.__running

animator = ParticleSystemSequenceImporter()

def on_frame_changed_ps_seq_importer(scene):
    if animator.ps == None :
        return

    if animator.is_running() :
        animator.step(scene.frame_current)

class ParticleSystemSequenceImportOperator(bpy.types.Operator):
    bl_idname = "pg.particlesystemsequenceimportoperator"
    bl_label = "ParticleSystem"
    bl_description = "Hello"

    def execute(self, context) :
        if animator.ps == None :
            animator.build()

        if not animator.is_running() :
            animator.start()
        else :
            animator.stop()
        return {'FINISHED'}

class ParticleSystemSequenceImportPanel(bpy.types.Panel):
    bl_label = "PSSeqImport"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VDBTools"
    bl_context = "objectmode"

    def draw(self, context):
        op = ParticleSystemSequenceImportOperator
        if not animator.is_running():
            self.layout.operator(op.bl_idname,text="Start", icon='PLAY')
        else:
            self.layout.operator(op.bl_idname,text="Stop", icon='PAUSE')

classes = [
  ParticleSystemSequenceImportOperator,
  ParticleSystemSequenceImportPanel,
]

class ParticleSystemSequenceImportUI :
    def register():
        for c in classes:
            bpy.utils.register_class(c)
        #animator.init()
        bpy.app.handlers.frame_change_pre.append(on_frame_changed_ps_seq_importer)

    def unregister():
        for c in classes:
            bpy.utils.unregister_class(c)