import json, operator
with open('output.json', 'w') as output_file:
    data_file = open('auth_data.txt', 'r')
    users = []
    comps = []
    links_users = []
    links_comps = []
    comp_dict = {}
    src_comp_counts = {}
    dest_comp_counts = {}
    comp_connections = {}
    users_dict = {}
    iteration_u = 0
    iteration_c = 0
    for line in data_file:
        no_newline_char = line.split('\n')
        line_data = no_newline_char[0].split(',')
        if len(line_data) < 4:
            break
        if line_data[0] != line_data[1]:
            users.append({"name":line_data[0], "group": 1})
            users.append({"name":line_data[1], "group": 2})
            links_users.append({"source":iteration_u*2, "target":(iteration_u*2)+1, "value": 1})
            iteration_u += 1
        if line_data[2] != line_data[3]:
            if line_data[2] in src_comp_counts and line_data[3] in dest_comp_counts:
                index1 = comp_dict.get(line_data[2])
                index2 = comp_dict.get(line_data[3])
                src_comp_counts[line_data[2]] = src_comp_counts.get(line_data[2]) + 1
                dest_comp_counts[line_data[3]] = dest_comp_counts.get(line_data[3]) + 1
                src_list = comp_connections.get(line_data[2])
                dest_list = comp_connections.get(line_data[3])
                src_list.append(line_data[3])
                dest_list.append(line_data[2])
                comp_connections[line_data[2]] = src_list
                comp_connections[line_data[3]] = dest_list
                links_comps.append({"source":index1, "target":index2, "value": 1})
            elif line_data[2] in src_comp_counts and line_data[3] not in dest_comp_counts:
                index = comp_dict.get(line_data[2])
                src_comp_counts[line_data[2]] = src_comp_counts.get(line_data[2]) + 1
                dest_comp_counts[line_data[3]] = 1
                src_list = comp_connections.get(line_data[2])
                src_list.append(line_data[3])
                comp_connections[line_data[2]] = src_list
                comp_connections[line_data[3]] = [line_data[2]]
                comp_dict[line_data[3]] = iteration_c
                comps.append({"name":line_data[3], "group": 2})
                links_comps.append({"source":index, "target":(iteration_c*2)+1, "value": 1})
                iteration_c += 1
            elif line_data[2] not in src_comp_counts and line_data[3] in dest_comp_counts:
                index = comp_dict.get(line_data[3])
                src_comp_counts[line_data[2]] = 1
                comp_connections[line_data[2]] = [line_data[3]]
                dest_list = comp_connections.get(line_data[3])
                dest_list.append(line_data[2])
                comp_connections[line_data[3]] = dest_list
                dest_comp_counts[line_data[3]] = dest_comp_counts.get(line_data[3]) + 1
                comp_dict[line_data[2]] = iteration_c
                comps.append({"name":line_data[2], "group": 2})
                links_comps.append({"source":iteration_c*2, "target":index, "value": 1})
                iteration_c += 1
            else:
                comp_dict[line_data[2]] = iteration_c
                comp_dict[line_data[3]] = iteration_c
                src_comp_counts[line_data[2]] = 1
                dest_comp_counts[line_data[3]] = 1
                comp_connections[line_data[2]] = [line_data[3]]
                comp_connections[line_data[3]] = [line_data[2]]
                comps.append({"name":line_data[2], "group": 1})
                comps.append({"name":line_data[3], "group": 2})
                links_comps.append({"source":iteration_c*2, "target":(iteration_c*2)+1, "value": 1})
                iteration_c += 1
    #data = {"nodes": comps, "links": links_comps}
    data_file.close()
    sorted_src = sorted(src_comp_counts.items(), key=operator.itemgetter(1))
    sorted_dest = sorted(dest_comp_counts.items(), key=operator.itemgetter(1))
    #print sorted_src
    #print sorted_dest
    #print sorted_src[-1]
    #Pair ('CS1234', 543352)
    nodes = []
    links = []
    biggest_pairs = []
    counter = -200
    total_iterations = 0
    print len(sorted_src)
    print len(sorted_dest)
    while counter != 200:
        pair_src = sorted_src[counter]
        pair_dest = sorted_dest[counter]
        if pair_src[1] > 1000000:
            nodes.append({"name": pair_src[1], "num": 1, "group": 5})
        elif pair_src[1] > 100000:
            nodes.append({"name": pair_src[1], "num": 1, "group": 4})
        elif pair_src[1] > 10000:
            nodes.append({"name": pair_src[1], "num": 1, "group": 3})
        elif pair_src[1] > 1000:
            nodes.append({"name": pair_src[1], "num": 1,  "group": 2})
        else:
            nodes.append({"name": pair_src[1], "num": 1,  "group": 1})

        if pair_dest[1] > 1000000:
            nodes.append({"name": pair_dest[1], "num": 0,  "group": 5})
        elif pair_src[1] > 100000:
            nodes.append({"name": pair_dest[1], "num": 0,  "group": 4})
        elif pair_dest[1] > 10000:
            nodes.append({"name": pair_dest[1], "num": 0,  "group": 3})
        elif pair_dest[1] > 1000:
            nodes.append({"name": pair_dest[1], "num": 0,  "group": 2})
        else:
            nodes.append({"name": pair_dest[1], "num": 0,  "group": 1})
        counter += 1
        #links.append({"source":total_iterations*2, "target":(total_iterations + 1)*2, "value": 1})
        total_iterations += 1
    #links.append({"source":0, "target":1, "value": 1})
    #links.append({"source":2, "target":3, "value": 1})
    #links.append({"source":2, "target":5, "value": 1})
    #links.append({"source":4, "target":3, "value": 1})
    #links.append({"source":6, "target":1, "value": 1})
    data = {"nodes": nodes, "links": links}
    json.dump(data, output_file, indent=2)