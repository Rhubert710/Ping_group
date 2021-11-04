from ping_group_class import Ping_group


def generate_pingGroups(text_file):
    '''
    returns a LIST of Ping_group objects
    '''
    with open(text_file, 'r') as f:

        current_pingGroup_object_str = ''
        objects_created_list =[]
        objects_name_list = []
        temp_object = None
        

        for line in f:

            if line[:4] =='PING':

                domain_fulll_str = line.split()[1]
                domain_var_str = line.split('.')[0][5:]
                current_pingGroup_object_str = f'{domain_var_str}_pingGroup'
                
                globals()[f'{domain_var_str}_pingGroup'] = Ping_group(domain_fulll_str)
                objects_created_list.append(globals()[current_pingGroup_object_str])
                objects_name_list.append(current_pingGroup_object_str)
            
            if 'ttl' in line:
                s_line = line.split()
                globals()[current_pingGroup_object_str].newPing = [int(s_line[0]), s_line[3], int(s_line[5].partition('=')[2]), float(s_line[6].partition('=')[2])]

            
            if 'timeout' in line:
                globals()[current_pingGroup_object_str].newPing= ['timeout']

            
        
        print(f'successfully created {len(objects_created_list)} Ping Groups: {objects_name_list}')
        return objects_created_list




my_pingGroups = generate_pingGroups('ping_out.txt')

for pg in my_pingGroups:
    print(pg)
