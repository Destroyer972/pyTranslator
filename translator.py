import xml.etree.ElementTree as ET

class Translator:
	def __init__(self,lang="en", default_lang="en",langs_path="langs"):
		self.default_lang = default_lang
		self.langs_path = langs_path
		self.load_lang(lang)

	def load_lang(self,lang="en"):
		self.root = ET.parse('{}/lang_{}.xml'.format(self.langs_path,lang)).getroot()

	def get_element(self,path):
		if self.root.find(path).text != None:
			return self.root.find(path).text
		else:
			return ET.parse('{}/lang_{}.xml'.format(self.langs_path,self.default_lang)).getroot().find(path).text

	
