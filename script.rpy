label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ t_name = "Trollface"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "..."
    "a day like any other"
    "i see someone"
    "no..."
    "oh!that's trollface and sayori"
    "sayori is my good childhood friend and trollface came from that old memes."
    "i saved trollface from his epiphany."
    "sooooo...we're friends now!"
    s"heyyyyyyyyy"
    t"wait [player]!"
    show trollface 1c zorder 3 at l22
    t"um....goodmorning,hosna!"
    show sayori 1a zorder 2 at l21
    mc"goodmorning to you too,trollface"
    t 1q"and i waked her up."
    s 5b"ehehehe...."
    "trollface looked at the school and then me."
    t 2i"what are you waiting for,[player]?"
    mc"uhhhh..sorry!let's walk to school"
    hide trollface
    show sayori 3r zorder 2 at t11
    "why sayori isn't talking today?"
    "maybe...she's still tired."
    hide sayori
    show class
    "class ends before i knew it."
    mc"ugh!...I'm not going to late again!"
    show corridor
    "i ran at club."
    show white for one milisecond
    show trollface 1y zorder 1 at h11
    t"ah!"
    "an accident with trollface?"
    t"__"
    t 2t"LOOK AT YOUR_"
    show trollface 1g zorder 1 at hf11
    t"oh it's you [player]?"
    t"sorry for shouting at you."
    hide trollface
    show club
    m"............"
    show trollface 2i zorder 2 at l22
    t"monika?"
    show monika 4n zorder 3 at l21
    m"Oh sorry!i just wanted to write a poam while waiting for you"
    mc"ah no problem!"
    hide trollface
    hide monika
    "..."
    "i feel like that i want to spend all the day with trollface."
    mc"ammmm...trollface?"
    show trollface 1a zorder 1 at f11
    t"yes [player]?."
    mc"what do you think about girls?"
    t 2j"they are great and lovely and im so glad that you joined me in this club."
    t 2q"and still...."
    t 1e"i can't thank you enough for saving me!"
    t 3p"being hated by people in that way was hurtful."
    t 3k"im grateful that you always thought of me."
    mc"um. sorry but can you give me a hug."
    t 1j"i can't say no to your warm hugs...."
    show t_cg1
    mc"and if you close your eyes.."
    mc"hug gets warmer.."
    "owww... he's so cute and hand_some!"
    "it's girls stuff but..."
    mc"I LOVE YOU SOOOOOO MUCH TROLLFACE!"
    "and after that our hug ends"
    hide t_cg1
    scene bg club_day
    show trollface 1e zorder 1 at f11
    t"i love you too."
    "he talks warmly."
    t"im forever grateful for that i have my hero."
    t"..."
    show trollface 2b zorder 1 at h11
    t"you!"
    mc"your really a good friend."
    t 4n"thanks for compliment and everything"
    t"__"
    show trollface 2y zorder 2 at h22
    show monika 3k zorder 3 at l21
    m"time for sharing poems"
    menu:
         mc "Who shoud i share my poem to...?"
         "trollface.":
            call ch0_end_trollface from ch0_end_trollface

    scene bg club_day
    with wipeleft_scene
    m"Okay,everyone!"
    show monika 2a zorder 1 at t11
    m"the club meeting ends!"
    m 2k"how do you feel about your poems?"
    show monika 1j zorder 4 at t44
    show sayori 3r zorder 3 at t43
    s"it felt good!"
    show natsuki 1d zorder 2 at t42
    n"i feel the same too!"
    show yuri 1b zorder 1 at t41
    y"it was the best one."
    hide yuri
    hide natsuki
    hide sayori
    show monika 1d zorder 3 at t22
    show trollface 1p zorder 2 at f21
    t"....."
    m 1g"ahhh..what happend trollface?"
    t 1g"ammmm...monika don't you think [player]'s poem was more look like a dictation?"
    m 2i"yeah...but no need to hurt anybody's feeling by insulting them."
    t 1r"oh sorry!"
    hide trollface
    m"anyway....goodbye girls!"
    return

label ch0_end_trollface:
    $ ch0_choice = ""
    mc"of course trollface!"                                                                                                                                                                                                                                                  
    show trollface 1a zorder 2 at t11
    t"you there!"
    t"soooooo let's see"
    call showpoem (poem_t1)
    t 1n"yeah....."
    mc"it's amazing!"
    t 1d"r_really?"
    mc"and it's poem of your own perspective"
    mc"well done!"
    mc"you said you love stories."
    mc"and this poem mixed with story and poetry"
    t"don't you want to share your poem with me?"
    mc"ah..sure"
    t 1i"......"
    t 1r"ah sorry hosna but it's not a poem."
    t 2i"it's more look like a bunch of words"
    t"how someone write it and thinks it's a poem!"
    "i showed trollface a heavy experssion and he looks away."
    t 2l"ammm....but it has some of my favorite words anyway."
    return
       
    $ chapter = 1
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show monika 4k zorder 3 at t11
    m "Hi again, [player]!"
    m 1b"and his friend,Trollface!"
    show trollface 1c zorder 2 at t33
    t "hello.....monika."
    hide monika
    hide trollface
    "i think he's still mad at me."
    show trollface 2o zorder 1 at t11
    t"...."
    mc 1f"ammm...sorry trollface..."
    mc"for that stupid poem and bad emotion...."
    t 1e"no problem [player]...."
    mc 1d"or.....maybe im not what you expected..."
    t 1i"no no no no it's right that i didn't expect you to save me."
    t 1b"but maybe you can't write a poem truely..."
    t 1n"i can't do it too!"
    t"so im sorry."
    mc 1d"we both sorry anyways...."
    t 1a"yeah! and let's forget about that situation"
    mc"i have an idea! let's invite monika and you to my home.in that way,we can practice on our poem skill"
    t 1b"i agree,[player]!"
    show trollface 3i zorder 3 at h22
    t"__"
    show monika 4k zorder 2 at l21
    m"time for sharing poems!"

    return


    label ch1_end:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    mc "Phew..."
    "FINISH!"
    mc "wait huh?"
    mc "is that__"
    "My eyes land on Trollface and Natsuki."
    show trollface 1h zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show trollface 1j zorder 2 at t21
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Trollface smiles sadly."
    show natsuki zorder 3 at f22
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki zorder 1 at t22
    show trollface zorder 3 at f21
    t 1h "Eh?"
    t "Um...did you say something?"
    show trollface zorder 1 at t21
    show natsuki zorder 3 at f22
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki zorder 1 at t22
    show trollface zorder 3 at f21
    t 1j "Oh Thanks..."
    t "Yours is cute?"
    show trollface zorder 1 at t21
    show natsuki zorder 3 at f22
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki zorder 2 at t22
    show trollface zorder 1 at f21
    t 1d "I-I know that!"
    t 1c "The language, I guess..."
    t "I was trying to say something better..."
    show trollface zorder 1 at t21
    show natsuki zorder 3 at f22
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something better to say?"
    n "Thanks, but it really didn't come out better at all!"
    show natsuki zorder 2 at t22
    show trollface zorder 2 at f21
    t 1i "Um..."
    t "Well, I do have to advise you couple suggestions..."
    show trollface zorder 1 at t21
    show natsuki zorder 3 at f22
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Sayori liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show natsuki zorder 2 at t22
    show trollface zorder 2 at f21
    t 2s "Excuse me..."
    t "what did i do to deseve it!? ."
    t 2t "and why you think im insulting your writing style?."
    t "it's good,though."
    show trollface zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Nn...!"
    show natsuki zorder 2 at t22
    show trollface zorder 1 at f21
    t 1k "And [player] liked my poem too, you know."
    t "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    show trollface zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress him , Trollface."
    play music t7
    show natsuki zorder 2 at t22
    show trollface zorder 1 at f21
    t 1d "E-Eh?!"
    t "That's not what I...!"
    t 1q "Grrrrr..."
    t "You...You're just..."
    "Trollface stands up as well."
    t 2s "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show trollface zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki zorder 2 at t22
    show trollface zorder 3 at f21
    t 2r "I...!"
    t "No..."
    t "If I was that crazy..."
    $ style.say_dialogue = style.edited
    t 1x "{nw}...i would rip you to pieces!"
    $ style.say_dialogue = style.normal 
    show trollface zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "wha__!"
    show sayori 2l behind yuri, natsuki at l41
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    s "U-Um!!"
    s "Is everyone okay...?"
    show sayori 2 at lhide
    hide sayori
    show natsuki zorder 3 at f33
    show trollface 3x zorder 2 at h32
    show natsuki zorder 2 at t33
    $ style.say_dialogue = style.edited
    t "{nw}HAHAHAH!"
    $ style.say_dialogue = style.normal
    show monika 3l behind trollface, natsuki at l41
    m "Um, Trollface, that's a little--"
    show monika zorder 3 at h41
    show trollface 2x zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    $ style.say_dialogue = style.edited
    t "{nw}come on....it's just a littl--!"
    $ style.say_dialogue = style.normal
    play sound "sfx/slap.ogg"
    show monika at lhide
    hide monika
    show yuri zorder 2 at t32
    show trollface zorder 1 at t42
    show natsuki zorder 2 at t33
    show sayori 4p behind trollface, natsuki at l41
    t "ah...!"
    show sayori at lhide
    hide sayori
    show trollface zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    t"Why did you slap me [player]?"
    show natsuki 4m zorder 3 at f21
    t 1u "[player]..."
    t "*sob*"
    show trollface zorder 1 at s21
    show natsuki zorder 3 at f22
    n 4u"i didn't know that it goes on that far!"
    t 1w "IT'S THE PROBLEM ,NATSUKI!"
    t 1v "i.e YOU NEVER THINK OF WHAT YOU SHOULD DO."
    t 1u"but_!"
    t 1v"what do think about it [player]?"
    t "isn't it {i}tomfoolery{/i}?"
    show trollface zorder 2 at t21
    mc "Um...!"
    show trollface 1t zorder 3 at f21
    show natsuki 1e zorder 3 at f22
    t "Well??"
    mc "..."
    show trollface zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about what is true..."
    "But whomever I agree with, they'll probably think more highly of me!"

    menu:
        "So, of course that's going to be...!"
        "Natsuki.":
            call ch1_end_natsuki
        "Trollface.":
            call ch1_end_trollface

    show bg club_day
    show monika 4b zorder 2 at t11
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show monika zorder 2 at t44
    show sayori 4x zorder 2 at t31
    s "It was a lot of fun!"
    show sayori behind yuri at thide
    show yuri 1i zorder 2 at t31
    hide sayori
    y "Well, I'd say it was worth it."
    show yuri behind natsuki at thide
    show natsuki 4q zorder 2 at t31
    hide yuri
    n "It was alright. Well, mostly."
    show natsuki zorder 1 at thide
    hide natsuki
    show trollface zorder 1 at f21
    t 1o"..................."
    m 1i "trollface, we have to TALK in private place after club."
    t 1d"...Sure,Monika,sure..."
    mc "can i come with you,Monika?."
    m 1c "Yeah..."
    mc "In that case,sayori can you walk home without me?"
    mc "Just today."
    s 3k "*sigh* Ok...."
    mc "..."
    show monika zorder 1 at thide
    hide monika
    "I think to myself."
    "He disappointed me yesterday,too."
    "but i have to unfold it."
    "so......"
    show corridor
    show monika 2i zorder 2 at t22
    show trollface 1p zorder 2 at t21
    m "so....Admit it trollface!"
    t "..."
    mc "Monika,please don't act so scary."
    m 1i "Oh!sorry that was a little bad."
    mc "Here,let me explain it."
    mc "It's not that he's in good mood of saying it."
    m 3a"ok say."
    mc "ok, Trollface was a poular internet meme character that gots forggotten and trapped by a demon named..."
    mc "Trollge!"
    mc "he trapped in his own mind while,Trollge killed everyone."
    mc "But me and a friend helped me to save him..."
    mc "wait we helped him to get out and defeat Trollge."
    mc "And i brought everything and everyone back."
    mc "and now we are friends!"
    t 1e "Ah.....thanks,[player]."
    m 3o "...."
    m 1r "Sorry that i didn't know his past were this bad..."
    t 1k"aha!...no problem monika"
    show trollface 1d zorder 2 at h21
    mc "Trollface,You better apologize,too"
    t 1m "Ok! sorry monika."
    m 4b "Anyways goodbye boys."
    hide monika
    mc "goodbye."
    return

