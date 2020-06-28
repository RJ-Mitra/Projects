import shutil,os

source_dir = "C:/Users/MyUser/Downloads" #Change to source directory path

base_target_path = source_dir #Set to destination dir path

code_path = base_target_path + "/Codes"
template_path = base_target_path + "/Templates"
doc_path = base_target_path + "/Documents"
app_path = base_target_path + "/Applications"
img_path = base_target_path + "/Images"
zip_path = base_target_path + "/Compressed"
video_path = base_target_path + "/Videos"
audio_path = base_target_path + "/Audios"

if "Codes" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Codes")
if "Templates" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Templates")
if "Documents" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Documents")
if "Applications" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Applications")
if "Images" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Images")
if "Compressed" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Compressed")
if "Videos" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Videos")
if "Audios" not in (os.listdir(base_target_path)):
    os.mkdir(base_target_path+"/Audios")

code_ext = ["scala","py","sql","dbc","ipynb"]
doc_ext = ["xlsx","docx","txt","csv","ppt","pptx","xlsb","xlsm","pdf"]
template_ext = ["json","rdp","pem"]
compressed_ext = ["zip","gz","tar","7zip"]
image_ext = ["img","png","jpg","jpeg"]
application_ext = ["exe","msi","apk"]
video_ext = ["mp4","avi"]
audio_ext = ["mp3","ogg"]

#Rename file if already exists
def checkIfExists(target_dir, filename):
    count = 1
    allFiles = os.listdir(target_dir)
    if filename in allFiles:
        while filename in allFiles:
            filename = filename.split(".")[0]+"("+str(count)+")."+filename.split(".")[-1]
            count+=1
    return filename


fileList = os.listdir(source_dir)

print("*** Script run started ***")

count = 0

try:
    for i in fileList:
        if "." in i:
            ext = (i.split(".")[-1]).lower()
            if ext in template_ext:
                shutil.move(source_dir+"/"+i, template_path+"/"+checkIfExists(template_path,i))
                count+=1
            elif ext in doc_ext:
                shutil.move(source_dir+"/"+i, doc_path+"/"+checkIfExists(doc_path,i))
                count+=1
            elif ext in code_ext:
                shutil.move(source_dir+"/"+i, code_path+"/"+checkIfExists(code_path,i))
                count+=1
            elif ext in application_ext:
                shutil.move(source_dir+"/"+i, app_path+"/"+checkIfExists(app_path,i))
                count+=1
            elif ext in image_ext:
                shutil.move(source_dir+"/"+i, img_path+"/"+checkIfExists(img_path,i))
                count+=1
            elif ext in compressed_ext:
                shutil.move(source_dir+"/"+i, zip_path+"/"+checkIfExists(zip_path,i))
                count+=1
            elif ext in video_ext:
                shutil.move(source_dir+"/"+i, video_path+"/"+checkIfExists(video_path,i))
                count+=1
            elif ext in audio_ext:
                shutil.move(source_dir+"/"+i, audio_path+"/"+checkIfExists(audio_path,i))
                count+=1
except:
    print("One or more files cannot be moved. Please check if they are open in any task.")

print(str(count) + " files moved.")
print("*** Script run complete ***")