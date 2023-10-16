from bs4 import BeautifulSoup
import requests, os
import re

# making slug
def generate_slug(input_string):
    # Convert to lowercase
    slug = input_string.lower()
    
    # Replace spaces with hyphens
    slug = re.sub(r'\s+', '-', slug)
    
    # Remove special characters
    slug = re.sub(r'[^a-zA-Z0-9-]', '', slug)
    
    # Remove leading and trailing hyphens
    slug = slug.strip('-')
    
    return slug


def doctor_information():
    get_url = requests.get('https://www.doctorbangladesh.com/').text
    soup = BeautifulSoup(get_url, 'lxml')

    doctors = soup.find_all('li', class_ ="doctor")

    for index, doctor in enumerate(doctors): 
        doc_photo = doctor.find('div', class_="photo").img['src']
        doc_name = doctor.find('h3', class_ = 'title').a.text
        doc_degree = doctor.ul.li.text
        doc_speciality = doctor.find('li', class_ = "speciality").text       
        doc_designation_element = doctor.find('li', title="Designation")    
        doc_workplace = doctor.find('li', title="Workplace").text
        
        
        if doc_designation_element:
            doc_designation = doc_designation_element.small.strong.text
        else:
            doc_designation = "Not specified"
             
        # =================== Doctor Chember Address and Phone ======================
        doc_name_slug = generate_slug(doc_name)
        # print(doc_name_slug)
        
        doc_detail = requests.get(f'https://www.doctorbangladesh.com/{doc_name_slug}/').text
        # print(doc_detail)
        
        soup_d = BeautifulSoup(doc_detail, 'lxml')
        # print(soup_d)
        
        doc_infos = soup_d.find_all('div', class_ = "entry-content")
        
        for info in doc_infos:
            info_d = info.find('p')
            
            get_text = info_d.get_text()

            # Remove kora holo first theke address porjonto then so on
            name_pattern = r"(.+?)Address:"
            address_pattern = r"Address:(.+?)Visiting Hour:"
            visiting_hours_pattern = r"Visiting Hour:(.+?)Appointment:"
            appointment_pattern = r"Appointment:(.+?)Call Now"

            # Find matches using regular expressions
            name_match = re.search(name_pattern, get_text)
            address_match = re.search(address_pattern, get_text)
            visiting_hours_match = re.search(visiting_hours_pattern, get_text)
            appointment_match = re.search(appointment_pattern, get_text)

            # Extract the information
            hospital_name = name_match.group(1).strip() if name_match else "Not specified"
            address = address_match.group(1).strip() if address_match else "Not specified"
            visiting_hours = visiting_hours_match.group(1).strip() if visiting_hours_match else "Not specified"
            appointment = appointment_match.group(1).strip() if appointment_match else "Not specified"
            
            
        # print(hospital_name)
        # print(address)
        # print(visiting_hours)
        # print(appointment)
        
        folder = f"doc_info/folder_{index+1}/"
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        with open(f"{folder}/{index+1}_doctor.txt", 'w') as f:
            
            f.write(f"""
                Doctor Photo       : {doc_photo.strip()} \n 
                Doctor Name        : {doc_name.strip()} \n
                Doctor Degree      : {doc_degree.strip()} \n
                Doctor Speciality  : {doc_speciality.strip()} \n
                Doctor Designation : {doc_designation.strip()} \n
                Doctor Workplace   : {doc_workplace.strip()} \n
                Hospital Name      : {hospital_name.strip()} \n
                Address            : {address.strip()} \n
                Visiting Hour      : {visiting_hours.strip()} \n
                Appointment        : {appointment.strip()} \n
                
                
              """)
        print(folder, "Information Save Successfully")
        
        # print(f"""
        #         Doctor Photo       : {doc_photo.strip()} \n 
        #         Doctor Name        : {doc_name.strip()} \n
        #         Doctor Degree      : {doc_degree.strip()} \n
        #         Doctor Speciality  : {doc_speciality.strip()} \n
        #         Doctor Designation : {doc_designation.strip()} \n
        #         Doctor Workplace   : {doc_workplace.strip()} \n
        #         Hospital Name      : {hospital_name.strip()} \n
        #         Address            : {address.strip()} \n
        #         Visiting Hour      : {visiting_hours.strip()} \n
        #         Appointment        : {appointment.strip()} \n
                
                
        #       """)
       




if __name__ == '__main__':
    doctor_information()