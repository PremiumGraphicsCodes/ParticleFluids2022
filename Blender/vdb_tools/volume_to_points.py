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

from asyncore import write
import bpy
import json

import os
import subprocess

class VDB_TOOLS_OT_VolumeToPointsOperator(bpy.types.Operator) :
  bl_idname = "pg.volumetopointsoperator"
  bl_label = "VolumeToPoints"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context) :
      #export_dir_path = bpy.path.abspath(context.scene.filter_property.export_directory_prop)
      name = context.scene.volume_to_points_property.name_prop

      selected_volume = self.get_selected_volume(context)
      if selected_volume == None :
        return {'CANCELLED'}

      volume = selected_volume.data
      filepath = bpy.path.abspath( volume.filepath )

      print(filepath)

      export_dir_path = os.path.dirname(filepath)
      points_file_path = os.path.join(export_dir_path, name + ".ply")

      j = self.to_json(filepath, points_file_path)
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

      bpy.ops.import_mesh.ply(filepath=points_file_path)

      #vol = bpy.data.volumes.new(name = name)
      #vol.filepath = export_file_path
      #ob = bpy.data.objects.new(name, vol)
      #bpy.context.collection.objects.link(ob)

      return {'FINISHED'}

  def get_selected_volume(self, context) :
    for o in bpy.data.objects:
      if o.type == 'VOLUME' and o.select_get():
        return o
    return None

  def to_json(self, input_vdb_file, output_ply_file) :
    read_dict = dict()
    read_dict["FilePath"] =  input_vdb_file
    read_dict["Radius"] = 0.5
    read_command = ["VDBSceneFileRead", read_dict]

    convert_dict = dict()
    convert_dict["Radius"] = 1.0
    convert_dict["VDBSceneId"] = 1
    convert_command = ["VDBSceneVolumeToPoints", convert_dict]

    write_dict = dict()
    write_dict["FilePath"] = output_ply_file
    write_dict["FileFormat"] = "PLY"
    write_dict["VDBSceneId"] = 2
    write_command = ["VDBSceneFileExport", write_dict]

    data = dict()
    data = [read_command, convert_command, write_command]
    return data

class VolumeToPointsPropertyGroup(bpy.types.PropertyGroup):
  #width_prop : bpy.props.IntProperty(
  #    name="width",
  #    description="",
  #    default=1,
  #    min=1
  #)
  name_prop : bpy.props.StringProperty(
    name="name",
    description="Name",
    default="points",
  )

class VDB_TOOLS_PT_VolumeToPointsPanel(bpy.types.Panel) :
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "VDBTools"
  bl_label = "VolumeToPoints"
  
  def draw(self, context):
    layout = self.layout
    #layout.prop(context.scene.filter_property, "width_prop", text="Width")
    layout.prop(context.scene.volume_to_points_property, "name_prop", text="Name")
    layout.operator(VDB_TOOLS_OT_VolumeToPointsOperator.bl_idname, text="ToPoints")

classes = [
  VDB_TOOLS_OT_VolumeToPointsOperator,
  VDB_TOOLS_PT_VolumeToPointsPanel,
  VolumeToPointsPropertyGroup
]

class VDB_TOOLS_VolumeToPoints_UI :
  def register():
    for c in classes:
      bpy.utils.register_class(c)
    bpy.types.Scene.volume_to_points_property = bpy.props.PointerProperty(type=VolumeToPointsPropertyGroup)

  def unregister() :
    del bpy.types.Scene.volume_to_points_property
    for c in classes:
      bpy.utils.unregister_class(c)
 