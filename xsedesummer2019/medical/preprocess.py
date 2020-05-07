import csv, os, shutil

base_dir = '/home/xsede4/xsedesummer2019/medical/img/'
img_dir = '/home/xsede4/xsedesummer2019/medical/img/original_images/'

with open('data.csv', mode='r') as csv_file:
    line_count = 0
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if line_count == 0:
            # First line has column names
            line_count += 1
        else:
            label = row['Finding Labels']
            image_name = row['Image Index']
            new_path = os.path.join(base_dir, label)
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                
            # Copy image
            from_img_path = os.path.join(img_dir, image_name)
            to_img_path = os.path.join(new_path, image_name)
            shutil.copy2(from_img_path, to_img_path)

    print('All files copied!')