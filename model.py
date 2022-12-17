
def import_data(data, sep=None):
    with open('phone.txt', 'a+', encoding='utf-8') as file_txt, open('phone.csv', 'a+', encoding='utf-8') as file_csv:
        if sep == None:
            for i in data:
                file_txt.write(f"{i}\n")
                file_csv.write(f"{i}\n")
            file_txt.write(f"\n")
            file_csv.write(f"\n")
        else:
            file_txt.write(sep.join(data))
            file_csv.write(sep.join(data))
            file_txt.write(f"\n")
            file_csv.write(f"\n")

def export_data():
    with open('phone.txt', 'r', encoding='utf-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data

    


def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None    