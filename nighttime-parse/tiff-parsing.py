# Import necessary packages
import os
import rasterio as rio
import earthpy as et

def main():
    # Get data and set working directory
    et.data.get_data("tiff-files")
    os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
    
    # Define relative path to file
    lidar_dem_path = os.path.join("data", "colorado-flood", "spatial", 
                              "boulder-leehill-rd", "pre-flood", "lidar",
                              "pre_DTM.tif")

    with rio.open(lidar_dem_path) as lidar_dem:
        lidar_dem.bounds

if __name__ == "__main__":
    main()