# Exercise 6
from pathlib import Path
from satpy import Scene, find_files_and_readers

exercise = Path("C:/Users/sa-br/Documents/edu/python/exercise-6-Bruenins/")
input_dir  = exercise / "data"
output_dir = exercise / "results"
input_dir.mkdir(parents = True, exist_ok = True)
output_dir.mkdir(parents = True, exist_ok = True)

# 1. Read the Scene that you downloaded from the data directory using SatPy. [2P]
files = find_files_and_readers(base_dir="C:/Users/sa-br/Documents/edu/python/data", reader="seviri_l1b_nc")
scn = Scene(filenames=files)

# 2. Load the composites "natural_color" and "convection" [2P]
scn.load(["natural_color", "convection"])

# 3. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5 
from pyresample.geometry import AreaDefinition

area_id = "Dem. Rep. Kongo"
description = "Dem. Rep. Kongo in Lambert Azimuth Equal Area"
proj_id = "Dem. Rep. Kongo"
proj_dict = {"proj": "laea", "lat_0": -3, "lon_0": 23}

width = 500
height = 500

llx = -15E5
lly = -15E5
urx = 15E5
ury = 15E5

area_extent = (llx,lly,urx,ury)
area_def = AreaDefinition(area_id, proj_id, description, proj_dict, width, height, area_extent)

local_scn = scn.resample(area_def)

# 4. Save both loaded composites of the resampled Scene as simple png images. [2P]
local_scn.save_datasets(writer = "simple_image", 
                        datasets = ["natural_color", "convection"], 
                        filename = "{name}_{start_time:%Y%m%d_%H%M%S}.png", 
                        base_dir = output_dir)