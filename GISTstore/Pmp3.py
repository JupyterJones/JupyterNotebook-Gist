import pyglet
def exit_callback(dt):
    pyglet.app.exit()
    return
def pmp3(mp3File):
    music = pyglet.media.load(mp3File)
    music.play()
    pyglet.clock.schedule_once(exit_callback , music.duration)
    pyglet.app.run()
    return