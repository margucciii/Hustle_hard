#Code for the Gifted students detection and classification
IQ_results = {"verbal_reasoning": 0, "logical": 0, "mathematical": 0, "spatial": 0, "creative": 0}

#Detect and clasify their Giftedness based on their results

def calculation(dct):
    result = "The student is gifted in: "
    cont = 0
    creativity_exam = False
    for key, value in dct.items():
        if value >= 75:                                         #Analyse item by item to check if the student is gifted
            if cont != 0:
                result += ", "
            result += key
            cont += 1
            if key == "cretive":                                #Special clause for creativity (only if gifted in creativity, might be creatively gifted)
                creativity_exam = True

    if cont == 5:
        print("The student is Creatively Gifted")               #If gifted in all areas, they are creatively gifted
    elif cont == 4:
        if not creativity_exam:
            print("The student is Intellectually Gifted")       #If gifted in 4 areas but not creativity, they are intellectually gifted
    else:
        if cont >= 3:
            result += ". Flexibility recommended."              #If gifted in more than 3 areas recommend flexibility (Able to skip 1 or more grades)
        print(result)


#Get the IQ test results by inputs
verbal_reasoning = float(input("What is your verbal reasoning mark? "))
IQ_results ["verbal_reasoning"] = verbal_reasoning
logical = float(input("What is your logical mark? "))
IQ_results ["logical"] = logical
mathematical = float(input("What is your mathematical mark? "))
IQ_results ["mathematical"] = mathematical
spatial = float(input("What is your spatial mark? "))
IQ_results ["spatial"] = spatial
creative = float(input("What is your creative mark? "))
IQ_results ["creative"] = creative
print("Thanks, now your results are being calculated.")

#Use the function with the inputs

calculation(IQ_results)
