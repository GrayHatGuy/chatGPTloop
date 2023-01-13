import openai
# Set the API key
openai.api_key = "<ENTER YOUR API KEY"
# Use the ChatGPT model to generate text
model_engine = 'text-davinci-002'
while True: 
    qr = input('Do you have a question for chatGPT? ') 
    if qr == '' or not qr[0].lower() in ['y','n']:print('Please answer with y or n!') 
    else:break 
if qr[0].lower() == 'y':
    f = open('chatGPTchat.out', 'w')
    n = 1
    i = 1
    loops = input('How many loops? ') 
    bots = input('How many bots in the conversation? ')
    promptseed = input('Ask your question and press <enter> when complete to submit: ')
    print('The human asked: ', promptseed)
    f.write('The human asks a group of ' + str(bots) + ' bots to discuss this question in ' + str(loops) + ' iterations: ' + str(promptseed) + '\n')
    while True:
        prompt = promptseed
        if n > int(loops): break
        for i in range(1, int(bots)):
            completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.9)
            response = completion.choices[0].text
            prompt = response + '' + prompt         
            print('interation ' + str(n) + ' chatGPT bot# ' + str(i) + ' ' + str(response))
            f.write('interation ' + str(n) + ' chatGPT bot# ' + str(i) + ' ' + str(response) + '\n')
            print('Bot ' + str(i) + ' asks Bot ' + str(i + 1) + ' ' + promptseed + '\n')
            f.write('Bot ' + str(i) + ' asks Bot ' + str(i + 1) + ' ' + promptseed + '\n')
            i = i + 1
        next
        n = n + 1
    f.close()
if qr[0].lower() == 'n':
    print('bye') 