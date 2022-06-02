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

from scene.triangle_mesh_scene import *
from scene.polygon_mesh_scene import *
from scene import *

class BLTriangleMesh :
  def __init__(self, scene):
    self.mesh = TriangleMeshScene(scene)
    self.bl_mesh = None
    self.obj = None

  def build(self, name) :
    self.bl_mesh = bpy.data.meshes.new(name = name)
    self.obj = bpy.data.objects.new(name, self.bl_mesh)
    bpy.context.collection.objects.link(self.obj)

  def convert_to_polygon_mesh(self, name) :
    self.bl_mesh = bpy.data.meshes.new(name = name)
    self.obj = bpy.data.objects.new(name, self.bl_mesh)

    coords = []
    faces = []
    next_vertex = 0
    triangles = self.mesh.get_triangles()
    for t in triangles.values :
      coords.append( (t.v0.x, t.v0.y, t.v0.z ))
      coords.append( (t.v1.x, t.v1.y, t.v1.z ))
      coords.append( (t.v2.x, t.v2.y, t.v2.z ))
      faces.append( (next_vertex,next_vertex+1,next_vertex+2) )
      next_vertex += 3

    self.bl_mesh.from_pydata(coords, [], faces)
    
    # Display name and update the mesh
    self.obj.show_name = True
    self.bl_mesh.update()
    bpy.context.collection.objects.link(self.obj)

#      triangle.

#    self.mesh.
#    mesh.from_pydata()

  def convert_from_polygon_mesh(self, obj) :
    self.bl_mesh = obj.to_mesh()
    self.obj = obj
    #meshes = bpy.data.meshes

    matrix_world = self.obj.matrix_world
    print('---matrix_world---')
    print(matrix_world)

    positions = []
    print("num of vertices:", len(self.bl_mesh.vertices))
    for vt in self.bl_mesh.vertices:
      print("vertex index:{0:2} co:{1} normal:{2}".format(vt.index, vt.co, vt.normal))
      vvv = matrix_world @ vt.co
#      vt.transform(matrix_world)
      p = Vector3dd(vvv[0], vvv[1], vvv[2])
      positions.append(p)

    #self.mesh.create_polygon_mesh_scene("", positions, normals, [], 0)
    triangles = Triangle3ddVector()
    for pl in self.bl_mesh.polygons:
#      print("polygon index:{0:2} ".format(pl.index), end="")
#     print("vertices:", end="")
#      for vi in pl.vertices:
#        print("{0:2}, ".format(vi), end="")
      if len(pl.vertices) == 3 :
        v0 = positions[pl.vertices[0]]
        v1 = positions[pl.vertices[1]]
        v2 = positions[pl.vertices[2]]
        triangle1 = Triangle3dd(v0, v1, v2)
        triangles.add(triangle1)    
      elif len(pl.vertices) == 4 :
        v0 = positions[pl.vertices[0]]
        v1 = positions[pl.vertices[1]]
        v2 = positions[pl.vertices[2]]
        v3 = positions[pl.vertices[3]]
        triangle1 = Triangle3dd(v0, v1, v2)
        triangles.add(triangle1)
        triangle2 = Triangle3dd(v0, v2, v3)
        triangles.add(triangle2)
    self.mesh.create(triangles, "")

  def update(self):
      triangles = self.mesh.get_triangles()
      bm = bmesh.new()   # create an empty BMesh
      for t in triangles.values:
        v0 = bm.verts.new([t.v0.x, t.v0.y, t.v0.z])  # add a new vert
        v1 = bm.verts.new([t.v1.x, t.v1.y, t.v1.z])  # add a new vert
        v2 = bm.verts.new([t.v2.x, t.v2.y, t.v2.z])  # add a new vert
        bm.faces.new([v0, v1, v2])
      bm.to_mesh(self.bl_mesh)
      bm.free()
      self.bl_mesh.update()
