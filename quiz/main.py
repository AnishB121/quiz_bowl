from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
example = ['<b>This element is the central atom of the product of the Michaelis-Arbuzov reaction, which is used to prepare esters of this element. Knowles won the 2001 Chemistry Nobel for designing the asymmetric, chiral hydrogenation catalyst DIPAMP, whose two central atoms are of this element. This element is the central atom of a reagent that deaminates arenediazonium salts. Replacing hydroxyl groups with halogens often uses (*)</b> trihalides of this element. The most common organic reagent that uses this element is its triphenyl type, which is a reactant in the Wittig reaction. For 10 points, name this nonmetal that lies below nitrogen on the periodic table.',
 '<b>An attempt to impeach this man led to a brawl within his state legislature on “Bloody Monday.” This man imagined his potential presidency, including his cabinet nominees, in the book </b><i><b>My First Days in the White </b><b>House</b></i><b>. This man attempted to unseat Judge Benjamin Pavy through gerrymandering, leading Pavy’s son-in-law, Dr. (*)</b> Carl Weiss, to assassinate him. This man planned to redistribute wealth by limiting annual income to $1 million in a scheme that would make “every man a king,” the “Share Our Wealth” program. For 10 points, name this Louisiana politician who was nicknamed “the Kingfish.”',
 "This woman, who is described as a “clothed hyena” in one book, remembers her mother’s parrot asking “qui est là?” in another text. In the first book in which she appears, a stout redhead is repeatedly blamed for her “curious cachinnations.” In a later book, she lives with her aunt Cora after her home in Coulibri (koo-LEE-bree) is destroyed, and she commits date-rape in Granbois (grahn-BWAH) using an obeah (oh-BAY-ah) potion from Christophine. In the earlier book, Mr. Briggs reveals this person’s existence during an aborted wedding. The later book explains that this woman was called Antoinette Cosway before being renamed and shuttered in an annex of Thornfield Hall, where she was guarded by Grace Poole. For 10 points, what protagonist of Jean Rhys’s (zhahn rees's) Wide Sargasso Sea is the “madwoman in the attic” in Charlotte Bronte’s Jane Eyre?",
 'One building in this city features several asymmetric plates of glass set up on a podium made of travertine - the podium sits opposite a U-shaped wall made from golden onyx . At the center of that building is a statue of a woman entitled Alba, or Dawn, created by George Kolbe, which sits in the middle of a small pool. This city is also home to a museum of contemporary art designed by Richard Meier, with an exterior made of white porcelain-enameled steel. One of the tallest buildings in this city was designed to looking like a geyser gushing from the ground by Jean Nouvel - but that building, the Agbar Tower, may in fact look more like a giant blue penis with a red bottom. A multicolored dragon fountain straddles the stairway at the entrance to a certain park in this city, which features a winding serpentine bench. For 10 points, name this city home to Park Guell, as well as the Casa Mila and the unfinished Sagrada Familia.',
 '<b>In this play, Aunt Julie cares for her sister Rina and hints that one character is pregnant, while another character exclaims that she destroyed a child. One character in this play visits Mademoiselle Diana’s and accidentally shoots himself in the gut, after earlier being given a pistol to kill himself. That character in this play is having an affair with (*)</b> Thea Elvsted and writes a paper on the history of Brabant. The protagonist of this play is married to George Tesman, and she eventually burns Eilert Lovborg’s manuscript. For 10 points, name this play in which the title character shoots herself with her uncle’s pistol, a work of Henrik Ibsen.',
 'A variant of this experiment that successively introduces quarter wave plates and a diagonal polarizer and utilizes a pair of entangled particles is known as the quantum eraser, which was inspired by a variant proposed by John Wheeler that is known as the delayed-choice experiment. Another variant of this experiment confirmed Born’s rule that the probability density never contains high-order interference terms. The third volume of The Feynman Lectures opens by considering this experiment in an analysis that contrasts the behavior of bullets and waves. This experiment utilizes a screen on which appear a set of interference fringes regardless of whether photons pass through a namesake apparatus one at a time. For 10 points, name this experiment demonstrating the wave nature of light that was carried out by Thomas Young.',
 '<b>Phaeton misleads the protagonist of this novel after kissing a woman he claimed to be his sister. Miss Lavish publishes a book that includes a scene with a romanticized version of the female protagonist’s kiss with a man in a field of (*)</b> violets in this novel. That woman’s fiancée, a “superior” Londoner, shows true remorse for his pompousness after the protagonist leaves him for a man who rescued her after witnessing a murder in Italy. That man, George Emerson, marries Lucy Honeychurch in, for 10 points, what E.M. Forster novel about the title accommodation overlooking the Arno?',
 'The name of this location means gathering place in its native tongue. Shark’s Cove is one of the best dive sites on this island, although Hanauma Bay is also popular. The television show Lost was filmed on a beach on the north shore of this island, which is also home to the Banzai Pipeline at Ehukai Beach Park. Snakes on a Plane opens with a view of Diamondhead on this island. The Beach Boys sang a song referencing this island’s Waimea Bay, which is home to a surfing contest in memory of Eddie Aikau. This island is the birthplace of Barack Obama and home to the USS Arizona Memorial. For 10 points, name this island, the location of Pearl Harbor, Waikiki, and Honolulu.']
api_key = ""
passcode=""
import wikipediaapi
import google.generativeai as genai
class question(BaseModel):
    passcode: str
    diffculty: str
    topic: str 

class guess(BaseModel):
    passcode: str
    question: str

@app.get("/")
def test():
    return {"TEST"}

genai.configure(api_key = api_key)
QZZR = genai.GenerativeModel('gemini-1.5-flash')

wiki_wiki = wikipediaapi.Wikipedia(user_agent='QZZR ()', language='en',extract_format=wikipediaapi.ExtractFormat.WIKI)
@app.post("/get_question/")
async def get_question(question: question):
    if question.passcode == "":
        p = wiki_wiki.page(question.topic)
        prompt_3 = "Use the following context to generate a pyramidal quizbowl-type question on the given topic. The format should be similar to a quizbowl question, and the answer should lie within information in the article. The difficulty rating should be" + question.diffculty + ". Make sure that the question contains 4-5 sentences, sorted from hard and obscure clues in sentences to more revealing sentences. All sentences should countain a clue pertaining to the answer, not context. The last sentence must be worded like a question, but does not necessarily need to be a question. Please start the last sentence in the question field with the phrase 'For ten points'. Don't add an answer field, and make sure the answer is not " + question.topic + ". The question should be about a detail of the event, not the event itself. Here are a few questions to model the structure of your question after: " + example[0]+ example[1] + example[2] + example[3] + example[4] + example[5] + example[6] + "Here is the context: " + p.text
        response = QZZR.generate_content([prompt_3])
        return {'response': response.text}
    else:
        return {'response':'No'}

@app.post('/get_answer/')
async def get_answer(guess: guess):
    if guess.passcode == "":
        prompt_4 = "Answer the following question. Do not provide a justification, just the answer alone, not in a sentence. Here is the question: " + guess.question
        response_1 = QZZR.generate_content([prompt_4])
        return {'response': response_1.text}
    else:
        return {'response':'No'}
