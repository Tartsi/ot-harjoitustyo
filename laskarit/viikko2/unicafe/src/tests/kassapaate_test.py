import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def testaa_rahakassassa_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def testaa_edulliset_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaat_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_riittavakateismaara_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_riittamatonkateismaara_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_riittavakateismaara_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_riittamatonkateismaara_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_riittavakorttimaksu_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_riittamatonkorttimaksu_edullinen(self):
        m = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(m), False)
        self.assertEqual(m.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_riittavakorttimaksu_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_riittamatonkorttimaksu_maukas(self):
        m = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(m), False)
        self.assertEqual(m.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahan_lataus_kortille_onnistuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_rahan_lataus_kortille_ei_onnistu(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000), None)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)