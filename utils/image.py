from pygame.image import load

def load_frames(path, nframes):
	images = []

	for i in xrange(nframes):
		images.append(
			load('%s/%d.png' % (path, i+1)).convert_alpha()
		)

	return images