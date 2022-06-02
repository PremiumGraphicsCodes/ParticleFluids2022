bl_info = {
    "name": "サンプル 222: 何もしないアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "アドオンの有効化と無効化を試すためのサンプル",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}
import bpy
from bpy.props import *

#
# TUTORIAL_OT_SayComment
#
class TUTORIAL_OT_SayComment(bpy.types.Operator):
  bl_idname = "tutorial.saycomment"
  bl_label = "Say Comment"
  bl_options = {'REGISTER', 'UNDO'}
  
  #--- properties ---#
  comment: StringProperty(default = "Hello", options = {'HIDDEN'})

  #--- execute ---#
  def execute(self, context):
    self.report({'INFO'}, self.comment)

    return {'FINISHED'}

#
# TUTORIAL_PT_SamplePanel
#
class TUTORIAL_PT_SamplePanel(bpy.types.Panel):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = "Tutrial"
  bl_label = "PanelTitle"

  #--- draw ---#
  def draw(self, context):
    layout = self.layout
    
    layout.operator(TUTORIAL_OT_SayComment.bl_idname, text = "Say")

#
# register classs
#
classs = [
  TUTORIAL_PT_SamplePanel,
  TUTORIAL_OT_SayComment
]

#
# register
#
def register():
  for c in classs:
    bpy.utils.register_class(c)

#
# unregister()
#    
def unregister():
  for c in classs:
    bpy.utils.register_class(c)

#
# script entry
#    
if __name__ == "__main__":
  register()