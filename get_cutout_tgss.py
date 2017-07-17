# script to obtain cutouts around using and RA and DEC list
# Aayush Saxena

import pyvo as vo
import subprocess

vo.__file__
url='http://vo.astron.nl/tgssadr/q_fits/imgs/siap.xml'

query = vo.sia.SIAQuery(url)
query.size = 0.1
query.format = 'image/fits'

#######################################
# Edit the name of the input file here:
input_file = "id_ra_dec.txt
#######################################

with open("input_file",'r') as te:
    # Input text file should have ID RA DEC
    for line in te:
        name=line.split()[0]
        ra=line.split()[1]
        dec=line.split()[2]

        query.pos = (float(ra), float(dec))

        results = query.execute()

        for image in results:
            print "Downloading %s..." %name
            image.cachedataset(filename="TGSSimages/%s.fits" %name)

print("All done!")
