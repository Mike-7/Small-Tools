import sys
import zlib

if len(sys.argv) < 2:
	print("No file input.")
	exit()

f = open(sys.argv[1], 'rb')
rawDeflateData = f.read()
f.close()

zobj = zlib.decompressobj(-15)
data = zobj.decompress(rawDeflateData)

f = open(sys.argv[1] + '.dec', 'wb')
f.write(data)
f.close()