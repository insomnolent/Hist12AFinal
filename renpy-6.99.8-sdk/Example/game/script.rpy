# declared images
image bg black = "black.png"
image bg white = "white.png"
image bg colonialbackground = "NA_landscape.jpg"
image bg office = im.Scale("lawyeroffice.jpg",900,1200)

# Native American chapter
image chief normal = "NA_chief.png"
image chief talk = "NA_chief_talk.png"
image settler normal = "Settler.png"
image settler smile = "Settler_smile.png"
image settler talk = "Settler_talk.png"
#Chinese Immigrant chapter
image chinese normal = "Chinese.png"
image chinese dejected = "Chinese_dejected.png"
image chinese talk = "Chinese_talk.png"
image lawyer normal = "Lawyer.png"
image lawyer talk = "Lawyer_talk.png"
image lawyer look = "Lawyer_lookdown.png"

define n = Character(None,what_slow_cps = 40,show_two_window = True, color="#c8c8ff")
define y = Character('You',what_slow_cps = 40,show_two_window = True)
# Native American chapter
define c = Character('Native American Chief',what_slow_cps = 40,show_two_window = True)
define s = Character('Colonial Settler',what_slow_cps = 40,show_two_window = True)
# Chinese Immigrant chapter
define l = Character('Lawyer',what_slow_cps = 40,show_two_window = True)
define i = Character('Chinese Immigrant',what_slow_cps = 40,show_two_window = True)

# where program starts running
# scene (name of image) will put that image on the background
label start:
 scene bg black
 
# skip to a certain chapter
# delete later before finalizing
 n "What chapter?"
menu:
    "Native Americans":
        jump NA
    "Chinese Immigrants":
        jump CI

# begin Native American chapter

label NA:
 pause(.5)
 n "{i}What is going on?{/i}"
 n "{i}Where am I?{/i}"

 scene bg colonialbackground
 with fade
 
 play music "naturesounds.mp3"

 n "You look around at your surroundings."
 y "{i}Wow, this looks like one of the paintings I saw in my History 12A class. Am I dreaming?{/i}"
 y "{i}But why would I be here, of all places?{/i}"
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
 y "{i}What are they talking about? I can't hear anything...{/i}"
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
y "{i}How disturbing...{/i}"
y "{i}I feel bad for that Native American Chief...I wonder if he'll be okay..."

stop music

n "But before you can dwell on this further, the scene shifts."

scene bg black
with Dissolve(.5)
scene bg white
with Dissolve(.5)
scene bg black
with Dissolve(.5)
scene bg white
with Dissolve(.5)
scene bg black
with Dissolve(.5)

jump CI

# begin Chinese immigrants chapter
label CI:
y "{i}Now what's going on...?{/i}"
play music "office.mp3"

scene bg office
with fade

n "It looks like you are now in an office-like setting."
n "You look around and see someone sitting on a chair in the corner."
y "{i}This has to be a dream...but it seems so realistic!{/i}"

show chinese dejected at left
with dissolve
n "He looks anxious..."
show chinese normal at left
with dissolve
n "...but still hopeful."
show chinese dejected at left
with dissolve
n "You want to ask him some questions, but he probably won't hear you..."
n "You still try to get his attention."
menu:
    "Hi sir, why are you here?":
        jump interrupt
    "Hello, what's your name?":
        jump interrupt
    
label interrupt:
    play sound "door.mp3"
    n "You are interrupted by the door opening."
    n "The door closes and a lawyer walks into the room."
    play sound "footsteps.mp3"
    show lawyer normal at right
    with dissolve
    
play sound "chair.mp3"
n "The lawyer ignores you and sits down on a chair in front of the other man."
show lawyer talk at right
with dissolve
l "Hello, my name is William Hill and I am your attorney."
l "I was hired for you by the Chinese Six Companies. I will do my best to help you."
l "Let’s begin by you telling me your story."
show lawyer normal at right
with dissolve
show chinese talk at left
with dissolve
i "I have been here for 10 years now working on the railroads."
i "I tried to obtain a certificate of residency as conditioned in the Geary Act of 1892, but there was no white witness that could testify of my status."
i "An officer, I don’t remember his name, arrested me because I did not have the certificate."
i "When I tried to explain to him and the judge about my situation, they did not listen."
show chinese dejected at left
with dissolve
i "The judge ordered me to be deported."
show chinese normal at left
with dissolve
show lawyer talk at right
with dissolve
l "So you have been in America for two years without a certificate?"
l "But you have been in America for a total of 10 years, so since 1884?"
show lawyer normal at right
with dissolve
n "The Chinese immigrant nods his head."
show chinese talk at left
with dissolve
i "Yes."
show chinese normal at left
with dissolve
show lawyer look at right
with dissolve
l "What is the name of the railroad company you worked for?"
show lawyer normal at right
with dissolve   
show chinese talk at left
with dissolve
i "I worked for the California and Nevada Railroad."
show chinese normal at left
with dissolve
show lawyer look at right
with dissolve
l "Why were you unable to obtain a certificate?"
show lawyer normal at right
with dissolve
show chinese talk at left
with dissolve
i "There were hundreds of Chinese people like me working on the tracks."
i "We did as we were told and never saw or talk to our employer unless if one of us had made a mistake or if we needed to work faster."
i "If I never interacted with my employer, the how could he be my witness?"
show chinese normal at left
with dissolve    
n "The lawyer scribbles some notes down on his paper. He sighs."
show lawyer talk at right
with dissolve
l "I am sorry, but I can do nothing for you at this moment."
l "As established by the case of Fong Yue Ting v. U.S., deportation is not a punishment for a crime."
l "You are not unlawfully residing in America, but your inability to obtain a certificate is merely an administrative mistake."
l "They are fixing that mistake by sending you home. This is what the Supreme Court has said and that is the precedent."
show lawyer normal at right
with dissolve
n "Angered, you try to interject."
y "{i}That's not fair! He should not be deported! It's not even his fault!{/i}"
n "The Chinese immigrant begins to lose his composure."
show chinese talk at left
with dissolve
i "Is there really nothing you can do?"
show chinese normal at left
with dissolve
show lawyer look at right
with dissolve
l "Yes, I'm afraid so."
show lawyer normal at right
with dissolve
show chinese talk at left
with dissolve
i "Then I am sorry to waste your time. Thank you for trying to help."
show chinese normal at left
with dissolve
play sound "chair.mp3"
n "The lawyer leaves with his head bowed low."
play sound "footsteps.mp3"
n "You wish you could go stop the lawyer from leaving. But before you could move, the scene shifts again."

stop sound
stop music

scene bg black
with Dissolve(.5)
scene bg white
with Dissolve(.5)
scene bg black
with Dissolve(.5)
scene bg white
with Dissolve(.5)
scene bg black
with Dissolve(.5)

