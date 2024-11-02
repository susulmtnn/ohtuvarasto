import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_virheellinen_tilavuus(self):
        self.varasto=Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)

    def test_lisää_negatiivinen(self):
        self.varasto=Varasto(8,8)
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_enemman_kuin_mahtuu(self):
        self.varasto=Varasto(8,8)
        self.varasto.lisaa_varastoon(1)
    
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_alku_saldo_pienempi_kuin_0(self):
        self.varasto=Varasto(8,-1)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_voi_ottaa_negatiivista(self):
        #self.varasto=Varasto(8,1)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-1),0)

    def test_ota_kaikki(self):
        self.varasto=Varasto(8,8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10),8)

    def test_testaa__str__(self):
        varasto = Varasto(10, 8)
        vastaus = "saldo = 8, vielä tilaa 2"

        self.assertEqual(str(varasto), vastaus)

