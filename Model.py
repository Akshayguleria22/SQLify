from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model_path = 'gaussalgo/T5-LM-Large-text2sql-spider'
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Get user input for question and schema
question = input("Enter your question: ")
schema = input("Enter the database schema: ")

# Combine the question and schema into the input text
input_text = f"Question: {question} Schema: {schema}"

# Tokenize the input text

model_inputs = tokenizer(input_text, return_tensors="pt")

# Generate SQL query
outputs = model.generate(**model_inputs, max_length=512)

# Decode the generated SQL query
output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

# Print the SQL query
print("SQL Query:")
print(output_text[0])


#Test
#What is the average, minimum, and maximum age for all French musicians?
#"stadium" "Stadium_ID" int , "Location" text , "Name" text , "Capacity" int , "Highest" int , "Lowest" int , "Average" int , foreign_key:  primary key: "Stadium_ID" [SEP] "singer" "Singer_ID" int , "Name" text , "Country" text ,         "Song_Name" text , "Song_release_year" text , "Age" int , "Is_male" bool ,         foreign_key:  primary key: "Singer_ID" [SEP],         "concert" "concert_ID" int , "concert_Name" text , "Theme" text , "Year" text , foreign_key: "Stadium_ID" text from "stadium",         "Stadium_ID" , primary key: "concert_ID" [SEP] "singer_in_concert",         foreign_key: "concert_ID" int from "concert",         "concert_ID" , "Singer_ID" text from "singer" "Singer_ID" , primary key: "concert_ID" "Singer_ID"
