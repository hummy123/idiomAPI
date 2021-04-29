import torch
import pathlib
from transformers import BertTokenizer, BertForSequenceClassification

def inference(input_text):
    #initialise tokeniser
    tokenizer = BertTokenizer.from_pretrained('bert-large-cased')

    #load model and set to training mode
    #NOTE: Generate ML Model to use by following steps in readme.md!
    PATH = "entire_idiom_model.pt"
    model = torch.load(PATH, map_location=torch.device('cpu'))
    model.eval()

    #list of classes (idiom categories) 
    #NOTE: ORDER IS IMPORTANT!
    classes = ["none", "It's raining cats and dogs."] 

    #convert input text to tokenizer format
    input_tok = tokenizer(input_text, return_tensors="pt")

    #infer the class the input belongs to
    input_classification_logits = model(**input_tok).logits
    input_results = torch.softmax(input_classification_logits, dim=1).tolist()[0]

    #find probability in text (previous step used vector representation)
    max_probability = 0
    cur_idiom = ""
    for i in range(len(classes)):
        cur_probability = int(round(input_results[i] * 100))
        if(cur_probability > max_probability):
            max_probability = cur_probability
            cur_idiom = classes[i]
    
    #return answer
    return cur_idiom    
