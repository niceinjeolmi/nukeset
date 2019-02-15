import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("kdy", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
