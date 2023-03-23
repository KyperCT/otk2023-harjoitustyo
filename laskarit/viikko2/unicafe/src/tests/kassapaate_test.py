import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(0)
    
    def test_kassa_init_raha_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kassa_init_edullisesti_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kassa_init_maukkaasti_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_kateis_edullisesti_kun_riittaa_kassa_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_kateis_maukkaasti_kun_riittaa_kassa_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_kateis_edullisesti_kun_riittaa_myydyt_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kateis_maukkaasti_kun_riittaa_myydyt_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)
        
    def test_kateis_edullisesti_kun_riittaa_vaihtoraha_oikein(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)
    
    def test_kateis_maukkaasti_kun_riittaa_vaihtoraha_oikein(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto, 100)

    def test_kateis_edullisesti_kun_ei_riita_kassa_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kateis_maukkaasti_kun_ei_riita_kassa_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kateis_edullisesti_kun_ei_riita_myydyt_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_kateis_maukkaasti_kun_ei_riita_myydyt_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)
        
    def test_kateis_edullisesti_kun_ei_riita_vaihtoraha_oikein(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihto, 100)
    
    def test_kateis_maukkaasti_kun_ei_riita_vaihtoraha_oikein(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihto, 200)
    
    def test_kortti_edullisesti_kun_riittaa_kassa_ei_kasva(self):
        self.kortti.lataa_rahaa(10000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortti_maukkaasti_kun_riittaa_kassa_ei_kasva(self):
        self.kortti.lataa_rahaa(10000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortti_edullisesti_kun_riittaa_myydyt_kasvaa(self):
        self.kortti.lataa_rahaa(10000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kortti_maukkaasti_kun_riittaa_myydyt_kasvaa(self):
        self.kortti.lataa_rahaa(10000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
        
    def test_kortti_edullisesti_kun_riittaa_true(self):
        self.kortti.lataa_rahaa(10000)
        vaihto = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(vaihto, True)
    
    def test_kortti_maukkaasti_kun_riittaa_true(self):
        self.kortti.lataa_rahaa(10000)
        vaihto = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(vaihto, True)

    def test_kortti_edullisesti_kun_ei_riita_kassa_ei_kasva(self):
        self.kortti.lataa_rahaa(100)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortti_maukkaasti_kun_ei_riita_kassa_ei_kasva(self):
        self.kortti.lataa_rahaa(100)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortti_edullisesti_kun_ei_riita_myydyt_ei_kasva(self):
        self.kortti.lataa_rahaa(100)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_kortti_maukkaasti_kun_ei_riita_myydyt_ei_kasva(self):
        self.kortti.lataa_rahaa(100)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
        
    def test_kortti_edullisesti_kun_ei_riita_false(self):
        self.kortti.lataa_rahaa(100)
        vaihto = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(vaihto, False)
    
    def test_kortti_maukkaasti_kun_ei_riita_false(self):
        self.kortti.lataa_rahaa(100)
        vaihto = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(vaihto, False)
    
    def test_kortti_edullisesti_kun_riittaa_kortti_vahenee_oikein(self):
        self.kortti.lataa_rahaa(1000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
    
    def test_kortti_maukkaasti_kun_riittaa_kortti_vahenee_oikein(self):
        self.kortti.lataa_rahaa(1000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_kortti_edullisesti_kun_ei_riita_ei_muutu_raha(self):
        self.kortti.lataa_rahaa(100)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_kortti_maukkaasti_kun_ei_riita_ei_muutu_raha(self):
        self.kortti.lataa_rahaa(100)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_kortti_kassa_lataus_saldo_muuttuu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortti_kassa_lataus_kassaraha_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 101000)
    
    def test_kortti_kassa_lataus_negatiivinen_ei_muuta_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.00 euroa")
    
    def test_kortti_kassa_lataus_negatiivinen_ei_muuta_kassarahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
