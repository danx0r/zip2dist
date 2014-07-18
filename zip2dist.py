#
# reqs: 
# apt-get install libsqlite3-dev
# pip install pyzipcode geopy
#
"""
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
    documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
    the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
    TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
    DEALINGS IN THE SOFTWARE.
"""

import pyzipcode
import geopy
from geopy import distance

zipdb = pyzipcode.ZipCodeDatabase()

def zip2latlon(zip):
    z = zipdb[zip]
    return z.latitude, z.longitude

def zip2dist(zip1, zip2):
    p1 = geopy.Point(*zip2latlon(zip1))
    p2 = geopy.Point(*zip2latlon(zip2))
    d = distance.distance(p1, p2).miles
    return d

if __name__=="__main__":
    z1 = 10024 #NYC
    z2 = 94301 #PAlo Alto
    z3 = 94303 #another zip near East Palo Alto
    print "distance twixt NYC and Palo Alto, CA:", zip2dist(z1, z2)
    print "distance twixt Palo Alto and East PA:", zip2dist(z3, z2)