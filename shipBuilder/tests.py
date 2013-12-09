import scripts.unit_tests.ingestion as Ingestion
from django.test import TestCase
import os, json

# Create your tests here.
class VehicleDataTests(TestCase):
		def helper_load_json_data(self):
			DATA_PATH = "/Users/john/Documents/SSB/Parsed Data"
			dataFile = "test_vehicle.json"
			try:
			        with open(os.path.join(DATA_PATH, dataFile), 'r') as f:
			                data = json.load(f)
			except:
				data = None
			return data

		def test_find_existing_model(self):
			"""
			Verifies the ability to find a previous model object for the 
			Vehicle
			"""
			data = self.helper_load_json_data()
			self.assertIsNotNone(data)
			v = Ingestion.VehicleData(data)
			self.assertIsNotNone(v)
			existingModel = v.existingModel
			self.assertIsNotNone(existingModel)
		def test_load_json(self):
			"""
			Tests that we can properly load and parse JSON Data
			for a Vehicle object from the game data
			"""
			data = self.helper_load_json_data()
			self.assertIsNotNone(data)
