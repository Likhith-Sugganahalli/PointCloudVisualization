import open3d as o3d
import os
import json

with open("config.json") as file:
	config = json.load(file)

dataset_path = config['path_dataset']
ply_path = os.path.join(dataset_path,'scene/integrated.ply')

print("Load a ply point cloud, print it, and render it")
print(ply_path)
pcd = o3d.io.read_point_cloud(ply_path)
o3d.visualization.draw_geometries([pcd])

