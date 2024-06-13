import unittest
from pathlib import Path
import pandas as pd
from test_unitaire.generators.testOperators import generateTestOperators
from addition import add
from multiplication import mult
from main import calculate

# Import des cas de test
testDf = Path("./testOperators.csv")
if not testDf.is_file():
    generateTestOperators(testDf)

dfTests = pd.read_csv(testDf, sep=',', index_col=None)

# Creation de la classe


class TestOperators(unittest.TestCase):
    dfTests = dfTests

    def testAddition(self):
        result = self.dfTests.apply(lambda x: add(x.x, x.y), axis=1)
        reference = self.dfTests.res_add
        diff = self.dfTests.loc[result != reference]
        assertion = diff.shape[0] == 0
        if not assertion:
            diff.to_csv(Path("./results/addition.csv"), sep=',', index=True)
        self.assertTrue(assertion, "La multiplication ne fonctionne pas correctement")

    def testMultiplication(self):
        result = self.dfTests.apply(lambda x: mult(x.x, x.y), axis=1)
        reference = self.dfTests.res_mult
        diff = self.dfTests.loc[result != reference]
        assertion = diff.shape[0] == 0
        if not assertion:
            diff.to_csv(Path("./results/multiplication.csv"), sep=',', index=True)
        self.assertTrue(assertion, "La multiplication ne fonctionne pas correctement")

    def testMain(self):
        result = self.dfTests.apply(lambda x: calculate(x.x, x.y), axis=1)
        reference = self.dfTests.res_calculate
        diff = self.dfTests.loc[result != reference]
        assertion = diff.shape[0] == 0
        if not assertion:
            diff.to_csv(Path("./results/calculate.csv"), sep=',', index=True)
        self.assertTrue(assertion, "Le calculateur ne fonctionne pas correctement")


if __name__ == '__main__':
    unittest.main()
