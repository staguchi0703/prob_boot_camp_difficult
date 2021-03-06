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
        input = """4
0 1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
0 3 2 1 2 2 1"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
