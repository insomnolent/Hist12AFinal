# declared images
image bg black = "black.png"
image bg colonialbackground = "NA_landscape.jpg"

image chief normal = "NA_chief.png"
image chief talk = "NA_chief_talk.png"
image settler normal = "colonizer.png"
image settler smile = "colonizer_smile.png"

define n = Character(None,what_slow_cps = 30,show_two_window = True, color="#c8c8ff")
define c = Character('Native American Chief',what_slow_cps = 30,show_two_window = True)
define s = Character('Colonial Settler',what_slow_cps = 30,show_two_window = True)

# where program starts running
# scene (name of image) will put that image on the background
label start:
 scene bg black
# will pause test before starting to type it
 pause(.5)
 n "What is going on?"
 n "Where am I?"

 scene bg colonialbackground
 with fade

 n "You look around at your surroundings."
 n "It looks like one of the landscapes from the colonial paintings you saw in your History 12A class"
 n "But why would you be here, of all places?"
 n "You hear some noises behind you."
 n "You turn around to see what it is."

 show chief normal at left
 with dissolve

 show chief talk at left

 c "What are you doing here?"
 menu:
  "Oh-uh, I'm just, uh...": 
   jump ignore
  "I don't know! Who are you??": 
   jump ignore
  "That is a good question.":
   jump ignore

label ignore:
 show chief normal at left

 n "He doesn't seem to hear you."
 n "It seems like he's speaking to someone else."
 n "You look towards your right."

 show settler normal at right
 with dissolve

 n "The settler smiled."

 show settler smile at right

 s "Well for the exact same reason as you!"
 s "We both want what's best for our people, after all."
 s "Now, let's start going over the terms of this treaty..."

 show settler normal at right

 n "They begin talking with words and numbers that you can't understand."
 n "What treaty are they talking about?"
 n "You keep trying to hear words you can recognize."
 show chief talk at left
 c "-the last time you claimed to \"govern\" and \"protect\" Native Americans, it resulted in even more chaos!"
 c "I'm not sure if this will be-"

 n "From the way he's talking about it, this sounds like the 1850 Act for the Governance and Protection of Indians!"
 

