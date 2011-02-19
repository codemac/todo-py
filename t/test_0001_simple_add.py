import unittest
import tempfile
import todo
import commands
#import pdb

class TestSimpleAdd(unittest.TestCase):
# setupall, teardownall
    def setUp(self):
        self.testfile = tempfile.NamedTemporaryFile()
        self.testfilename = self.testfile.name
        

    def tearDown(self):
        self.testfile.close()

    def test_add_single_item(self):
        start_todotxt = '''A task of importance
Another task of lesser importance
Let's do this right folks!
'''
        end_todotxt = '''A task of importance
Another task of lesser importance
Let's do this right folks!
The added todo...
'''
        command_line = ['-t', self.testfile.name, 'add', 'The added todo...']
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        todo.run(command_line)
        
        with open(self.testfilename, 'r') as tf:
            testvalue = tf.read()
#        pdb.set_trace()
        self.assertTrue(end_todotxt == testvalue)
