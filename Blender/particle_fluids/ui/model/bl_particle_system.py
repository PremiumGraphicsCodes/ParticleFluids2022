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
import bmesh
import CrystalPLI
import scene

from scene.particle_system_scene import *
from scene import *

class BLParticleSystem :
  def __init__(self, scene):
    self.ps = ParticleSystemScene(scene)

  def convert_to_polygon_mesh(self, ob_name):
      # Create new mesh and a new object
      self.me = bpy.data.meshes.new(name = ob_name + "Mesh")
      ob = bpy.data.objects.new(ob_name, self.me)

      positions = self.ps.get_positions()
      coords = []
      for p in positions.values :
        coords.append( (p.x, p.y, p.z))
      # Make a mesh from a list of vertices/edges/faces
      self.me.from_pydata(coords, [], [])

      # Display name and update the mesh
      ob.show_name = True
      self.me.update()
      bpy.context.collection.objects.link(ob)

  def update(self):
      positions = self.ps.get_positions()
      print(len(positions.values))
      bm = bmesh.new()   # create an empty BMesh
      for p in positions.values:
        bm.verts.new((p.x, p.y, p.z))  # add a new vert
      bm.to_mesh(self.me)
      bm.free()
      self.me.update()

  def update_from_positions(self, positions) :
      bm = bmesh.new()   # create an empty BMesh
      for p in positions.values:
        bm.verts.new((p.x, p.y, p.z))  # add a new vert
      bm.to_mesh(self.me)
      bm.free()
      self.me.update()
