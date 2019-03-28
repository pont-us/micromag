#!/usr/bin/env python3

from micromag import HysteresisCurve
import unittest


class TestHysteresisCurve(unittest.TestCase):

    def test_create(self):
        _ = HysteresisCurve("test_data/6m1a-050-hyst-mass-slope")

    def test_parameters(self):
        curve = HysteresisCurve("test_data/6m1a-050-hyst-mass-slope")
        self.assertEqual("+5.130438E-03", curve.params["Coercivity"])
        self.assertEqual("+10.00000E-03", curve.params["Field increment"])

    def test_loop_1(self):
        curve = HysteresisCurve("test_data/6m1a-050-hyst-mass-slope")
        self.assertEqual(3, len(curve.loops))
        self.assertEqual((4, 101), curve.loops[0].shape)
        self.assertEqual((4, 201), curve.loops[1].shape)
        self.assertEqual((4, 201), curve.loops[2].shape)


if __name__ == "__main__":
    unittest.main()
