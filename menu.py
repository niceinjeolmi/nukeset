import nuke
import nukescripts
import checkenv
import openfile
import helloworld
import nklibrary
import makewrite
#import openfile_v01

tb = nuke.toolbar("Nodes")
m = tb.addMenu("kdy", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
m.addCommand("Draw/slate", "nuke.createNode('slate')")
m.addCommand("Draw/slate_v02", "nuke.createNode('slate_v02')")
m.addCommand("Draw/slate_v03", "nuke.createNode('slate_v03')")
m.addCommand("Draw/Slate_jonas", "nuke.createNode('Slate_jonas')")

mb = menubar.addMenu("Lazypic")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/lazypic/nuke/issues')")
mb.addCommand("Slack", "nukescripts.start('https://lazypic.slack.com')")
mb.addCommand("Clip Library", "nukescripts.start('https://www.youtube.com/channel/UC0L_YtB4PWSkOwp2m9587MA/playlists?view_as=subscriber')")

mb = menubar.addMenu("kdy")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()", "F6", shortcutContext=2)
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()", "F7", shortcutContext=2)
mb.addCommand("CheckEnv", "reload(checkenv);checkenv.main()")
mb.addCommand("OpenFile", "reload(openfile);openfile.main()", "F8", shortcutContext=2)
mb.addCommand("HelloWorld", "reload(helloworld);helloworld.main()")
mb.addCommand("NkLibrary", "reload(nklibrary);nklibrary.main()")
mb.addCommand("MakeWrite", "reload(makewrite);makewrite.main()", "F10", shortcutContext=2)
#mb.addCommand("OpenFile_v01", "openfile_v01.openfile()", "F9", shortcutContext=2)
