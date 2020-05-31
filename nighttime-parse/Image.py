import rasterio as rio
from PIL import Image
import numpy as np

# TODO make functions private
class Image:

    # @param: preMigrImgFilePath is the filepath for the pre-migration image
    # @param: postMicrImgFIlePath is the filepath for the post-migration image
    def __init__(self, countyList, latLongHash, preMigrImgFilepath, postMigrImgFilepath):
        self.nightHash = self.fillHash(countyList, latLongHash)
        self.preMigrImgFilepath = preMigrImgFilepath
        self.postMigrImgFilepath = postMigrImgFilepath
        self.originX = self.getImgOrigin().left
        self.originY = self.getImgOrigin().top

    # @param: returns object containing image bounding box
    def getImgOrigin():
        with rio.open(preMigrImgFilepath) as preMigrImg:
            print( "Bounds: " + preMigrImg.bounds)
            return preMigrImg.bounds
    
    # @param: lat, lon are the coordinates to be converted
    def convertToLocal(latLonTuple):
        print("ConvertToLocal: " + (latLonTuple[1] - self.originX, latLonTuple[0] - self.originY))
        return (latLonTuple[1] - self.originX, latLonTuple[0] - self.originY)

    # @param: pre is the preMigration image
    # @param: post is the postMigration image
    # @param: latLon is
    def calcPPDChange(pre, post, coord):
        x = coord[0]
        y = coord[1]
        PPDChange = abs(post.getpixel(x, y) - pre.getpixel(x, y))/pre.getpixel(x, y)
        print('calcPPDChange: ' + PPDChange)
        return PPDChange

    # @param: countyList is a list of counties
    # @param: latLongHash is a hash table containing key (county) and value (struct of lat long) pairs
    def fillHash(countyList, latLongHash):
        # open tif files
        preMigrImg = Image.open(self.preMigrImgFilepath)
        postMigrImg = Image.open(self.postMigrImgFilepath)
        for county in countyList:
            countyLatLon = latLongHash[county] # get lat & lon of county
            countyXY = convertToLocal() # convert to image coordinates

            # add key (county) / value (percent pop density change) to hash
            self.nightHash[county] = calcPPDChange(preMigrImg, postMigrImg, countyCoord)
        return self.nightHash