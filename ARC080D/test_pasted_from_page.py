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
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 2
3
2 1 1"""
        output = """1 1
2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
5
1 2 3 4 5"""
        output = """1 4 4 4 3
2 5 4 5 3
2 5 5 5 3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
1
1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
