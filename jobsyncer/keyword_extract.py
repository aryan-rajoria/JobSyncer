from keybert import KeyBERT
import nltk
from nltk.corpus import stopwords
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def extract_tech_keywords(text, num_keywords=20):
    # Initialize KeyBERT model
    kw_model = KeyBERT()

    # Create a custom stop words list
    stop_words = set(stopwords.words('english'))
    # Add common words that might not be relevant
    stop_words.update(['use', 'using', 'used', 'also', 'like', 'can', 'may', 'might'])

    # Extract keywords
    keywords = kw_model.extract_keywords(text, 
                                         keyphrase_ngram_range=(1, 3), 
                                         stop_words=list(stop_words), 
                                         use_mmr=True, 
                                         diversity=0.7,
                                         top_n=num_keywords)

    # Filter keywords to keep only those likely to be technical terms
    tech_keywords = [keyword for keyword, _ in keywords if keyword.lower() not in stop_words and not all(c in string.punctuation for c in keyword)]

    return tech_keywords


# Function to read content from a text file and store it in a variable
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Specify the path to your text file
file_path = 'output.txt'

# Read the content of the file
file_content = read_file(file_path)

# Print the content of the file
print(file_content)


tech_keywords = extract_tech_keywords(file_content)
print("Extracted technical keywords:")
for keyword in tech_keywords:
    print(f"- {keyword}")