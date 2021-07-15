# PointCloudVisualization

Links:
https://github.com/intel-isl/Open3D

https://storage.googleapis.com/open3d-releases-master/python-wheels/open3d-0.13.0-cp38-cp38-manylinux_2_27_x86_64.whl


https://www.doc.ic.ac.uk/~ahanda/VaFRIC/iclnuim.html
For testing, I specifically used this subset: http://www.doc.ic.ac.uk/~ahanda/living_room_traj2_frei_png.tar.gz

As the python bindings for open3d are only wrappers around a c++ backend, for initial varification of method, i used python.
The python files are all part of the examples given in the open3d git repo.I have uploaded the python files in this repo, but for your verification, the examples folder from the open3d repo can also be used.

Most of the python files are not needed, but to maintain file structure, i have retained all the files for now.

Dependencies:
Opencv tested with 4.5.2 build (also tested without, works fine)
Open3D (installation instructions included)



Installing open3d for python:

Because i faced memory leaks while using the pip version, it is recommended that open3d 13 is installed using the wheel provided,
download the wheel(download the wheel by right-click>save link as) into your working directory and using the command:

(Inside a venv)
python3 -m pip install <the wheel file>


Setup the dataset:
Download the subset from the given link, or choose another subset, i using the TUM compatible (TUM RGB-D Compatible PNGs) version.

place the decompressed dataset in your working directory,ensure that the depth and color images have a 1-1 association.

copy the dataset folder link (working_directory/living_room_traj2_frei_png in my case) and paste it as the path_dataset in the config.json provided.

As the depth scale of the downloaded dataset is 5000, i have already added it into the config.json

cd into python/reconstruction_system and run:

	python3 run_system.py working_directory/PointCloudVisualization/config.json --make --register --refine  --integrate
 

After the process completes, run the viewer.py to obtain a point cloud
