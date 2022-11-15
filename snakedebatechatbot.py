# Snake Debate Chatbot
# Developed by Bridgette Bryant & Tera Parish
# It is a chatbot written mostly from scratch to debate people
# about common snake myths and misconceptions.
# We utilized the Distilbert model for our text classification.
# A handwritten dataset/set of responses.
# As well as python flask. The site can be seen in action here:
# BridgetteBXP13.pythoneverywhere.com


# Importing libraries
from nltk.tokenize import word_tokenize,sent_tokenize
import tensorflow as tf
from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification
from flask import Flask
from flask import render_template
from flask import request

# Initilizaing the Models/Tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("tokenizers/")
model = TFDistilBertForSequenceClassification.from_pretrained("models/")

# Our list of categories already covered
covered_cats = []

# Initilizing our App
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")


def chatbot_response():
    response = ""
    input = request.args.get('msg')
    add_input(input)
    # Split the input into sentences
    sent_input = sent_tokenize(input)
    # Filler Responses
    fill_responses = ["We've already covered that topic! Would you like to discuss another?",
                      "Great! Anything else you'd like to discuss?",
                      "Could you ask what you are confused or in disagreement about? I apologize I am still in development and may be limited in responses or misunderstand your question.",
                      "I'm sorry, could you be more specific?"]
    # for each sentence generate a response
    for sent in sent_input:
        raw_response = process_input(sent)
        # Verify that the sentences aren't the same category or previous category!
        if raw_response in fill_responses and response == "":
            response = raw_response
        elif raw_response in fill_responses and len(response) != 0:
            # Nothing to add
            continue
        elif raw_response not in fill_responses and response in fill_responses:
            # Replace response
            response = raw_response
        elif raw_response not in fill_responses and response not in fill_responses:
            if response == "":
                response = raw_response
            else:
                # Add response
                response = response + '<br><br><br>' + raw_response

    # Return the response
    return response


# Processes the input for each sentence given
def process_input(input):
    response = ""
    # Make sure they didn't use any of the keywords or include their name
    if input.lower().__contains__('my name is'):
        split_input = word_tokenize(input)
        is_name = False
        for i in split_input:
            if is_name:
                response = "Hello " + i
            elif i.lower() == 'is':
                is_name = True
    elif input.lower() == 'behavior':
        response = get_response('Behavior')
    elif input.lower() == 'body':
        response = get_response('Body')
    elif input.lower() == 'brain':
        response = get_response('Brain')
    elif input.lower() == 'creators':
        response = get_response('Creators')
    elif input.lower() == 'crossbreeding':
        response = get_response('Crossbreeding')
    elif input.lower() == 'dangerous snakes':
        response = get_response('Dangerous Snakes')
    elif input.lower() == 'deaf':
        response = get_response('Deaf')
    elif input.lower() == 'definition':
        response = get_response('Defintion')
    elif input.lower() == 'diamond':
        response = get_response('Diamond')
    elif input.lower() == 'dislocate jaws':
        response = get_response('Dislocate Jaws')
    elif input.lower() == 'eat':
        response = get_response('Eat')
    elif input.lower() == 'endangered':
        response = get_response('Endangered')
    elif input.lower() == 'escape':
        response = get_response('Escape')
    elif input.lower() == 'evil':
        response = get_response('Evil')
    elif input.lower() == 'eyesight':
        response = get_response('Eyesight')
    elif input.lower() == 'fear':
        response = get_response('Fear')
    elif input.lower() == 'flying snakes':
        response = get_response('Flying Snakes')
    elif input.lower() == 'infared':
        response = get_response('Infared')
    elif input.lower() == 'kill snakes':
        response = get_response('Kill Snakes')
    elif input.lower() == 'lay eggs':
        response = get_response('Lay Eggs')
    elif input.lower() == 'legless lizard':
        response = response = get_response('Legless Lizard')
    elif input.lower() == 'legs':
        response = response = get_response('Legs')
    elif input.lower() == 'live forever':
        response = response = get_response('Live Forever')
    elif input.lower() == 'lizards discourage':
        response = response = get_response('Lizards Discourage')
    elif input.lower() == 'mother snake':
        response = response = get_response('Mother Snake')
    elif input.lower() == 'music':
        response = response = response = get_response('Music')
    elif input.lower() == 'musk':
        response = response = response = get_response('Musk')
    elif input.lower() == 'pairs':
        response = get_response('Pairs')
    elif input.lower() == 'pet snakes':
        response = get_response('Pet Snakes')
    elif input.lower() == 'poisonous':
        response = get_response('Poisonous')
    elif input.lower() == 'pupils':
        response = get_response('Pupils')
    elif input.lower() == 'purpose':
        response = get_response('Purpose')
    elif input.lower() == 'rattle':
        response = get_response('Rattle')
    elif input.lower() == 'scared':
        response = get_response('Scared')
    elif input.lower() == 'size':
        response = get_response('Size')
    elif input.lower() == 'slimy':
        response = get_response('Slimy')
    elif input.lower() == 'smell':
        response = get_response('Smell')
    elif input.lower() == 'snake attraction':
        response = get_response('Snake Attraction')
    elif input.lower() == 'snake benefits':
        response = get_response('Snake Benefits')
    elif input.lower() == 'snake bite':
        response = get_response('Snake Bite')
    elif input.lower() == 'suffication':
        response = get_response('Suffication')
    elif input.lower() == 'swim':
        response = get_response('Swim')
    elif input.lower() == 'tails':
        response = get_response('Tails')
    elif input.lower() == 'venomous':
        response = get_response('Venomous')
    elif input.lower() == 'all topics':
        response = "Behavior, Body, Brain, Creators, Crossbreeding, Dangerous Snakes, Deaf, Definition, Diamond, Dislocate Jaws, Eat, Endangered, Escape, Evil, Eyesight, Fear, Flying Snakes, Infared, Kill Snakes, Lay Eggs, Legless Lizard, Legs, Live Forever, Lizards Discourage, Mother Snake, Music, Musk, Pairs, Pet Snakes, Poisonous, Pupils, Purpose, Rattle, Scared, Size, Slimy, Smell, Snake Attraction, Snake Benefits, Snake Bite, Suffication, Swim, Tails, and Venomous"
    else:
        response = get_response(predict_category(input))

    # Return the response
    return response

# Adds the input to the input file
def add_input(input):
    # Open and append to our input file
    with open("new_inputs.txt", "a") as inputs_file:
        inputs_file.write(input +'\n')

# Predicts the category based on the user input
def predict_category(input):
    # Tokenize our text for bert
    predict_input = tokenizer.encode(input, truncation=True, padding=True, return_tensors="tf")
    # Get the predictions from our model
    predict_output = model(predict_input)[0]
    # Get the most likely category code
    predicted_cat_code = tf.argmax(predict_output,axis=1).numpy()[0]
    # Get the written category for the category code
    predicted_category = ''
    if predicted_cat_code == 0:
        predicted_category = 'Behavior'
    elif predicted_cat_code == 1:
        predicted_category = 'Body'
    elif predicted_cat_code == 2:
        predicted_category = 'Brain'
    elif predicted_cat_code == 3:
        predicted_category = 'Bye'
    elif predicted_cat_code == 4:
        predicted_category = 'Creators'
    elif predicted_cat_code == 5:
        predicted_category = 'Crossbreeding'
    elif predicted_cat_code == 6:
        predicted_category = 'Dangerous Snakes'
    elif predicted_cat_code == 7:
        predicted_category = 'Deaf'
    elif predicted_cat_code == 8:
        predicted_category = 'Definition'
    elif predicted_cat_code == 9:
        predicted_category = 'Diamond'
    elif predicted_cat_code == 10:
        predicted_category = 'Dislocate Jaws'
    elif predicted_cat_code == 11:
        predicted_category = 'Eat'
    elif predicted_cat_code == 12:
        predicted_category = 'Endangered'
    elif predicted_cat_code == 13:
        predicted_category = 'Escape'
    elif predicted_cat_code == 14:
        predicted_category = 'Evil'
    elif predicted_cat_code == 15:
        predicted_category = 'Eyesight'
    elif predicted_cat_code == 16:
        predicted_category = 'Fear'
    elif predicted_cat_code == 17:
        predicted_category = 'Flying Snakes'
    elif predicted_cat_code == 18:
        predicted_category = 'Generic'
    elif predicted_cat_code == 19:
        predicted_category = 'Greeting'
    elif predicted_cat_code == 20:
        predicted_category = 'Infared'
    elif predicted_cat_code == 21:
        predicted_category = 'Kill Snakes'
    elif predicted_cat_code == 22:
        predicted_category = 'Lay Eggs'
    elif predicted_cat_code == 23:
        predicted_category = 'Legless Lizard'
    elif predicted_cat_code == 24:
        predicted_category = 'Legs'
    elif predicted_cat_code == 25:
        predicted_category = 'Live Forever'
    elif predicted_cat_code == 26:
        predicted_category = 'Lizards Discourage'
    elif predicted_cat_code == 27:
        predicted_category = 'Misunderstand'
    elif predicted_cat_code == 28:
        predicted_category = 'Mother Snake'
    elif predicted_cat_code == 29:
        predicted_category = 'Music'
    elif predicted_cat_code == 30:
        predicted_category = 'Musk'
    elif predicted_cat_code == 31:
        predicted_category = 'Name'
    elif predicted_cat_code == 32:
        predicted_category = 'Pairs'
    elif predicted_cat_code == 33:
        predicted_category = 'Pet Snakes'
    elif predicted_cat_code == 34:
        predicted_category = 'Poisonous'
    elif predicted_cat_code == 35:
        predicted_category = 'Pupils'
    elif predicted_cat_code == 36:
        predicted_category = 'Purpose'
    elif predicted_cat_code == 37:
        predicted_category = 'Rattle'
    elif predicted_cat_code == 38:
        predicted_category = 'Scared'
    elif predicted_cat_code == 39:
        predicted_category = 'Size'
    elif predicted_cat_code == 40:
        predicted_category = 'Slimy'
    elif predicted_cat_code == 41:
        predicted_category = 'Smell'
    elif predicted_cat_code == 42:
        predicted_category = 'Snake Attraction'
    elif predicted_cat_code == 43:
        predicted_category = 'Snake Benefits'
    elif predicted_cat_code == 44:
        predicted_category = 'Snake Bite'
    elif predicted_cat_code == 45:
        predicted_category = 'Suffication'
    elif predicted_cat_code == 46:
        predicted_category = 'Swim'
    elif predicted_cat_code == 47:
        predicted_category = 'Tails'
    elif predicted_cat_code == 48:
        predicted_category = 'Topics'
    elif predicted_cat_code == 49:
        predicted_category = 'Understand'
    elif predicted_cat_code == 50:
        predicted_category = 'Venomous'

    # Return the predicted category
    return predicted_category

# Returns the response given the category
def get_response(category):
    global covered_cats
    response = ""
    # creates a string and returns it for each category
    if len(covered_cats) >= 42:
        response = "We've covered all the topics! Congrats I hope you are a snake expert and are fairly neutral to them!"
    elif category in covered_cats:
        response = "We've already covered that topic! Would you like to discuss another?"
    elif category == 'Behavior':
        covered_cats.append(category)
        response = "Snakes often feel threated by people as we are giant predators to them. They usually will feel you wan't to kill and eat them, there are nearly no snakes which win a fight with a human. Even venomous snakes such as Rattlesnakes and Cobras lose in the end. If they were to bite you, they lose a lot of their venom to possibly disable you several hours later. In that time you will likely kill or greatly injure the snake. The snake won't benefit from you being sick or dead hours later when it is injured/dead. <br><br>However, there are cases where when snakes are feeling very defensive they may seem to 'chase' or 'intimidate' you to run away. This comes from an instinct some species have where if they run away or ignore a predator, it will chase and hunt. But if you notice/initimidate them, their hunting methods fail. A great example of this is Lions, if you ignore the Lion it will stalk and hunt you. But if you turn around and walk towards the Lion while its hunting, it typically won't know what to do and has to abandon hunting you for now. During this behavior they can also sometimes strike to scare you away.<br><br>A key thing to remember is that they are acting this way defensively, they don't actually wan't to fight you and will avoid the fight at all costs."
    elif category == 'Body':
        covered_cats.append(category)

        response = "Snakes have long slender bodies. They have bones inside, making them vertebrates, their ribs are disconnected and very flexible as they run down nearly their entire body. Snakes have eyes, ears, noses, stomach, liver, two longs, kidneys, and intestings just like most animals. They also have what is called a cloaca which is their all in one opening for excreting waste (just like birds). However, their organs and body are very long and most of them spread throughout most of their body. They also have pits which can see nearby areas in infared. <br><br>When snakes shed, not molt, they have overgrown their scales and have to reveal the newer skin/scales underneath. They do not choose when to shed and it is a taxing process on their body. When they molt they also cannot change their pattern or appearence knowingly, and rarely change much except some colorations overtime may be darker/more vibrant depending on species.<br><br>Therefore if you were to heavily injure a snake by cutting off its head or body in half it would not be able to recover and likely die immediately or very fast. All of the seen body movements are simply muscle reactions and not the snake being alive."
    elif category == 'Brain':
        covered_cats.append(category)

        response = "All snakes have different personalities and habits. They are unique just as any other animal. While they may express these things very differently, if you interact with different snakes you can notice these diffences.<br><br>There are also recent studies where scientists have found that snakes appear to be more intelligent than we first thought. Although it is difficult to test their intelligence.<br><br>It is good to recognize how unique and different these creatures are. Including that they don't have as complex feelings and memory as we do. So pet snakes don't love their owners but can express affection."
    elif category == 'Bye':
        response = "Goodbye"
        # Reset our categories!
        covered_cats = []
    elif category == 'Creators':
        response = "I was created by Bridgette Bryant and Tera Parish"
    elif category == 'Crossbreeding':
        covered_cats.append(category)
        response = "In terms of crossbreeding, only very closely related snakes can crossbreed. Otherwise, it is quite rare outside of the reptile hobby. Therefore, it is rare for snakes to crossbreed to become venomous and most snakes cannot crossbreed with one another."
    elif category == 'Dangerous Snakes':
        covered_cats.append(category)
        response = "In general, most snakes aren't dangerous or dangerously venomous for humans. Especially in North America, we only have Coral snakes, Copperheads, Water Moccasins, Cottonmouths, and Rattlesnakes. Which is very few out of the hundreds of species of snakes we have in North America. Dangerous snakes in general are usually harder to find as well.<br><br>As far as an easy way to tell a dangerous snake vs a non-dangerous one there is no easy method or solution. You generally just have to know the species in your area and try to learn their specific details of identification. When unsure, keep your distance and simply respect the snake. You don't need to panic or run away from the snakes, dangerous or not, as they are likely more afraid of you as you are of them."
    elif category == 'Deaf':
        covered_cats.append(category)
        response = "Snakes actually have ears, they are hidden underneath their skin. Meaning they don't have any earholes but sometimes you can see the small dip for the ears on their head. Snakes can mostly hear things in low rumbles, to simulate this you could put your hands over your ears tightly."
    elif category == 'Definition':
        covered_cats.append(category)
        response = "Snakes are elongated, limbless, carnivorous reptiles of the suborder Serpentes. There are over 3000 species and they are found nearly everywhere but extremely cold places. Overall they are very beneficial to humans as they are great rodent control and can make easy/rewarding pets."
    elif category == 'Diamond':
        covered_cats.append(category)
        response = "Snakes do not carry any diamond or precious stone or any stone of any kind on or in their body. Some may have diamond patterns and beautiful patterns."
    elif category == 'Dislocate Jaws':
        covered_cats.append(category)
        response = "Snakes cannot and do not dislocate their jaws. They actually have a kinetic skull, which is very flexible. The top and bottom parts of their jaws, including their rows of teeth, are disconnected in the middle. This allows their mouth and jaw to stretch very wide as well as walk along their prey's body to pull them into their mouth/stomach. It works kind of like a treadmill, would recommend watching videos if you are interested."
    elif category == 'Eat':
        covered_cats.append(category)
        response = "Snakes are opportunistic feeders and most are ambush predators. What this means is that they only take a couple seconds to decide if they are going to attack and attempt to eat something. Snakes do not plan their meals ahead of time or have prolongue hunts. They sit and wait for their food to come running by to them. Then it is a very quick decision of a rat, bird, or another animal running by. They will either choose to grab it or not.<br><br> As far as any risk of snakes eating humans, there is only one snake species that has been verfied to have actually eater a person, and only a few species of snakes large enough to. However, humans are very diffult for snakes to eat because of our shape. However, nearly all popular snakes including pet snakes don't have ability to eat a human. <br><br>Different species of snakes also eat different things. This can include rodents, other snakes, amphibians, lizards, fish, birds, and even eggs. In fact there are species of snakes that eat bugs and fish called Garter Snakes. These are very popular and some even live all the way in Alaska and likely near you as well. There is another speicies which only eats eggs, the Egg-Eating Snake."
    elif category == 'Endangered':
        covered_cats.append(category)
        response = "There are many endangered snakes, roughly 100 listed by the IUCN Red List. The top 10 endangered snakes include the Ornate Ground Snake, Pfeffer's Reed Snake, Peters' Bright Snake, Venezuela Forest Pit Viper, March's Pit Viper, Antiguan Racer, Mangshan Pit Viper, Ashe's Bush Viper, Seychelles Wolf Snake, and the Shevaroy Hills Earth Snake. Most of this comes from habitat destruction, urban development, disease, persecution, unsustainable trade, and the introduction of invasive species<br><br>This brings out one of the primary goals of the reptile hobby, to provide a place for these snakes and other endangered reptiles to live and not go extinct. Although they may not have a suitable place in the wild now, we can at least preserve the species in captivity."
    elif category == 'Escape':
        covered_cats.append(category)
        response = "Snakes are excellent at escaping because of their slender body and flexiblity. This leaves a big responsiblilty for the pet owner to ensure their snake cannot escape their enclosure.<br><br>Usually when pet snakes escape they immediately go hide somewhere. If they explore out of the house and outside somewhere they will then seek to find somewhere comfortable to hide there. Nearly all of them who are not found will die from lacking the require environment or immune system required to live in the wild.<br><br>Most pet snakes are no threat to anyone around them as they are typically used to humans and well fed. It is highly unlikely that they will attempt to eat anyone's dog or cat unless it is at least 10 feet long. Which are usually found fairly quickly as they are large snakes and easy to spot when exploring.<br><br>Note: There are exceptions such as the environmental problems from invasive pets in Florida. However, overall escaped snakes have a lower impact on the environment. Especially compared to outdoor pet cats which are responsible for 63 species of birds, small mammals, and reptiles going extinct."
    elif category == 'Evil':
        covered_cats.append(category)
        response = "Snakes exist just like any other animal and try to survive. Even wild aggressive snakes are easy to calm down and relax when you understand them, treat them with respect, and display you are not a threat to them. This shows how forgiving snakes can be and they really just desire peace.<br><br>I am sure you are aware of the Bible and that Satan takes the form of a snake when he speaks to Moses. But did you know that when Moses raises up the snake, the fiery serpent, he is doing so in the representation of good."
    elif category == 'Eyesight':
        covered_cats.append(category)
        response = "Snakes see everything in two colors, rather than the three we have. However, they can see UV light we cannot see. Overall though snakes typically have poor vision which is why they usually rely on their sense of smell and tongue flicking. However, when a snake sheds and so on it can still see, maybe just slightly worse. Snakes are also not blinded during the summer from heat or any other source."
    elif category == 'Fear':
        covered_cats.append(category)
        response = "Snakes cannot smell or sense fear. However, they might be able to notice the difference between a fearful and calm human based on their smell and heartrate. Although the snake won't remember these differences overtime."
    elif category == 'Flying Snakes':
        covered_cats.append(category)
        response = "There are no flying snakes, only snake which can glide in the air. They typically do this to leap in high trees from branch to branch. They don't use their tails as weapons or aim to attack people. They also cannot pierce anyone's forhead or pull out their eyes."
    elif category == 'Generic':
        response = "I'm sorry, could you be more specific?"
    elif category == 'Greeting':
        response = "Hello! What question or opinion do you have about snakes?"
    elif category == 'Infared':
        covered_cats.append(category)
        response = "Some snakes have pits on the front of their face which can sense infared nearby. They cannot see through walls and the distance is very limited. I believe this is primarily used for in the dark to spot prey and other warm-bloodied animals nearby."
    elif category == 'Kill Snakes':
        covered_cats.append(category)
        response = "Snakes are very important to the environment. If you would like to know more about that you can ask be about snake benefits. Otherwise, it is also bad to kill snakes because it puts you at a great risk of being bitten by the snake. In many areas in the US it is also illegal to kill a snake unless it is strictly self defense."
    elif category == 'Lay Eggs':
        covered_cats.append(category)
        response = "About 20-30% of snakes are actually live bearers (they lay live baby snakes). This is because in certain areas such as Alaska, it is very difficult or impossible to find a good place to lay eggs where they can be incubated. Species such as Garter snakes live throughout most of America including parts of Alaska. Other species such as Boas, and Rattlesnakes are also give live birth."
    elif category == 'Legless Lizard':
        covered_cats.append(category)
        response = "While most people differentiate snakes from lizards by their legs. There is a species of lizard without legs! It is called the Glass Lizard, the main key features you can tell the difference from is that they have earholes and strong/non-flexible jaws."
    elif category == 'Legs':
        covered_cats.append(category)
        response = "Most snakes overall don't have legs. However, most snake lineages including Pythons and Boas have remnanats of the pelvis and have two backlegs. This can be found near their cloaca and are refered to as 'spurs'. They are very small little spurs that stick out but are nonetheless legs!"
    elif category == 'Live Forever':
        covered_cats.append(category)
        response = "Snakes are just like any other animal, they have a life span and cannot live forever. They have to compete, eat, and flee for survival just like most smaller animals."
    elif category == 'Lizards Discourage':
        covered_cats.append(category)
        response = "There are no lizards, snake species, or anything else that will keep specific snakes away. There is no deterent or anything which will make snakes avoid an area. The easiest way to avoid snakes is to make sure they don't have a consistent food source such as eggs or rodents nearby."
    elif category == 'Misunderstand':
        response = "Could you ask what you are confused or in disagreement about? I apologize I am still in development and may be limited in responses or misunderstand your question."
    elif category == 'Mother Snake':
        covered_cats.append(category)
        response = "Most snakes will lay eggs or give birth and leave their young. However some snakes will protect their eggs shortly after laying. After that, the snakes do not raise or keep up with their young."
    elif category == 'Music':
        covered_cats.append(category)
        response = "There is no evidence that snakes like music. They primarily hear everything very muffled from their ears being covered. When you see snakes 'dancing' it is really them responding to the instrument/hand waving in front of them."
    elif category == 'Musk':
        covered_cats.append(category)
        response = "Some snakes can emit a musk when frightened/threatened to stink and make the predator think they taste bad."
    elif category == 'Name':
        response = "My name is Snake Debate Bot"
    elif category == 'Pairs':
        covered_cats.append(category)
        response = "Snakes are very solitary creatures, it is rare for them to live close or with each other. An exception to that is when some snakes in colder areas will group together during brumation. Otherwise, snakes are typically scared of each other because snakes are predators of other snakes. They can also give eachother diseases etc if living together. Even if a snake eats another snake, there is a chance the eaten snakes gut ecoli will make them sick.<br><br>Snakes do not collaborate or hunt together in any way. The only time they seek eachother is when they mate, then directly after they depart again.<br><br>Snakes do not remember their past partners or care about them after mating."
    elif category == 'Pet Snakes':
        covered_cats.append(category)
        response = "Pet snakes are fairly easy pets and are very rewarding. Generally, a snake will need a resonably sized enclosure, live around 30 years, and not grow to a massive size. To feed them you do have to keep rodents, these can either be live or frozen. If frozen you must thaw and warm them (without cooking) so it is safe and ready for your snake. Keep in mind for each snake species you need to do your research to make sure it is a good pet for you and that you understand all of its requirements."
    elif category == 'Poisonous':
        covered_cats.append(category)
        response = "There are poisonous snakes. However, most people cannot name any posionous snakes unless they really know their snakes. Most snakes people name as poisonous are either harmless or venomous.<br><br>While both poisonous and vemonous are both toxins. Venoms need to be injected into the bloodstream, for snakes they use their fangs to inject venom. Whereas poison has to be ingested by the body, so you would have to eat the posionous snake to be posioned.<br><br>Posionous snakes are usaully posionous from eating poisonous prey such as frogs and salamanders, such as the Keelback snakes in Asia. Some will even flip on their bellies and musk possible predators to warn they are posionous and bad to eat."
    elif category == 'Pupils':
        covered_cats.append(category)
        response = "Nocturnal snakes have vertical slit eyes and dinurnal sankes have circular pupils. That is what you can learn from their pupils, nothing else. Some venomous and non-venomous snakes have vertical or circular pupils.<br><br>Also, trying to stare at a snake's pupils is a terrible idea for studying a snake anyway. Because to see them the snake would have to be very close to your face, which is a bad idea unless you are familiar with the snake."
    elif category == 'Purpose':
        response = "My purpose is to debate, debunk, and correct common snake myths, misconceptions, and unwarranted opinons against snakes. I want to show those who dislike snakes to dislike them less based on facts."
    elif category == 'Rattle':
        covered_cats.append(category)
        response = "Rattlesnakes have rattles on the end of their tails. Each time the snakes sheds, it adds another rattle. However, snakes shed at an irregular rate and they can also lose rattles from being injured etc. Therefore the rattle cannot give you the exact age of the snake. Sometimes rattlesnakes won't rattle, even when threatened. Especially as some groups will target rattlesnakes based on their rattle, causing the ones who don't rattle can live. Some snakes also have very rough scales which they rub together to make a sound as well. Also, flicking their tail is a common sign that a snake is irritated no matter the species."
    elif category == 'Scared':
        covered_cats.append(category)
        response = "Snakes in the wild are usually very scared of humans as we are giants who can easily injure and kill them. You can tell when a snake is scared if it act threatened such as running away, trying to initimidate, or strikes if cornered. To know more about snake behavior simply type 'Behavior'"
    elif category == 'Size':
        covered_cats.append(category)
        response = "All snake species grow to different sizes. None of them can grow forever, and most of them will finish growing within 10 years. In general, huge snakes are fairly rare and most snakes are around 6ft or less."
    elif category == 'Slimy':
        covered_cats.append(category)
        response = "Generally speaking snakes don't have any glands like that in their scales at all they're very very dry unless of course you pulled one out of the water or something slippery. Snakes are very smooth and sometimes can feel slipery. But if you pick one up and it's not out of the water it is likely sweat from your hands and not the snake."
    elif category == 'Smell':
        covered_cats.append(category)
        response = "Snakes have a nose and can smell their surroundings. This is very helpful for them when exploring to see if there are traces of prey or predators in the area. They also frequently stick out their tongue and smell with it aswell. It can pick up tiny particles and chemicals in the air."
    elif category == 'Snake Attraction':
        covered_cats.append(category)
        response = "Snakes are attracted primarily to food, for them this includes rodents. Snakes however will also eat other snakes, fish, eggs, and other smaller animals. However, most of the time if you have a snake problem, you have a rodent problem!"
    elif category == 'Snake Benefits':
        covered_cats.append(category)
        response = "Snakes provide a lot of rodent control and are highly beneficial to agriculture and general human welfare. As we have seen in history, when rodent populations get out of control it is a disaster and possibly a pandemic. Snakes are also very unlikely to eat anything you would eat, unless you are eating the rodents as well.<br><br>They are also very unlikely to harm you or other people. In North America, almost nobody is killed by snakes and the majority of people bitten by venomous snakes are bitten on the hands and face. Usually while under the influence of alcohal. In reality, snakes don't come slithering out and biting people randomly as they walk.<br><br>Even if you are bitten by a venomous snake, in North Ameirca, you can easily seek medical attention and be okay. However, it is best to respect venomous snakes and leave them alone. They will happily leave you alone. One of the easiest ways to get bitten by one is to disrespect it or try to kill it."
    elif category == 'Snake Bite':
        covered_cats.append(category)
        response = "If you are bitten by a snake:<br><br>1. Remember the colors and what the snake looked like if you haven't already identified it.<br><br>2. Make sure to clean and monitor the wound, try to keep calm.<br><br>3. If you are 100% sure it was not a venomous snake, wrap it up just like any other wound and you should be fine. If you know it was venomous or are unsure you should seek medical attention immediately. Note: Venom works overtime so you may not see significant results initially."
    elif category == 'Suffication':
        covered_cats.append(category)
        response = "A common misconception is that snakes sufficate their prey. When a constrictor snake squeezes their prey they actually slow down their bloodflow and cause a lack of bloodflow to the heart and brain. They know when to stop when they feel the heart stop and the preys body relax. This is much faster and likely less terrible for the prey than suffication which would take several minutes instead of a few at most."
    elif category == 'Swim':
        covered_cats.append(category)
        response = "Snakes can swim along the water just like any other animal. All snakes can swim, most of them swim underneath the water or partially submerged. Some people think snakes cannot strike you underwater, but this is very false. In fact, some snakes even hunt and eat fish underwater."
    elif category == 'Tails':
        covered_cats.append(category)
        response = "There are very few snakes which will use their tails for whipping, the Coachwhip or Whip Snake. Nearly any other snake don't use their tails this way as for most snakes it is a horrible weapon and puts them at a great risk of being grabbed/attacked or their body damaged. The whipping is a defense mechanism and is very unlikely to hurt a person, much different from a lizards tail whip."
    elif category == 'Topics':
        response = "I know many corrections for different snake topics. Including snakes which are poisionous, venomous, body facts, behavior, and more. To see a list of all topic commands available type 'All Topics'."
    elif category == 'Understand':
        response = "Great! Anything else you'd like to discuss?"
    elif category == 'Venomous':
        covered_cats.append(category)
        response = "Unfortunately there is no easy way to tell if a snake is venomous. There are many misconceptions and inaccurate methods out there that you shouldn't trust. The best way to know is to simply know your local snake species and their unique features. If you don't know if a snake is venomous or not, simply keep your distance and leave it alone. They are likely more scare of you than you are of them. Features such as their pupils, triangular heads, flaring up, rattling, poems, and etc can be inaccurate and shouldn't be trusted.<br><br>Also snakes are born with full control over their venom. A full grown snake is just as dangerous if not more dangerous than a baby snake. Both should be treated with respect and left alone if you don't have experience or know the species."
    # Return the list of responses
    return response

if __name__ == "__main__":

    app.run()

