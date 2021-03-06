from shelljob import proc

def test_basic():
	out = proc.call( 'echo 123' )
	assert out == '123\n'

def test_shell():
	out, code = proc.call( ['exit 123'], shell = True, check_exit_code = False )
	assert out == ''
	assert code == 123

def test_return():
	# ensure bad returns are thrown
	try:
		proc.call( ['exit 1'], shell = True )
		assert False
	except proc.BadExitCode:
		pass

def test_timeout():
	try:
		proc.call( 'sleep 10', timeout = 0.1 )
		assert False
	except proc.Timeout:
		pass

def test_not_timeout():
	proc.call( 'sleep 1', timeout = 10 )


def test_encoding():
	output = proc.call( ['cat', 'happy.txt'] )
	assert output == 'Häppy ☺\n' # 'cat' appends a newline
	
	try:
		bad = proc.call( ['cat', 'UTF-8-test.txt'] )
		assert False
	except UnicodeDecodeError:
		assert True
	

if __name__ == '__main__':
	test_encoding()
