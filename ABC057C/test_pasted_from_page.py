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
        input = """49"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000003"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9876543210"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
