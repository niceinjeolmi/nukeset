import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("kdy", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
m.addCommand("Draw/slate", "nuke.createNode('slate')")
m.addCommand("Draw/slate_v02", "nuke.createNode('slate_v02')")
m.addCommand("Draw/slate_v03", "nuke.createNode('slate_v03')")
