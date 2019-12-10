import subprocess
import os
import time
import random
import pytumblr
from tumblr_keys import *    #this imports the content in our tumblr_keys.py file
#++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++ASCII_ART_PLAYer++++++++++++
#++++++++++++++++++++++++++++++++++++++++++
from art import *
import importlib
import pyclbr
module_name = 'art'
module_info = pyclbr.readmodule(module_name)
y=[]

#++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++GLOBAL_VARS++++++++++++
#++++++++++++++++++++++++++++++++++++++++++

class myclass(object):
    filelist2 = sorted(os.listdir("2glitch"))
    filelist = os.listdir("2glitch")
    list = os.listdir("2glitch") # dir is your directory path
    number_files = len(list)

    module_name = 'art'
    module_info = pyclbr.readmodule(module_name)
    y=[]

#++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

def Check_for_new ():
    time.sleep(360) # change back to 30
    print '+++++++++++++++++++++++++++++++++++++++++++++++++'
    print '++++++++++++++++++ASCII_ART++++++++++++++++++++++'
    print '+++++++++++++++++++++++++++++++++++++++++++++++++'
    print ''
    print '++++++++++++++Rechecking_Insta+++++++++++++++++++'
    print '+++++++++++++++++++++++++++++++++++++++++++++++++'


    # use instalooter to grab new files
    insta_looter = subprocess.Popen(["instaLooter hashtag 2glitch 2glitch -N  "], stdout=subprocess.PIPE, shell=True) # add  2glitch -N for new
    (insta_looter_out, err) = insta_looter.communicate()
    print insta_looter_out

    filelist2 = sorted(os.listdir("2glitch"))
    #filelist2 = sorted(filelist2,key=lambda x: int(os.path.splitext(x)[0]))


    list = os.listdir("2glitch") # dir is your directory path
    myclass.number_files = len(list)
    #print number_files
    #print filelist2[0]
    

def Dir_prep ():
    #make temp dir
    make_temp = subprocess.Popen(["mkdir temp"], stdout=subprocess.PIPE, shell=True)
    (make_temp_dir, err) = make_temp.communicate()
    print make_temp_dir
    
    make_2_glitch = subprocess.Popen(["mkdir glitched"], stdout=subprocess.PIPE, shell=True)
    (make_2_glitch_file, err) = make_2_glitch.communicate()
    print make_2_glitch_file

    proc3 = subprocess.Popen(["find . -name \*.DS_Store -type f -delete"], stdout=subprocess.PIPE, shell=True)
    (out3, err) = proc3.communicate()
    print out3

    myclass.filelist2 = sorted(os.listdir("2glitch"))
    myclass.filelist = os.listdir("2glitch")
    list = os.listdir("2glitch") # dir is your directory path
    myclass.number_files = len(list)

    copy_2_temp = subprocess.Popen(["cp 2glitch/" +myclass.filelist2[myclass.number_files-1]+" temp"], stdout=subprocess.PIPE, shell=True)
    (out_2_temp, err) = copy_2_temp.communicate()
    print out_2_temp

    myclass.filelist = os.listdir("2glitch")



def glitch_and_post ():
    count = 1
    while True:
        random_time = random.randint(1,3)
        if (count > myclass.number_files-1):
            dir_cleanup ()
            break
        
        while (count <= myclass.number_files-1):
            #print "number_files",myclass.number_files-1
            #print '++++++++++++++++++++++++++++++++++++++--while loop'
            gli = random.randint(25,99)
            seed = random.randint(25,99)
            iterations = random.randint(25,115)
            proc4 = subprocess.Popen(["python jpglitch.py -a "+ str (gli)+ " -s "+str (seed)+" -i "+str (iterations)+" --jpg -o glitched/gm"+str (count)+".jpg 2glitch/"+myclass.filelist[count]], stdout=subprocess.PIPE, shell=True)
            (out4, err) = proc4.communicate()


            print '++++++++++++++++++Just_Glitched++++++++++++++++++'          

            # hey change this tag
            #client.create_photo('hang-glitch-gallery', state="published", tags=["glitch", "2glitch", "art", "glitch bot", "generative art","MFAH", "atCAMH", "HANG", "shapeshiftersCAMH", "CAMHTeenCouncil", "glitched" , "python" , "instalooter", "jpglitch", "pytumblr"], data= "glitched/gm"+str(count)+".jpg")
            # test 
            #count = count + 1


            for i in range(240):
                try:
                    ## hey change this tag
                    client.create_photo('hang-glitch-gallery', state="published", tags=["glitch", "2glitch", "art", "glitch bot", "generative art","MFAH", "atCAMH", "HANG", "shapeshiftersCAMH", "CAMHTeenCouncil", "glitched" , "python" , "instalooter", "jpglitch", "pytumblr"], data= "glitched/gm"+str (count)+".jpg")
                    count = count + 1
                    break # Only triggered if input is valid...
                except:
                    print("THE INTERNET CONNECTION GOT SKETCHY")# perhaps reconnect, etc.
                    print("RE-TRYING IN 30 seconds" ) #perhaps reconnect, etc.
                    print("Attempt-->" + str (i))
                    i = i +1
                    time.sleep(30)
            else:
                    print("we failed all the attempts - deal with the consequences.")


            print '++++++++++++++++++++Just_Posted_2++++++++++++++++++++'
            print '+++++++++++hang-glitch-gallery.tumblr.com++++++++++'
            print "+++++++++++Working_on_image_",count, "of_",myclass.number_files-1,"+++++++++++++++"

            art_play()
            time.sleep(30)

def dir_cleanup ():
    rm_glitched = subprocess.Popen(["rm -R glitched"], stdout=subprocess.PIPE, shell=True)
    (rm_glitched_file, err) = rm_glitched.communicate()
    print rm_glitched_file     

    rm_2_glitch = subprocess.Popen(["rm -R 2glitch ; mkdir 2glitch"], stdout=subprocess.PIPE, shell=True)
    (rm_2_glitch_file, err) = rm_2_glitch.communicate()
    print rm_2_glitch_file

    proc2 = subprocess.Popen(["cp temp/" +myclass.filelist2[myclass.number_files-1]+" 2glitch"], stdout=subprocess.PIPE, shell=True)
    (out2, err) = proc2.communicate()
    print out2

    del_temp = subprocess.Popen(["rm -R temp"], stdout=subprocess.PIPE, shell=True)
    (del_temp_dir, err) = del_temp.communicate()
    print del_temp_dir

def art_play():
    #loads array with art objects
    for item in module_info.values():
        artname = str(item.name)
        y.append(artname)

    #gets number of objects in the array
    objects_inarray = len(y)

    #gets random array element
    random_object = random.randrange(0,objects_inarray)

    #print y[random_object]
    obj = eval(y[random_object] + "()")

 

while True:
    art_play()
    Check_for_new ()
    Dir_prep () 
    glitch_and_post ()
    time.sleep(120)

