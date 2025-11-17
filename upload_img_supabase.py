# upload_img_supabase.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
import json

SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
 
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# folder_path='img_upload'
# folder_path = 'batch3_compressed'
# folder_path = 'batch4_compressed'
folder_path = 'batch10_compressed'


SUPABASE_URL="https://zffxolckdzbutfyzsbis.supabase.co"

#unloded file
unloded_files=[]

def upload_images_to_supabase(folder_path):
    for filename in os.listdir(folder_path):
        img_path=''
        data={}
        update_response={}
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif',".webp")):
            file_path = os.path.join(folder_path, filename)

            # if len(filename.split(" ")) > 1:
            #     upload_filename = filename.replace(" ","-").lower()  # Replace spaces with - for URL compatibility
            # else:
            #     upload_filename = filename.replace(" ", "").lower()

            upload_filename = filename.replace(" .",".").replace('(',"").replace(')',"").replace('_',"-").replace('#',"").replace("'", "").replace(" ","-").lower()  # Replace spaces with - for URL compatibility

              #  update the coctail table with the new image path where cocktail_id matches
            print(f"\n\nChecking for cocktail_id: {upload_filename.split('.')[0]}")
            get_response = supabase.table('cocktail_details').select('*').eq('cocktail_id', upload_filename.split('.')[0]).execute()

            print('get_response--->>>>',get_response.data[0].get('cocktail_name') if get_response.data else "No data found")
            # exit()


            print(f"Uploading {file_path}...")
            with open(file_path, 'rb') as file:
                try:
                    file_data = file.read()
                    response = supabase.storage.from_('cocktail').upload(f'public/{upload_filename}', file_data, {"upsert": "true"})
                    data = response.dict()
                

                    img_path = f"{SUPABASE_URL}/storage/v1/object/public/cocktail/public/{upload_filename}"                

                    print("img_path: ",img_path)

                    #  update the coctail table with the new image path where cocktail_id matches
                    update_response = supabase.table('cocktail_details').update({'img_path': img_path}).eq('cocktail_id', upload_filename.split('.')[0]).execute()

                    # print("update_response",update_response)

                except Exception as e:
                    unloded_files.append({
                        "filename": filename,
                        "img_path": img_path,
                        "upload_filename": upload_filename,
                        "img_data": data,
                        "update_response": update_response,
                        "error": str(e)
                    })
                    print(f"\n\n in  exception img_path: {img_path}")
                    print(f"Error uploading {filename}: {e}")
    
    if unloded_files:
        with open('unloded_files.json', 'w') as f:
            json.dump(unloded_files, f, indent=4)
        print(f"Some files failed to upload. Details saved in 'unloded_files.json'.")

upload_images_to_supabase(folder_path)


# https://zffxolckdzbutfyzsbis.supabase.co/storage/v1/object/public/cocktail/public/25th%20Hour.png

# {'path': 'public/25th Hour.png', 'full_path': 'cocktail/public/25th Hour.png', 'fullPath': 'cocktail/public/25th Hour.png'}