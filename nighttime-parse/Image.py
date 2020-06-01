import rasterio as rio
import numpy as np
from PIL import Image

class Image:

    # @param: countyList is a list of counties (strings)
    # @param: latLongHash is the hash table mapping counties to lat/lon
    # @param: preMigrImgFilePath is the filepath for the pre-migration image
    # @param: postMicrImgFIlePath is the filepath for the post-migration image
    def __init__(self, countyList, latLongHash, preMigrImgFilepath, postMigrImgFilepath):
        self.nightHash = self.fillHash(countyList, latLongHash)
        self.preMigrImgFilepath = preMigrImgFilepath
        self.postMigrImgFilepath = postMigrImgFilepath
        self.originX = self.getImgOrigin().left
        self.originY = self.getImgOrigin().top
        self.countyList = countyList
        self.latLongHash = latLongHash

    # returns object containing image bounding box
    def getImgOrigin():
        with rio.open(preMigrImgFilepath) as preMigrImg:
            self.originX = preMigrImg.bounds.left
            self.originY = preMigrImg.bounds.top
            return preMigrImg.bounds

    # @param: lat, lon are the coordinates to be converted
    def convertToLocal(latLonTuple):
        return (latLonTuple[1] - self.originX, latLonTuple[0] - self.originY)

    # @param: pre is the preMigration image
    # @param: post is the postMigration image
    # @param: latLon is
    def calcPPDChange(pre, post, coord):
        x = coord[0]
        y = coord[1]
        PPDChange = abs(post.getpixel(x, y) - pre.getpixel(x, y))/pre.getpixel(x, y)
        return PPDChange

    # @param: countyList is a list of counties
    # @param: latLongHash is a hash table containing key (county) and value (struct of lat long) pairs
    def fillHash(countyList, latLongHash):
        # open tif files
        preMigrImg = Image.open(self.preMigrImgFilepath)
        postMigrImg = Image.open(self.postMigrImgFilepath)
        for county in countyList:
            countyLatLon = latLongHash[county] # get lat & lon of county
            countyCoord = convertToLocal(countyLatLon) # convert to image coordinates

            # add key (county) / value (percent pop density change) to hash
            self.nightHash[county] = calcPPDChange(preMigrImg, postMigrImg, countyCoord)
        return self.nightHash