import unittest
from mismosCaracteres import mismosCaracteres  # Asegúrate de reemplazar 'my_module' con el nombre de tu módulo

class TestFindAnagrams(unittest.TestCase):
  def test_mismosCaracteres(self):
    self.assertEqual(mismosCaracteres(["amor", "roma", "perro"]), ["amor", "roma"])
    self.assertEqual(mismosCaracteres(["amor", "roma", "perro", "amro"]), ["amor", "roma", "amro"])
    self.assertEqual(mismosCaracteres(["amor", "roma", "perro", "amro", "mora"]), ["amor", "roma", "amro", "mora"])
    self.assertEqual(mismosCaracteres(["amor", "roma", "perro", "amro", "mora", "perrito"]), ["amor", "roma", "amro", "mora"])
    self.assertEqual(mismosCaracteres(["amor", "roma", "perro", "amro", "mora", "perrito", "romaa"]), ["amor", "roma", "amro", "mora"])

if __name__ == '__main__':
  unittest.main()