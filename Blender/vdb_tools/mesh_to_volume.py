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

from venv import create
import bpy
import json

import os
import subprocess

class VDB_TOOLS_OT_MeshToVolumeOperator(bpy.types.Operator) :
  bl_idname = "pg.meshtovolume"
  bl_label = "MeshToVolume"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context) :
      points_file_prop = context.scene.mesh_to_volume_property.points_file_prop
      name = context.scene.mesh_to_volume_property.name_prop
      voxel_size = context.scene.mesh_to_volume_property.voxel_size_prop
      filepath = bpy.path.abspath( points_file_prop )

      print(filepath)

      export_dir_path = os.path.dirname(filepath)
      mesh_file_path = os.path.join(export_dir_path, name + ".stl")
      vdb_file_path = os.path.join(export_dir_path, name + ".vdb")

      bpy.ops.export_mesh.stl(filepath=mesh_file_path, use_selection = True)

      j = self.to_json(mesh_file_path, voxel_size, vdb_file_path)
      print(json.dumps(j, ensure_ascii=False, indent=2))

      json_file_path = os.path.join(export_dir_path, "command.json")
      with open(json_file_path, 'w') as f:
        json.dump(j, f, ensure_ascii=False, indent=4)

      addon_dirpath = os.path.dirname(__file__)
      tool_path = os.path.join(addon_dirpath, 'VDBRunner')
      params = []
      params.append(tool_path)
      params.append(json_file_path)        
      
      result = subprocess.run(params, shell=True)
      if result == -1 : 
        return {'CANCELLED'}

      vol = bpy.data.volumes.new(name =name)
      vol.filepath = vdb_file_path
      ob = bpy.data.objects.new(name, vol)
      bpy.context.collection.objects.link(ob)

      return {'FINISHED'}

  def to_json(self, input_stl_file, voxel_size, output_vdb_file) :
    read_dict = dict()
    read_dict["FilePath"] =  input_stl_file
    read_dict["FileFormat"] = "STL"
    read_dict["Radius"] = 0.5
    read_command = ["VDBSceneFileImport", read_dict]

    convert_dict = dict()
    convert_dict["VDBSceneId"] = 1
    convert_dict["DivideLength"] = voxel_size
    convert_command = ["VDBSceneMeshToVolume", convert_dict]

    write_dict = dict()
    write_dict["FilePath"] = output_vdb_file
    write_dict["VDBSceneId"] = 2
    write_command = ["VDBSceneFileWrite", write_dict]

    data = dict()
    data = [read_command, convert_command, write_command]
    return data

class MeshToVolumePropertyGroup(bpy.types.PropertyGroup):
  voxel_size_prop : bpy.props.IntProperty(
      name="voxelSize",
      description="",
      default=1,
      min=1
  )
  points_file_prop : bpy.props.StringProperty(
    name="points_file",
    description="",
    default="//",
    maxlen=1024,
    subtype='FILE_PATH',
  )
  name_prop : bpy.props.StringProperty(
    name="name",
    description="",
    default="volume",
  )

class VDB_TOOLS_PT_MeshToVolumePanel(bpy.types.Panel) :
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "VDBTools"
  bl_label = "MeshToVolume"
  
  def draw(self, context):
    layout = self.layout
    layout.prop(context.scene.mesh_to_volume_property, "voxel_size_prop", text="VoxelSize")
    layout.prop(context.scene.mesh_to_volume_property, "points_file_prop", text="PointsFile")
    layout.prop(context.scene.mesh_to_volume_property, "name_prop", text="Name")
    layout.operator(VDB_TOOLS_OT_MeshToVolumeOperator.bl_idname, text="ToVolume")

classes = [
  VDB_TOOLS_OT_MeshToVolumeOperator,
  VDB_TOOLS_PT_MeshToVolumePanel,
  MeshToVolumePropertyGroup
]

class VDB_TOOLS_MeshToVolume_UI :
  def register():
    for c in classes:
      bpy.utils.register_class(c)
    bpy.types.Scene.mesh_to_volume_property = bpy.props.PointerProperty(type=MeshToVolumePropertyGroup)

  def unregister() :
    del bpy.types.Scene.mesh_to_volume_property
    for c in classes:
      bpy.utils.unregister_class(c)
 