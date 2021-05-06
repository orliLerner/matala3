import re
import json

def read_txt():
    file_open = open('�צאט WhatsApp עם יום הולדת בנות לנויה.txt','r',encoding ='utf-8')
    text_read = file_open.readlines()   
    return text_read

def people(text):
    dic_ids = {}
    j = 0
    for line in text:
        line = line.strip()
        if( (" - ")and(": ") in line):
            start =  line.find(" - ")+3
            end = line.find(": ")
            person = line[start:end]
            if person not in dic_ids:
                dic_ids[person] = j
                j += 1
    return dic_ids

def list_messages(text_read,dic_ids):
    messages_l = []
    i = 0
    for line in text_read:
        line = line.strip()
        ##reading the lines of the group that went down a row
        if(i!=0 and i!=1):
            if( (" - ") not in line):
                tosefet = line
                msg["text"] = msg["text"] + tosefet
        if( (": ") in line):
            splitLine = line.split(' - ') 
            dateTime = splitLine[0] 
            message = ' '.join(splitLine[1:]) 
            start =  line.find(" - ")+3
            end = line.find(": ")
            person = line[start:end]
  
            splitMessage = message.split(': ') 
            message = ' '.join(splitMessage[1:]) 
            id_num = dic_ids[person]           
            msg = {"datetime":dateTime,"id":id_num,"text":message}
            messages_l.append(msg)
        i+=1
    return messages_l

text_read = read_txt() ##calling the first function
dic_ids = people(text_read) 
messages_l = list_messages(text_read,dic_ids) ##creating a list of the dictionaries of the messages

##part four
metadata = {}

start_chat = text_read[1].find(' "')
end_chat = text_read[1].find('" ')

chat_name = text_read[1][start_chat+2:end_chat]
    
split_dateTime = text_read[1].split(' - ')
creation_date = split_dateTime[0]
creator_temp = re.findall(r'ידי(\s.*?)$' , text_read[1])
creator = creator_temp[0].rstrip()
num_of_participants = len(dic_ids)

metadata["chat_name"] = chat_name
metadata["creation_date"] = creation_date
metadata["num_of_participants"] = num_of_participants
metadata["creator"] = creator

final_dic = {}
final_dic["messages"] = messages_l
final_dic["metadata"] = metadata

result_file = open(chat_name+".txt",'w',encoding='utf8')
result_file.write(json.dumps(final_dic, indent = 4, ensure_ascii=False))
result_file.close()
