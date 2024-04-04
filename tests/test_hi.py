from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsHiTest(TestCase):
    def test_cardinal_for_integers(self):
        self.assertEqual(num2words(199, lang='hi'), 'एक सौ निन्यानवे')
        self.assertEqual(num2words(58, lang='hi'), 'अठावन')
        self.assertEqual(num2words(1214558, lang='hi'),
                         'बारह लाख चौदह हज़ार पांच सौ अठावन')
        self.assertEqual(num2words(521214558, lang='hi'),
                         'बावन करोड़ बारह लाख चौदह हज़ार पांच सौ अठावन')

    def test_cardinal_for_float_number(self):
        self.assertEqual(
          num2words(12.5, lang='hi'), "बारह दशमलव पांच")
        self.assertEqual(
          num2words(12.51, lang='hi'), "बारह दशमलव पांच एक")