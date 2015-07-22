#import globepost
#from globepost import settings
import os,sys
'''
This script is use to populate the country table of newsapp.Country class
It extract country,code from country_code text file
The source of the file is :ftp://ftp.ripe.net/iso3166-countrycodes
the format table is:
Country                                         A 2     A 3     Number
So we are to extract Country and A2 column
After extraction format it into JSON string and save it into file
To run:
python populate_country.py
'''
import re
import json
def create_json(lines):
    
    i=0
    json_doc=""
    #json_str="["
    
    for line in lines:
        if   line not in ['\n','\r\n']:
            i=i+1
            segment=re.split("\s{2,}",line)
            country,code=segment[0],segment[1]
            #print(country," ## ",code)
            json_str= '{ "model":"newsapp.Country","pk":'+str(i)+',"fields": {"country_code":'+'"'+str(code)+'"'+',"country_name":'+'"'+str(country)+'"'+'}},'
            json_doc=json_doc+json_str           
            



            
            
    json_dump('['+json_doc+']')
                  


def json_dump(jsondoc):
    path=r"C:\Users\Coder\Documents\CodeProject\globepost\json_country_code.json"
    with open(path,"w") as f:
        fw=f.writelines(jsondoc)
        print(str(fw))

if __name__=="__main__":
    path=r"C:\Users\Coder\Documents\CodeProject\globepost\country_code.txt"
    print(path)
    linelist=[]
    if os.path.exists(path):
        
        with open(path,"r")as f:
            i=0
            while(i<2):
                line=f.readline()
               
                if "---------" in line:
                    i=i+1
                    while(True):
                        line=f.readline()
                        
                        if "---------" in line:
                            i=i+1
                            break
                        else:
                            if line != "":
                                linelist.append(line)
                                #print(line)

    create_json(linelist)
    

                

                    

            


    