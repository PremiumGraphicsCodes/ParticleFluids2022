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

import threading
import time

import bpy

class Test1():
  def __init__(self):
    self.started = threading.Event()
    self.alive = True

  def __del__(self):
    self.kill()

  def begin(self):
    print("begin")
    self.thread = threading.Thread(target=self.func)
    self.thread.start()
    self.started.set()
    self.alive = True

  def end(self):
    self.started.clear()
    print("\nend")

  def kill(self):
    self.started.set()
    self.alive = False
    self.thread.join()

  def func(self):
    i = 0
    self.started.wait()
    while self.alive:
      i += 1
      print("{}\r".format(i), end="")
      self.started.wait()

test1 = Test1()

class ThreadStartOperator(bpy.types.Operator):
    bl_idname = "pg.threadstartoperator"
    bl_label = "ThreadStart"
    bl_description = "Hello"

    def execute(self, context) :
      test1.begin()
      return {'FINISHED'}

class ThreadPauseOperator(bpy.types.Operator):
    bl_idname = "pg.threadpauseoperator"
    bl_label = "ThreadPause"
    bl_description = "Hello"

    def execute(self, context) :
      test1.end()
      return {'FINISHED'}

class ThreadCancelOperator(bpy.types.Operator):
    bl_idname = "pg.threadrcanceloperator"
    bl_label = "ThreadCancel"
    bl_description = "Hello"

    def execute(self, context) :
      test1.kill()
      return {'FINISHED'}        

class ThreadSamplePanel(bpy.types.Panel):
    bl_label = "ThreadSample"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "PFSolver"
    bl_context = "objectmode"

    def draw(self, context):
        self.layout.operator(ThreadStartOperator.bl_idname,text="Start")
        self.layout.operator(ThreadPauseOperator.bl_idname,text="Pause")
        self.layout.operator(ThreadCancelOperator.bl_idname, text="Cancel")

classes = [
    ThreadStartOperator,
    ThreadPauseOperator,
    ThreadCancelOperator,
    ThreadSamplePanel,
]

class ThreadSampleUI :
    def register():
        for c in classes:
            bpy.utils.register_class(c)

    def unregister():
        for c in classes:
            bpy.utils.unregister_class(c)
