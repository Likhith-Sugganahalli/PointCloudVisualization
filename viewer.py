import open3d as o3d
import matplotlib.pyplot as plt


print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("/home/whoknows/Documents/Visualizer/pipeline/living_room_traj2_frei_png/scene/integrated.ply")
o3d.visualization.draw_geometries([pcd])

