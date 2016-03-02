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
 n "{i}What is going on?{/i}"
 n "{i}Where am I?{/i}"

 scene bg colonialbackground
 with fade

 n "You look around at your surroundings."
 n "{i}Wow, this looks like one of the paintings I saw in my History 12A class. Am I dreaming?{/i}"
 n "But why would you be here, of all places?"
 n "You hear some noises near the lake in front of you."
 n "You move forward to investigate."

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
 n "He's speaking to someone else."
 n "You look to your right."

 show settler normal at right
 with dissolve

 n "The settler smiles."

 show settler smile at right

 s "I am here to make a deal with you!"
 s "I want your land and I promise to give you an area of land for you and your family to live peacefully."
 s "Here is a treaty for you to review. Please look over the terms of this treaty and let me know if you are unsatisfied."

 show settler normal at right

 n "They begin talking about the terms, but you can’t hear them. You only pick up a few words."
 n "{i}What are they talking about? I can't hear anything...{/i}"
 n "You keep trying to pick out words from their conversation."
 show chief talk at left
 c "You write that you will leave my family in peace, but how can I trust you? The 1850 Act for the Protection and Governance of Indians was established to benefit us, but it only benefitted your people."
 c "You have invaded our land, destroyed our people and eliminated all chances of survival. So tell me, how can I believe that this treaty will stand?"
 s "You are right. The 1850 Act has failed you. However, you have my word that I will stand by this treaty and leave you and your family in peace. I only want your land and nothing more."
 
 n "You try to interject:"
menu: 
 "Don't trust him!":
     jump ignoreagain
 "Are you sure that's the best solution?":
     jump ignoreagain
 "What if he's lying?":
     jump ignoreagain

label ignoreagain:
 n "He still doesn’t seem to hear you."
 c "I'm not sure if this will be the best idea..."
 s "But what other choice do you have? If you don’t sign this treaty, then you risk having your land taken by force!"
 n "The chief is in a dilemma. He has to choose between his land, or the peace of his people."
 c "I still have my doubts, but I will sign this treaty with you." 
 s "You have made a smart decision."
show settler smile at right

n "He smiles again."