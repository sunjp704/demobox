
from abc import ABC
import numpy as np

class Mesh(object):

    def __init__(self,points,faces,owners,neighbors) -> None:
        self.points=points  #list
        self.face_points=faces    #list
        self.owners=owners  #list
        self.neighbors=neighbors    #list
        self.num_points=len(self.points)
        self.num_faces=len(self.face_points)
        self.num_interior_faces=len(self.neighbors)
        self.num_boundary_faces=self.num_faces-self.num_interior_faces
        self.num_cells=max(self.owners)
        self.cell_faces=self.__get_cell_faces()
        self.cell_points=self.__get_cell_points()
        self.cell_neighbors=self.__get_cell_neighbors()
        self.point_faces=self.__get_point_faces()
        self.point_cells=self.__get_point_cells()

    def __get_cell_faces(self):
        cell_faces=[None]*self.num_cells
        for face_id in len(self.owners):
            owner=self.owners[face_id]
            if cell_faces[owner] is None:
                cell_faces[owner]=[face_id]
            else:
                cell_faces[owner].append(face_id)

        for face_id in len(self.neighbors):
            neighbor=self.neighbors[face_id]
            if cell_faces[neighbor] is None:
                cell_faces[neighbor]=[face_id]
            else:
                cell_faces[neighbor].append(face_id)
        
        return cell_faces

    def __get_cell_points(self):
        cell_points=[None]*self.num_cells
        for cell_id in range(self.num_cells):
            faces=self.cell_faces[cell_id]
            points=[]
            for face_id in faces:
                points=list(set(self.face_points[face_id]).union(set(points)))
            cell_points[cell_id]=points
        return cell_points

    def __get_cell_neighbors(self):
        cell_neighbors=[None]*self.num_cells
        for face_id in range(self.num_interior_faces):
            owner=self.owners[face_id]
            if cell_neighbors[owner] is None:
                cell_neighbors[owner]=self.neighbors[face_id]
            else:
                cell_neighbors[owner].append(self.neighbors[face_id])
        return cell_neighbors

    def __get_point_faces(self):
        point_faces=[None]*self.num_points
        for face_id in range(self.num_faces):
            points=self.face_points[face_id]
            for p in points:
                if point_faces[p] is None:
                    point_faces[p]=[face_id]
                else:
                    point_faces[p].append(face_id)
        return point_faces

    def __get_point_cells(self):
        point_cells=[None]*self.num_points
        for cell_id in range(self.num_cells):
            points=self.cell_points[cell_id]
            for p in points:
                if point_cells[p] is None:
                    point_cells[p]=[cell_id]
                else:
                    point_cells[p].append(cell_id)
        return point_cells

class Mesh3D(Mesh):
    @classmethod
    def from_openFOAM(self):
        pass

    # def face_area(self):
    #     del_coord=self.points[self.faces[:,0],:]-self.points[self.faces[:,1],:]
    #     face_area=np.sqrt(np.sum(np.square(del_coord),axis=1))
    #     face_centroid=0.5*(np.sum(del_coord,axis=1))
    #     
    #     pass



    # def face_centroid():
# 
    #     pass
    # def volume_element():
    #     pass
    # def centroid_surf():
    #     pass
    # def face_weighting_factor():
    #     pass



    

if __name__=='__main__':
    pass