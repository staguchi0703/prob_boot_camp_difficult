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
        input = """5
6
8
1
2
3"""
        output = """21"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6
3
1
4
1
5
9"""
        output = """25"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3
5
5
1"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_origin(self):
        input = """5
1
1
3
4
5"""
        output = """13"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()