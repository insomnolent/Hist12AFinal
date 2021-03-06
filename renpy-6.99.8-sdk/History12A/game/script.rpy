﻿# declared images - backgrounds
image bg black = "black.jpg"
image bg white = "white.png"
image bg colonialbackground = "NA_landscape.jpg"
image bg detentioncenter = im.Scale("immigrant.jpg",1000,1200)
image bg buildings = im.Scale("Watts_Riot_1.jpg",900,1100)
image bg crowd = im.Scale("Watts_Riot_2.jpg",900,800)
image bg speaker = im.Scale("Blackspeech.png",800,600)
image bg speaker_lookarm = im.Scale("Blackspeech_lookarm.png",800,600)
image bg speaker_lookright = im.Scale("Blackspeech_lookright.png",800,600)
image bg speaker_talk = im.Scale("Blackspeech_talk.png",800,600)
image bg lecturehall = "ch4/LectureHall.jpg"
image bg lecturehall blur = "ch4/LectureHallblur.png"
image bg credits = "ch4/Credits.png"

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
image man normal = "BlackMan.png"
image man angry = "BlackMan_angry.png"
image man right = "BlackMan_lookright.png"
image man talk = "BlackMan_talk.png"
# Classroom
image prof normal = "ch4/Professor.png"
image prof tilt = "ch4/Professor_happy.png"
image prof tiltopen = "ch4/Professor_happytalk.png"
image prof normalopen = "ch4/Professor_talk.png"

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
# Classroom
define p = Character('Professor',what_slow_cps = 40)

# where program starts running
# scene (name of image) will put that image on the background
label start:
 scene bg black
 $ chapter = 0
 
jump chaptermenu
label chaptermenu:
if chapter > 0:
    n "What chapter? (You can also press 'Control' to skip through dialogue)"
    menu:
        "Native Americans":
            jump NA
        "Chinese Immigrants":
            jump CI
        "Watt's Rebellion":
            jump WR
        "Lecture room":
            jump CR
else:
    jump NA
    
# begin Native American chapter
label NA:
 n "Be sure to turn up your volume! Press space to advance."
 n "If you want to go back a line, press the 'back' button at the bottom of this screen (It's kind of hard to see)"
 n "Thanks for reading, and enjoy!"
 
 pause(2.0)
 y "{i}What is going on?{/i}"
 y "{i}Where am I?{/i}"
 
 play music "naturesounds.mp3"
 scene bg colonialbackground with fade

 n "You look around at your surroundings."
 y "{i}Wow, this looks like one of the paintings I saw in my History 12A class. Am I dreaming?{/i}"
 y "{i}But why would I be here, of all places?{/i}"
 n "You hear some noises near the lake in front of you."
 n "You move forward to investigate."

 show chief normal at left  with dissolve

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

 show settler normal at right with dissolve

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
 show chief normal at left
 show settler talk at right
 s "You are right. The 1850 Act has failed you. However, you have my word that I will stand by this treaty and leave you and your family in peace. I only want your land and nothing more."
 show settler normal at right
 
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
show chief talk at left
c "I'm not sure if this will be the best idea..."
show chief normal at left
show settler talk at right
s "But what other choice do you have? If you don’t sign this treaty, then you risk having your land taken by force!"
n "The chief is in a dilemma. He has to choose between his land, or the peace of his people."
show settler normal at right
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
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)

jump CI

# begin Chinese immigrants chapter
label CI:
y "{i}Now what's going on...?{/i}"
play music "apollo_justice.mp3" fadein 2.0

scene bg detentioncenter with fade

n "It looks like you are now in a detention facility."
n "A sign on the door says that it is an Immigration Detention center."
n "You look around and see someone sitting on a chair in the corner."
y "{i}This has to be a dream...but it seems so realistic!{/i}"

show chinese dejected at left with dissolve
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
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)

jump WR

# third chapter Watt's Rebellion
label WR:

scene bg buildings with fade
play music "ch3/Rebellion.mp3" fadein 1.0

n "The surroundings suddenly changed again."
y "{i}It seems like I’m in early 20th century Los Angeles.{/i}"
y "{i}What's with all this chaos??{/i}"
n "You see buildings burning. There are fire fighters putting out the flames and trash is all over the street."
y "{i}I hope no one gets hurt...{/i}"
n "Hearing a lot of shouts from down the street, you decide to approach where the sounds are coming from."

scene bg black with fade
scene bg crowd with dissolve
stop music fadeout 1.0
play music "ch3/Crowd_Talking.mp3"

y "{i}Oh my gosh, what’s going on? This is complete havoc!{/i}"
n "People are milling around everywhere, pushing and talking and gesturing at the same time."
n "You end up joining a crowd of people on the side. Someone is speaking amongst the chaos."
n "You are so preoccupied that you accidentally bump into a tall African American."

show man normal at left

n "He seems startled to see you there."

show man talk at left with dissolve
a "What are you doing here? This is no place for a kid like you!"
 
menu:
    "What's going on?":
        jump explain
    "Who are you?":
        jump introduce
    "Who are you calling a kid?!":
        jump angry

label explain:
    show man right at left with dissolve
    a "We're finally protesting against our unfair treatment! Are you gonna join us?"
    jump decide        
label introduce:
    show man normal at left with dissolve
    a "That's not important. Are you going to join our cause?"
    jump decide
label angry:
    show man angry at left with dissolve
    a "Obviously you! Do you wanna get arrested with all of us that badly?"
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
show man angry at left with dissolve
a "Well then what are you doing here??"
jump progress
    
label react:
show man talk at left with dissolve
a "Great! As soon as the speaker finishes, we will finally begin the real event!"
jump progress

label apologize:
n "You quickly apologize before you make him more angry."
show man normal at left with dissolve
n "He seems satisfied for now."
show man talk at left with dissolve
a "Well if you don't understand, you probably shouldn't be here anyway..."
jump progress

label progress:
show man right at left with dissolve
n "He looks back at the noisy crowd."
show man talk at left with dissolve
a "Now stop trying to distract me, I want to listen to the speaker!"
play sound "ch3/Crowd_shout.mp3"
n "The crowd shouts again in unison, before the speaker quiets them down."
stop music

scene bg black with fade

scene bg speaker with dissolve
play sound "ch3/Microphone_Feedback.wav"
play music "ch3/inspiring.mp3"
b "Our black families have come to Los Angeles before, believing that we were not targets of prejudice and oppression."
b "Soon our communities grew, as we brought back more families to what we thought was safety."
scene bg speaker_lookright with dissolve
b "But then White LA got scared of us black folk."
scene bg speaker with dissolve
b "‘Herds of Blacks were coming!’ they said."
scene bg speaker_talk with dissolve
b "‘Draw the color line before it’s too late,’ they said."
scene bg speaker_lookright with dissolve
b "They wanted to contain and crowd us in our neighborhood of South Central Ave."
b "They removed all other white people into cleaner, nicer neighborhoods, while we were forced into poverty."
b "While our homes became more crowded, we needed ways to get out of our misery"
scene bg speaker_lookarm with dissolve
b "Our ‘Harlem of the West’ began here!"
scene bg speaker_lookright with dissolve
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
play sound "ch3/Crowd_shout.mp3"
b "Let’s continue this rebellion and take back what is ours!"
stop music
stop sound
# label DB:

scene bg black with fade
scene bg crowd with dissolve

play music "ch3/Speech_murmur.mp3"
n "You feel just as energized as the other people in the crowd."
y "{i}Wow, that was such an inspiring speech!{/i}"
y "{i}Makes me want to help them in any way possible!{/i}"
y "{i}Except...I still don't know when or where I am...{/i}"
n "The tall African American man turns back to you with a grin."
show man normal at left with dissolve
a "Now do you see why we're gathered here?"
n "He sees your bewildered expression."
show man right at left with dissolve
a "Since you seem new to this place...and uh still kind of lost..."

$ count = 1
jump loop

label loop:

if count > 0:
    show man normal at left with dissolve
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
            a "We are all finally rising against the years of oppression and discrimination of our people."
            jump loop
        "Nope, I'm good for now.":
            $ count = 0
            jump loop
else:
    show man right at left with dissolve
    a "Great! I'll be off then!"
    jump progress2
    
label progress2:    
hide man with dissolve
play sound "ch3/Crowd_shout.mp3" fadein 1.0
n "He hurries back to join the increasingly loud crowd."
n "As he turns away, you feel the ground begin to spin again."
stop sound
stop music

scene bg black with fade
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)
scene bg white with Dissolve(.5)
scene bg black with Dissolve(.5)

jump CR
label CR:

scene bg white with Dissolve(0.5)
show bg black with dissolve
y "..........."
scene bg white with Dissolve(0.5)
show bg black with dissolve
y "....................."
scene bg white with Dissolve(0.5)
show bg black with dissolve
y "..............................."
scene bg lecturehall blur with Dissolve(0.5)
scene bg black with dissolve
play music "ch4/Studentmurmur.mp3" fadein 1.0
y "{i}Huh?...wait a second...{/i}"
scene bg lecturehall with Dissolve(3.0)
n "You wake inside a familiar lecture room."
y "!!!"
y "{i}This looks like Franz Hall!{/i}"
n "You realize you were dreaming during lecture!"
n "Luckily, no one noticed you sleeping."
n "Professor Lytle-Hernandez is still in the middle of teaching class."

show prof normal with dissolve
p "...saw the Native Americans, the Chinese Immigrants, and the Watts Rebellion and how all these moments have led to the current situation of mass incarceration in LA."
show prof normalopen with dissolve
p "The Native American narrative showed us the elimination and disappearance of natives."
show prof normal with dissolve
p "The Chinese Immigrants story made it legal to find people within our borders who came to America without proper documentation to be deported and detained."
show prof normalopen with dissolve
p "Finally, the police violence that occurred during the Watts Rebellion and now in our time shows the attack on black livelihood."
p "These are just a few important times in our history that have led to what we now know as mass incarceration in LA."
show prof normal with dissolve
n "The professor looks around the room."
p "So what do we hope for the future?"
y "{i}Hmmm should I raise my hand?{/i}"

menu:
    "Yes, raise hand.":
        n "You raise your hand."
        p "You over there! Yes?"
        jump chosen
    "No, don't raise hand.":
        n "You don't raise your hand."
        n "The professor looks around and sees no one volunteering."
        n "She ends up calling on you."
        p "How about you over there?"
        jump chosen

label chosen:
stop music
play sound "ch4/chairsqueak.mp3"

n "You stand up."
play music "ch4/Classroom.mp3" fadein 2.0

n "Remembering the dream flashbacks and the lessons you learned in History 12A, you start speaking."
y "I hope for a future where we spend more money on schools than on prisons."
y "I hope that there will be more educational programs to help released inmates reenter society more easily." 
y "I hope that criminalization will not be written on to the color of your skin or your economic status."
y "And I hope that we will always be aware of what we learned in this class and not take our privilege for granted."
n "You sit down, oddly satisfied."

show prof tilt with dissolve
n "The professor smiled."
show prof tiltopen with dissolve
p "Those are great hopes for the future. I wish for all of you, after taking this class, that you remember this knowledge and share it with your friends and family."
show prof tilt with dissolve
show prof normal with dissolve
p "The wrongs that exist in our history can and need to be corrected."
show prof normalopen with dissolve
p "It is unfair for large numbers of poor whites, people of color, and others to be incarcerated because they don't fit into societal norms."
show prof normal with dissolve
p "There is no one cause or one solution to this problem, so it is important to analyze it from all perspectives."
show prof normalopen with dissolve
p "Take this knowledge and engage in discussions of the future because the future is in your hands."
show prof tiltopen with dissolve
play sound "ch4/applause.wav" fadein 1.0

scene bg black with Dissolve(3.0)
stop sound
stop music
$ renpy.pause(2.0)
play music "ch4/Ending.mp3"
show bg credits with fade
$ renpy.pause(45.0)

stop music

show bg black with dissolve
$ chapter = 1
n "Do you want to read the story again?"
menu:
    "Yes please!":
        jump chaptermenu
    "No thanks!":
        n "Thanks for reading! Press space to exit."
