class RMColorManager(object):
	
	lila = '\033[95m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	bold = '\033[1m'
	underline = '\033[4m'

	def __init__(self):
		pass

	def printWithColor(self, text, color):
		print(color + text + self.end)

	def printError(self, text):
		print(self.red + text + self.end)

	def printBold(self, text):
		print(self.bold + text + self.end)
