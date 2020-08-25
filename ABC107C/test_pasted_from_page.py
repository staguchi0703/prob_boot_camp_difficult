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
        input = """5 3
-30 -10 10 20 50"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
10 20 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8 5
-9 -7 -4 -3 1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
