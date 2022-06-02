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
from space.voxel_scene import Voxelizer
from scene.file_io import FileIO

import os
import subprocess

from CrystalPLI import World
from scene.scene import Scene

world = World()
scene = Scene(world)

class PARTICLE_FLUIDS_OT_VoxelizerOperator(bpy.types.Operator) :
  bl_idname = "pg.voxelizeroperator"
  bl_label = "MeshToPS"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context) :
      global scene
      divide_length = context.scene.voxelizer_property.divide_length_prop
      export_dir_path = bpy.path.abspath(context.scene.voxelizer_property.export_directory_prop)

      selected_mesh = self.get_selected_mesh(context)
      if selected_mesh == None :
        return {'CANCELLED'}
      mesh = BLTriangleMesh(scene)

      mesh_file_path = os.path.join(export_dir_path, "tmp_fs_mesh.stl")
      ps_file_path = os.path.join(export_dir_path,"tmp_fs_ps.stl")

      mesh.convert_from_polygon_mesh(selected_mesh)
      mesh.mesh.export_stl(mesh_file_path)

      addon_dirpath = os.path.dirname(__file__)
      tool_path = os.path.join(addon_dirpath, '../../vdb/MeshToPSTool')
      params = []
      params.append(tool_path)
      params.append("-i")
      params.append(mesh_file_path)
      params.append("-o")
      params.append(ps_file_path)
      params.append("-l")
      params.append(str(divide_length))          
      
      result = subprocess.run(params, shell=True)
      if result != -1 :
        ps = BLParticleSystem(scene)
        ps.ps.create_empty("")
        ps.convert_to_polygon_mesh("")               

        FileIO.import_pcd(scene, ps.ps.id, ps_file_path)
        ps.update()

      return {'FINISHED'}

  def get_selected_mesh(self, context) :
    for o in bpy.data.objects:
      if o.type == 'MESH' and o.select_get():
        return o
        #return o.to_mesh()
    return None

class VoxelizerPropertyGroup(bpy.types.PropertyGroup):
  divide_length_prop : bpy.props.FloatProperty(
    name="divide_length",
    description="",
    default=1.0,
    min = 0.0
  )
  export_directory_prop : bpy.props.StringProperty(
    name="export_dir",
    description="Path to Directory",
    default="//",
    maxlen=1024,
    subtype='DIR_PATH',
  )

class PARTICLE_FLUIDS_PT_Voxelizer_Panel(bpy.types.Panel) :
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "VDBTools"
  bl_label = "MeshToPS"
  
  def draw(self, context):
    layout = self.layout
    layout.prop(context.scene.voxelizer_property, "divide_length_prop", text="DivideLength")
    layout.prop(context.scene.voxelizer_property, "export_directory_prop", text="ExportDir")
    layout.operator(PARTICLE_FLUIDS_OT_VoxelizerOperator.bl_idname, text="Voxelize")

classes = [
  PARTICLE_FLUIDS_OT_VoxelizerOperator,
  PARTICLE_FLUIDS_PT_Voxelizer_Panel,
  VoxelizerPropertyGroup
]

class PARTICLE_FLUIDS_MeshToPSUI :
  def register():
    for c in classes:
      bpy.utils.register_class(c)
    bpy.types.Scene.voxelizer_property = bpy.props.PointerProperty(type=VoxelizerPropertyGroup)

  def unregister() :
    del bpy.types.Scene.voxelizer_property
    for c in classes:
      bpy.utils.unregister_class(c)
 