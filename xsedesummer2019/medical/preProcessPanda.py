
base_dir = '/home/xsede4/xsedesummer2019/medical/img/'

img_dir = '/home/xsede4/xsedesummer2019/medical/img/original_images/'


import pandas as pd
import numpy as np
import os
import shutill

data = pd.read_csv('Data_Entry_2017.csv')

uniqueLabels= []
i = 0
for image in data['Image Index']:
    image_name = image 
    # label = data['Finding Labels']
    for labels in data.loc[i, ['Finding Labels']]:

        if ('|' in labels):
                findingLabelSeperate= labels.split('|')
                for individualLabel in findingLabelSeperate:

                        if individualLabel not in uniqueLabels:
                                uniqueLabels.append(individualLabel)
                                paths = os.path.join(base_dir, individualLabel)
                                os.mkdir(paths)

                                #copy image

                        else:
                                paths = os.path.join(base_dir, individualLabel)
                                
                        from_img_path = os.path.join(img_dir, image_name)
                        to_img_path = os.path.join(paths, image_name)
                        shutil.copy2(from_img_path, to_img_path)
                                
                i+=1

        else:
                if (labels not in uniqueLabels):
                        uniqueLabels.append(labels)
                        paths = os.path.join(base_dir, labels)
                        os.mkdir(paths)

                else:
                        paths = os.path.join(base_dir, labels)
                        
                from_img_path = os.path.join(img_dir, image_name)
                to_img_path = os.path.join(paths, image_name)
                shutil.copy2(from_img_path, to_img_path)

                i+=1
print('All files copied bro!')
