
import unittest
import pandas as pd
import os
from assignment import read_csv_file, read_json_file, read_xml_file

class TestFileReading(unittest.TestCase):
    def setUp(self):
        # Create dummy files for testing
        self.csv_file = 'test.csv'
        self.json_file = 'test.json'
        self.xml_file = 'test.xml'

        pd.DataFrame({'A': [1, 2], 'B': [3, 4]}).to_csv(self.csv_file, index=False)
        pd.DataFrame({'A': [1, 2], 'B': [3, 4]}).to_json(self.json_file)
        with open(self.xml_file, 'w') as f:
            f.write('<root><row><A>1</A><B>3</B></row><row><A>2</A><B>4</B></row></root>')

    def tearDown(self):
        # Remove the dummy files
        os.remove(self.csv_file)
        os.remove(self.json_file)
        os.remove(self.xml_file)

    def test_read_csv_file(self):
        df = read_csv_file(self.csv_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))

    def test_read_json_file(self):
        df = read_json_file(self.json_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))

    def test_read_xml_file(self):
        df = read_xml_file(self.xml_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))

if __name__ == '__main__':
    unittest.main()
