'''
Audio mp3 scraper 
'''

import urllib.request # download di mp3
import pandas as pd
import os

def extract_url_name(url):
   '''
   From url extract name animal
   
   @params url: url of audio animal
   '''
   if type(url) is not str:
      return None
   
   s = url.split("/")
   
   if s[-1].endswith(".mp3"):
      s2 = s[-1].split("_")
      name = "".join([s2[0], " ", s2[1]])
   else:
      return None
   
   return name

def download_mp3(df, classes, data_path):
   '''
   Download all audios of selected classes of animals in separate directories
   
   @params df: directory of multimedia links
   @params classes: list of latin animal names
   @params data_path: path of download directory
   '''
   
   for animal in classes:
      # se il nome non è presente nel dataset
      if not any(df['animal_name'] == animal):
         print("NOT FOUND", animal)
      else:
         # identifier comlumn as links
         links = df[df['animal_name'] == animal]['identifier']
         path = f"{data_path}/{animal}".replace(' ', '_')
         
         # create directory if not exists 
         try:
            if not os.path.exists(path):
               os.makedirs(path)
         except OSError:
             print (f"Creation of the directory {path} failed")  
         
         # download and create file .mp3
         for link in links:
            try:
               urllib.request.urlretrieve(link, f"{path}/{link.split('/')[-1]}")
               print(f"{path}/{link.split('/')[-1]}", "SUCCESSFUL DOWNLOADED")
            except:
               print("ERROR", link, " does NOT downloaded!")
   
      print(animal, "audios directory, SUCCESSFUL CREATED")

'''
main

'''
if __name__ == "__main__":
   # set working directory
   os.chdir("C:/Users/fede9/Documents/GitHub/DSIM_project/audio_download")
   
   df = pd.read_csv("audio_reference/multimedia.txt", sep = "\t") # multimedia dataframe
   classes = ["Equus caballus"] # list of classes
   data_path = "data" # path of download directory
   
   # add animal latin name column
   df['animal_name'] = df['identifier'].apply(lambda x: extract_url_name(x))
   
   # download mp3 files
   download_mp3(df, classes, data_path)