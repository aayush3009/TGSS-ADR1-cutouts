# script to obtain cutouts around using and RA and DEC list
# Aayush Saxena

import pyvo as vo
import subprocess

vo.__file__
url='http://vo.astron.nl/tgssadr/q_fits/imgs/siap.xml'

#######################################
# Input text file should have ID RA DEC
# Edit the name of the input file here:
input_file = "id_ra_dec.txt"
#######################################

query = vo.sia.SIAQuery(url)
query.format = 'image/fits'

#######################################
# Choose the cutout size (degrees)
query.size = 0.1
#######################################

with open(input_file,'r') as te:
    for line in te:
        name=line.split()[0]
        ra=line.split()[1]
        dec=line.split()[2]

        query.pos = (float(ra), float(dec))

        results = query.execute()

        for image in results:
            print "Downloading %s..." %name
            image.cachedataset(filename="%s.fits" %name)

print("All done!")
