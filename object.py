class Marker:
	"""docstring for Marker"""
	def __init__(self, color="Red"):
		self.color = color

class MarkerBox:
	def __init__(self, markers=[]):
		self.markers = markers

	def add_markers(self, marker):
		self.markers.append(marker)

	def remove_marker(self, color):
		for marker in self.markers:
			if marker.color == color:
				markers.remove(marker)
				return marker
		return None

if __name__ == "__main__":
	mest_markers = MarkerBox()
	mest_markers.add_markers(Marker(color="blue"))
	mest_markers.add_markers(Marker(color="black"))
	mest_markers.add_markers(Marker(color="blue"))
	mest_markers.remove_marker(Marker("blue"))

		
		