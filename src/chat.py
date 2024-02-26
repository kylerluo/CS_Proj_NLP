from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*) ",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work at(.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"What is NLP ?",
        ["\nNLP stands for Natural Language Processing. It's a field of artificial intelligence (AI) and computational linguistics concerned with the interaction between computers and humans\nthrough natural language. The goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful.\nNLP encompasses a wide range of tasks and applications, including:\n\n* Text parsing and tokenization: Breaking down text into its constituent parts, such as words or phrases.\n\n* Named entity recognition (NER): Identifying and categorizing entities mentioned in text, such as names of people, organizations, locations, etc.\n\n* Sentiment analysis: Determining the sentiment or emotional tone expressed in text, such as positive, negative, or neutral.\n\n* Machine translation: Translating text from one language to another automatically.\n\n* Text summarization: Generating concise summaries of longer pieces of text.\n\n* Question answering: Providing answers to questions posed in natural language.\n\n* Speech recognition and synthesis: Converting spoken language into text and vice versa.\n\n* Language generation: Generating human-like text, such as in chatbots or virtual assistants.\n\nThese are just a few examples, and NLP continues to evolve with advancements in machine learning and deep learning techniques. It finds applications in various domains, including customer service, healthcare, finance, education, and more."]
    ],
    [
        r"What is natural language processing pipeline?",
        [ "The Natural Language Processing (NLP) pipeline refers to the series of steps or processes involved in analyzing and understanding natural language text. While specific implementations may vary depending on the task or application, a typical NLP pipeline can include the following stages:\n\nText Preprocessing:\n\n-Tokenization: Breaking down the text into smaller units such as words, phrases, or sentences.\n\n-Lowercasing: Converting all text to lowercase to ensure consistency.\n\n-Removing punctuation: Eliminating non-alphanumeric characters.\n\n-Removing stop words: Filtering out common words like 'and,' 'the,' 'is,' etc., which do not contribute much to the meaning of the text.\n\n-Part-of-Speech (POS) Tagging:\n\n-Assigning parts-of-speech (e.g., noun, verb, adjective) to each word in the text.\n\nNamed Entity Recognition (NER):\n\n-Identifying and categorizing named entities such as names of people, organizations, locations, dates, etc.\n\nDependency Parsing:\n\n-Analyzing the grammatical structure of the text to determine the relationships between words.\n\nSemantic Analysis:\n\n-Extracting the meaning or semantics from the text. \n\nModeling and Analysis:\n\n-Applying machine learning or deep learning models to perform specific tasks, such as text classification, named entity recognition, machine translation, etc.\n\n-Training and evaluating models on labeled datasets.\n\n-Fine-tuning models based on performance metrics and domain-specific requirements."]
    ],
        [
        r"What is the business impact of NLP?",
        [ "The Natural Language Processing (NLP) pipeline refers to the series of steps or processes involved in analyzing and understanding natural language text. While specific implementations may vary depending on the task or application, a typical NLP pipeline can include the following stages:\n\nText Preprocessing:\n\n-Tokenization: Breaking down the text into smaller units such as words, phrases, or sentences.\n\n-Lowercasing: Converting all text to lowercase to ensure consistency.\n\n-Removing punctuation: Eliminating non-alphanumeric characters.\n\n-Removing stop words: Filtering out common words like 'and,' 'the,' 'is,' etc., which do not contribute much to the meaning of the text.\n\n-Part-of-Speech (POS) Tagging:\n\n-Assigning parts-of-speech (e.g., noun, verb, adjective) to each word in the text.\n\nNamed Entity Recognition (NER):\n\n-Identifying and categorizing named entities such as names of people, organizations, locations, dates, etc.\n\nDependency Parsing:\n\n-Analyzing the grammatical structure of the text to determine the relationships between words.\n\nSemantic Analysis:\n\n-Extracting the meaning or semantics from the text. \n\nModeling and Analysis:\n\n-Applying machine learning or deep learning models to perform specific tasks, such as text classification, named entity recognition, machine translation, etc.\n\n-Training and evaluating models on labeled datasets.\n\n-Fine-tuning models based on performance metrics and domain-specific requirements."]
    ],
]
def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()