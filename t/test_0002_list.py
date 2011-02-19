import unittest
import tempfile
import todo
import commands
import pdb

class TestList(unittest.TestCase):
    # setupall, teardownall
    def setUp(self):
        self.testfile = tempfile.NamedTemporaryFile()
        self.testfilename = self.testfile.name
        

    def tearDown(self):
        self.testfile.close()

    def test_list_none_noeol(self):
        start_todotxt = ''
        end_output = ''
        
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)

    def test_list_none_eol(self):
        start_todotxt = '\n'
        end_output = ''
        
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)

    def test_list_some(self):
        start_todotxt = '''This is a task
take out the milk
buy more trash
refill the video machine'''
        end_output = '''1 This is a task
3 buy more trash
4 refill the video machine
2 take out the milk
'''
        
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)

    def test_list_all(self):

        start_todotxt = '''This is a task +project
take out the milk
buy more trash @store
refill the video machine @store +project
continue to be awesome sauce
Make more awesome sauce
'''

        end_output = '''6 Make more awesome sauce
1 This is a task +project
3 buy more trash @store
5 continue to be awesome sauce
4 refill the video machine @store +project
2 take out the milk
'''
        
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)

    def test_list_project(self):
        start_todotxt = '''This is a task +project
+something take out the milk
buy more trash +daily
refill the video machine +project
+awesome continue to be awesome sauce
Make more awesome sauce
'''

        end_output = '''5 +awesome continue to be awesome sauce
2 +something take out the milk
6 Make more awesome sauce
1 This is a task +project
3 buy more trash +daily
4 refill the video machine +project
'''
        
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)

    def test_list_context(self):
        start_todotxt = '''This is a task @workstuff
take out the milk @store
@store buy more trash
refill the video machine @store
@awesome continue to be awesome sauce
Make more awesome sauce
'''

        end_output = '''5 @awesome continue to be awesome sauce
3 @store buy more trash
6 Make more awesome sauce
1 This is a task @workstuff
4 refill the video machine @store
2 take out the milk @store
'''        
        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)


    def test_list_context_project(self):
        start_todotxt = '''This is a task @workstuff
take out the milk @store
@store buy more trash
+makacrapa do the thing with the stuff
refill the video machine @store
@awesome continue to be awesome sauce
Make more awesome sauce
+awesome it's a place and a project
'''

        end_output = '''8 +awesome it's a place and a project
4 +makacrapa do the thing with the stuff
6 @awesome continue to be awesome sauce
3 @store buy more trash
7 Make more awesome sauce
1 This is a task @workstuff
5 refill the video machine @store
2 take out the milk @store
'''

        self.testfile.write(start_todotxt)
        self.testfile.flush()
        command_line = ['-t', self.testfile.name, 'list']

        testvalue = todo.run(command_line)
#        pdb.set_trace()
        self.assertTrue(end_output == testvalue)
