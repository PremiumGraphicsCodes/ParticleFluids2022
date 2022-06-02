
import PythonLabelFileGenerator
import unittest

from PythonLabelFileGenerator import * 

class TestXXX(unittest.TestCase):
    def test_read(self):
        generator = PythonLabelFileGenerator()
        generator.read("./labels.h")

    def test_read_directory(self):
        generator = PythonLabelFileGenerator()
        generator.read_all_files("*.h")
        generator.write("./labels.py")
        
if __name__ == '__main__':
    unittest.main()