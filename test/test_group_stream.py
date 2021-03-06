import sys

from shelljob import proc

# The `sleep` in the bash output should mean one line at a time is read on the python side, since
# it returns the moment it has data, the timeout only applies when no more data is to be found
def test_group():
	sp = proc.Group()
	sp.run( [ "bash", "-c", "for ((i=0;i<10;i=i+1)); do echo $i; sleep 0.25; done" ] )
	while sp.is_pending():
		lines = sp.readlines()
		if len(lines) > 1:
			raise Exception("Expecting 1 line at a time: "+  str(len(lines)))
		for pc, line in lines:
			if not isinstance(line, bytes): # no encoding specified, expectding bytes
				raise Exception("Expecting bytes object")
			sys.stdout.write( "{}:{}\n".format( pc.pid, line ) )
			sys.stdout.flush()

if __name__ == '__main__':
	test_group()
