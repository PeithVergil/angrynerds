from pygame.image import load

def load_rgb(path):
	return load(path).convert()

def load_rgba(path):
	return load(path).convert_alpha()

def load_frames(path, nframes):
	images = []

	for i in xrange(nframes):
		images.append(
			load('%s/%d.png' % (path, i+1)).convert_alpha()
		)

	return images