
# Snake Debate Bot

## About Me

The Snake Debate Chatbot is a chatbot with a purpose to help stop the spread of common myths and misconceptions about snakes. These misconceptions can cause people to be harmed or harm the environment. It is designed debate against and debunk most snake myths inputted by the user. The ideal user for Snake Debate Chatbot is somebody whom dislikes/doesn’t know very much about snakes. Whom may believe some of these myths and is open-minded to being corrected/educated. It utilizes the Distil Bert Text Classification model, NLTK’s tokenizers, a handwritten dataset, and handwritten responses. It doesn’t save any user information except for the inputted sentences they give (in a text file) and gives an explicit warning to the user as it’s first message to not put ANY private information they wouldn’t feel comfortable with in a public database. We chose not to save any information such as name/interests to help protect the user’s privacy. It does however internally keep a list of covered topics that they have discussed with the user to avoid having the same responses repeatedly. My full report can be found [here](/SnakeDebatChatbot_Report.pdf)

## How to Run

1. Clone this Github Repo: https://github.com/BridgetteBXP13/Snake-Debate-Bot

2. Open in PyCharm or IDE:

- Option A: Have PyCharm/IDE Install Dependencies for you using your PC environment & Click Run in IDE
- Option B: Use Virtual Environment (Recommended for easy Uninstallation):
	(Make Sure your in Snake-Debate-Bot project directory!):
	1. Create/Activate Virual Environment: https://python.land/virtual-environments/virtualenv
	2. Install All Requirements in requirements.txt with Pip:
			
		`python -m pip install -r requirements.txt`
					
	3. Run Snake-Debate-Bot:
				
		`python snakedebatechatbot.py`
		
		
3. Chatting in Web:

	Open the Host given by the run (you will see a bunch of tensorflow/Bert info and can ignore those!
	
	Simply open something like this: http://127.0.0.1:5000
	
	You should see the bot and be able to chat with it, when you tell it your name or goodbye it assumes you are new user!
	
	
4. Uninstallation:

- If Option A from above:
	Delete Repo from you github and uninstall manually using:
			
	`python -m pip uninstall for anything installed by IDE`
				
- If Option B from above:
	Delete Repo folder including venv folder and done.
			
## Snake Debate Bot Hosted Online			
Currently Trying to find somewhere to be Hosted but is a large file and uses significant memory.
Snake-Debate-Bot will eventually be on internet.

So far Pythoneverywhere and Heroku have failed Snake-Debate-Bot :C

Currently attempting AWS
