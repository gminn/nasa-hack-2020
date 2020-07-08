from Image import Image
import numpy as np
import rasterio as rio

#READ: THIS IS A TESTER FILE AND NOT PART OF THE DRIVER. 
# TO RUN, INPUT THE COMPLETE FILE PATH OF THE BELOW FILES:

#TODO: Replace PROJECTPATH with the complete filepath of this project
PROJECTPATH = "/Users/gillianminnehan/Documents/Personal_Projects/nasa_space_apps2020/2020-team-repo/nasa-hackathon-2020/"

preMigrImgFilepath = PROJECTPATH + "nighttime-parse/tif-files/snapshot-2018-09-23T00_00_00Z/snapshot-2018-09-23T00_00_00Z.tif"
postMigrImgFilepath  = PROJECTPATH + "nighttime-parse/tif-files/snapshot-2018-10-21T00_00_00Z/snapshot-2018-10-21T00_00_00Z.tif"

def printMetaData() :
    # open tif files and process using geotiff
    with rio.open(preMigrImgFilepath) as preMigrImg:
        print("---------------")
        bounds = preMigrImg.bounds
        top = bounds.top
        left = bounds.left
        print(preMigrImg.bounds)
        print("---------------")
        with rio.open(postMigrImgFilepath) as postMigrImg:
            if preMigrImg.bounds != postMigrImg.bounds:
                print("Bounds of images not matching.")
                # TODO: Exit program
            print("---------------")
            print(postMigrImg.meta)
            print("---------------")

def printImageArr() :
    preMigrImg = im.open(preMigrImgFilepath)
    preMigrImg.show()
    postMigrImg = im.open(postMigrImgFilepath)
    postMigrImg.show()
    preMigrImgArr = np.array(preMigrImg)
    postMigrImgArr = np.array(postMigrImg)
    newarr = abs(postMigrImgArr - preMigrImgArr)
    newImg = im.fromarray(newarr)
    newImg.show()

def main():

    countyList = ['Hillsborough', 'Orange']
    tuple1 = (12, 15)
    tuple2 = (34, 72)
    list = [tuple1, tuple2]
    latLongHash = {}
    i = 0
    for county in countyList:
        latLongHash[county] = list[i]
        i = i + 1
    myIm = Image(countyList, latLongHash, preMigrImgFilepath, postMigrImgFilepath)
    print('nightHash: ' + myIm.nightHash)

if __name__ == "__main__":
    main()