#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2 2
2 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 5
1 1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10 998244353
10 9 8 7 5 6 3 4 2 1"""
        output = """185297239"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    