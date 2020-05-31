from Image import Image
#import earthpy as et
#from PIL import Image

preMigrImgFilepath = "/Users/gillianminnehan/Documents/Personal_Projects/nasa_space_apps2020/2020-team-repo/nasa-hackathon-2020/nighttime-parse/tif-files/snapshot-2018-09-23T00_00_00Z/snapshot-2018-09-23T00_00_00Z.tif"
postMigrImgFilepath  = "/Users/gillianminnehan/Documents/Personal_Projects/nasa_space_apps2020/2020-team-repo/nasa-hackathon-2020/nighttime-parse/tif-files/snapshot-2018-10-21T00_00_00Z/snapshot-2018-10-21T00_00_00Z.tif"

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
    preMigrImg = Image.open(preMigrImgFilepath)
    preMigrImg.show()
    postMigrImg = Image.open(postMigrImgFilepath)
    postMigrImg.show()
    preMigrImgArr = np.array(preMigrImg)
    postMigrImgArr = np.array(postMigrImg)
    newarr = abs(postMigrImgArr - preMigrImgArr)
    newImg = Image.fromarray(newarr)
    newImg.show()

def main():

    # Define path to tif files
    # preMigrFilename = "snapshot-2018-09-23T00_00_00Z.tif" # TODO pass in as CL args
    # postMigrFilename = "snapshot-2018-10-21T00_00_00Z.tif"
    # basePath = "/Users/gillianminnehan/Documents/Personal_Projects/nasa_space_apps2020/2020-team-repo/nasa-hackathon-2020/nighttime-parse/tif-files/snapshot-2018-10-21T00_00_00Z/"
    countyList = ['Hillsborough']
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