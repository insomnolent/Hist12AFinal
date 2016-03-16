# declared images
image bg black = "black.png"
image bg white = "white.png"
image bg colonialbackground = "NA_landscape.jpg"
image bg detentioncenter = im.Scale("immigrant.jpg",1000,1200)
image bg buildings = im.Scale("Watts_Riot_1.jpg",900,1100)
image bg crowd = im.Scale("Watts_Riot_2.jpg",900,800)
image bg speaker = im.Scale("Blackspeech.png",800,600)
image bg speaker_lookarm = im.Scale("Blackspeech_lookarm.png",800,600)
image bg speaker_lookright = im.Scale("Blackspeech_lookright.png",800,600)
image bg speaker_talk = im.Scale("Blackspeech_talk.png",800,600)

# Native American chapter
image chief normal = "NA_chief.png"
image chief talk = "NA_chief_talk.png"
image settler normal = "Settler.png"
image settler smile = "Settler_smile.png"
image settler talk = "Settler_talk.png"
# Chinese Immigrant chapter
image chinese normal = "Chinese.png"
image chinese dejected = "Chinese_dejected.png"
image chinese talk = "Chinese_talk.png"
image lawyer normal = "Lawyer.png"
image lawyer talk = "Lawyer_talk.png"
image lawyer look = "Lawyer_lookdown.png"
# Watt's Rebellion
image man normal = "Blackman.png"

define n = Character(None,what_slow_cps = 40,show_two_window = True, color="#c8c8ff")
define y = Character('You',what_slow_cps = 40,show_two_window = True)
# Native American chapter
define c = Character('Native American Chief',what_slow_cps = 40,show_two_window = True)
define s = Character('Colonial Settler',what_slow_cps = 40,show_two_window = True)
# Chinese Immigrant chapter
define l = Character('Lawyer',what_slow_cps = 40,show_two_window = True)
define i = Character('Chinese Immigrant',what_slow_cps = 40,show_two_window = True)
# Watt's Rebellion
define a = Character('Protestor',what_slow_cps = 40,show_two_window = True)
define b = Character('Speaker',what_slow_cps = 40)

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
    "Watt's Rebellion":
        jump WR
    "Classroom":
        jump CR
    "Debugging":
        jump DB

# begin Native American chapter

label NA:
 n "Be sure to turn up your volume! Press space to advance."
 n "If you want to go back a frame, press the 'back' button at the bottom of this screen."
    
 pause(.1)
 y "{i}What is going on?{/i}"
 y "{i}Where am I?{/i}"

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

scene bg black with Dissolve(.5)
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)

jump CI

# begin Chinese immigrants chapter
label CI:
y "{i}Now what's going on...?{/i}"
play music "apollo_justice.mp3" fadein 2.0

scene bg detentioncenter 
with fade

n "It looks like you are now in a detention facility."
n "A sign on the door says that it is an Immigration Detention center."
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
l "Let’s begin with you telling me your story."
show lawyer normal at right with dissolve
show chinese talk at left with dissolve
i "I have been here for 10 years now working on the railroads."
i "I tried to obtain a certificate of residency as conditioned in the Geary Act of 1892, but there was no white witness that could testify of my status."
i "An officer, I don’t remember his name, arrested me because I did not have the certificate."
i "When I tried to explain to him and the judge about my situation, they did not listen."
show chinese dejected at left with dissolve
i "The judge ordered me to be deported."
show chinese normal at left with dissolve
show lawyer talk at right with dissolve
l "So you have been in America for two years without a certificate?"
l "But you have been in America for a total of 10 years, so since 1884?"
show lawyer normal at right with dissolve
n "The Chinese immigrant nods his head."
show chinese talk at left with dissolve
i "Yes."
show chinese normal at left with dissolve
show lawyer look at right with dissolve
l "What is the name of the railroad company you worked for?"
show lawyer normal at right with dissolve   
show chinese talk at left with dissolve
i "I worked for the California and Nevada Railroad."
show chinese normal at left with dissolve
show lawyer look at right with dissolve
l "Why were you unable to obtain a certificate?"
show lawyer normal at right with dissolve
show chinese talk at left with dissolve
i "There were hundreds of Chinese people like me working on the tracks."
i "We did as we were told and never saw or talked to our employer unless one of us had made a mistake or if we needed to work faster."
i "If I never interacted with my employer, then how could he be my witness?"
show chinese normal at left with dissolve    
n "The lawyer scribbles some notes down on his paper. He sighs."
show lawyer talk at right with dissolve
l "I am sorry, but I can do nothing for you at this moment."
l "As established by the case of Fong Yue Ting v. U.S., deportation is not a punishment for a crime."
l "You are not unlawfully residing in America, but your inability to obtain a certificate is merely an administrative mistake."
l "They are fixing that mistake by sending you home. This is what the Supreme Court has said and this is the precedent."
show lawyer normal at right with dissolve
n "Angered, you try to interject."
y "{i}That's not fair! He should not be deported! It's not even his fault!{/i}"
n "The Chinese immigrant begins to lose his composure."
show chinese talk at left with dissolve
i "Is there really nothing you can do?"
show chinese normal at left with dissolve
show lawyer look at right with dissolve
l "Yes, I'm afraid so."
show lawyer normal at right with dissolve
show chinese talk at left with dissolve
i "Then I am sorry to waste your time. Thank you for trying to help."
show chinese normal at left with dissolve

play sound "chair.mp3"
n "The lawyer leaves with his head bowed low."
play sound "footsteps.mp3"
n "You wish you could go stop the lawyer from leaving. But before you could move, the scene shifts again."

stop sound
stop music

scene bg black with fade
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)

jump WR

# third chapter Watt's Rebellion
label WR:

scene bg buildings with fade
play music "ch3sounds/Rebellion.mp3" fadein 1.0

n "The surroundings suddenly changed again."
y "{i}It seems like I’m in early 20th century Los Angeles.{/i}"
n "You see buildings burning. There are fire fighters putting out the flames and trash is all over the street."
y "Hearing a lot of shouts from down the street, you decide to approach where the sounds are coming from."

scene bg blac with fade
scene bg crowd with dissolve
stop music fadeout 1.0
play music "ch3sounds/Crowd_Talking.mp3"

y "{i}Oh my gosh, what’s going on? This is complete chaos!{/i}"
n "You end up joining a crowd of people on the side. Someone is speaking amongst the chaos."
n "You are so preoccupied that you accidentally bump into a tall African American."

show man normal at left

n "He seems startled to see you there."

# $ count = 1
# jump loop

a "What are you doing here? This is no place for a kid like you!"

# label loop:
# if count > 0:
menu:
    "What's going on?":
        jump explain
    "Who are you?":
        jump introduce
    "Who are you calling a kid?!":
        jump angry

label explain:
    a "We're finally protesting against our unfair treatment! Are you gonna join us?"
    jump decide        
label introduce:
    a "That's not important. Are you going to join our cause?"
    jump decide
label angry:
    a "Obviously you! Do you wanna get arrested with all of us that badly?"
    # $ count = 0
    jump apologize
    
label decide:
    menu:
        "Definitely!":
            jump react
        "Uhh no thanks...":
            jump advice
        "I don't know.":
            jump advice

label advice:
a "Well then what are you doing here??"
jump progress
    
label react:
a "Great! As soon as the speaker finishes, we will finally begin the real event!"
jump progress

label apologize:
n "You quickly apologize before you make him more angry."
n "He seems satisfied for now."
a "Well if you don't understand, you should probably shouldn't be here anyway..."
jump progress

label progress:
n "He looks back at the noisy crowd."
a "Now stop trying to distract me, I want to listen to the speaker!"
# add in short shout
n "The crowd shouts again in unison, before the speaker quiets them down."
# potential loud shout noise

scene bg black with fade

scene bg speaker with dissolve
b "Our black families have come to Los Angeles before, believing that we were not targets of prejudice and oppression."
b "Soon our communities grew, as we brought back more families to what we thought was safety."
scene bg speaker_lookright with dissolve
b "But then White LA got scared of us black folk."
scene bg speaker_lookarm with dissolve
b "‘Herds of Blacks were coming!’ they said."
scene bg speaker_talk with dissolve
b "‘Draw the color line before it’s too late,’ they said."
scene bg speaker_lookright with dissolve
b "They wanted to contain and crowd us in our neighborhood of South Central Ave."
b "They removed all other white people into cleaner, nicer neighborhoods, while we were forced into poverty."
b "While our homes became more crowded, we needed ways to get out of our misery"
scene bg speaker_lookarm with dissolve
b "Our ‘Harlem of the West’ began here!"
scene bg speaker_talk with dissolve
b "Prostitution, gambling and saloons. The white man thought our vices were disgusting."
scene bg speaker with dissolve
b "The LAPD patrolled our neighborhood like we were animals in cages."
scene bg speaker_talk with dissolve
b "We were not born as animals!"
scene bg speaker_lookarm with dissolve
b "We were just contained and controlled like animals as if we can’t reason or love each other."
b "How can we live our lives if we are given nothing else--not even the basic human right of life?!"
scene bg speaker with dissolve
b "I love my brothers and sisters...{p}and yes, even the White folks."
scene bg speaker_talk with dissolve
b "What I don’t love--the way police beat and arrest us every day without any sympathy."
scene bg speaker_lookright with dissolve
b "They take away our loved ones for years inside prison walls."
scene bg speaker_talk with dissolve
b "They built more prisons than schools.{p}It is obvious where our children are destined to be." 
scene bg speaker_lookarm with dissolve
b "We need to take back our community for us and for our children."
b "Let’s continue this rebellion and take back what is ours!"
# potential loud sound from crowd

label DB:

scene bg black with fade
scene bg crowd with dissolve

n "You feel just as energized as the other people in the crowd."
y "{i}Wow, that was such an inspiring speech!{/i}"
y "{i}Makes me want to help them in any way possible!{/i}"
y "{i}Except...I still don't know when or where I am...{/i}"
n "The tall African American man turns back to you with a grin."

show man normal at left with dissolve
a "Now do you see why we're gathered here?"
n "He sees your bewildered expression."
a "Since you seem new to this place...and uh still kind of lost..."

$ count = 1
jump loop

label loop:

if count > 0:
    a "Any other questions?"
    menu:
        "What day is it again?":
            a "How could you forget? It's August 12th, 1965."
            jump loop
        "Where is this place?":
            a "This is the Watts of South L.A."
            jump loop
        "So who started this riot?":
            a "First of all, it's a rebellion, not a riot. And it's not just one person."
            a "We are finally rising against the years of oppression and discrimination of our people."
            jump loop
        "Nope, I'm good for now.":
            $ count = 0
            jump loop
else:
    a "Great! I'll be off then!"
    jump progress2
    
label progress2:    
hide man with dissolve
n "He hurries back to join the increasingly loud crowd."
n "As he turns away, you feel the ground begin to spin again."

scene bg black with fade
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)

jump CR

label CR:

scene bg white with fade
scene bg black with Dissolve(2.0)
scene bg white with dissolve
scene bg black with Dissolve(2.0)
    