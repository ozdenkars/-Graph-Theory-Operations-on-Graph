import sys
smn= sys.argv[1]
commands=sys.argv[2]
with open("smn.txt", "r",encoding="utf-8") as smn:
    smn_list=[]
    for line in smn.readlines():
        line = line.rstrip()
        line = line.split(":")
        smn_list.append(line)
    smn_dict={}
    for i in range(len(smn_list)):
        smn_dict[smn_list[i][0]]=smn_list[i][1].split()
with open ("commands.txt", "r",encoding="utf-8") as command:
    command_list=[]
    for line in command.readlines():
        line=line.rstrip()
        line= line.split()
        command_list.append(line)
output_list=[]
def ANU(username):
    if username in smn_dict.keys():
        x='ERROR: Wrong input type! for "ANU"! -- This user already exists!!'
        output_list.append(x)
    else:
        smn_dict[username] = []
        x= 'User ' + "'"+username+"'" + ' has been added to the social network successfully'
        output_list.append(x)
def DEU(username):
    if username in smn_dict.keys():
        del smn_dict[username]
        a=smn_dict.values()
        for key in smn_dict.keys():
            if username in smn_dict[key]:
                smn_dict[key].remove(username)
        x='User '+"'"+username+"'" +' and his/her all relations have been deleted successfully'
        output_list.append(x)
    else:
        x='ERROR: Wrong input type! for "DEU"!--There is no user named '+"'"+username+"'" +' !!'
        output_list.append(x)
def ANF(sourceuser,targetuser):
    if not sourceuser in smn_dict.keys() and targetuser in smn_dict.keys():
        x= 'ERROR: Wrong input type! for "ANF"! -- No user named '+"'"+sourceuser+"'"+' found!!'
        output_list.append(x)
    elif not (targetuser in smn_dict.keys()) and sourceuser in smn_dict.keys():
        x= 'ERROR: Wrong input type! for "ANF"! -- No user named ' + "'" + targetuser+"'" + ' found!!'
        output_list.append(x)
    elif not sourceuser in smn_dict.keys() and not targetuser in smn_dict.keys():
        x = 'ERROR: Wrong input type! for "ANF"! -- No user named ' +"'"+ sourceuser + "'"+ ' and ' +"'"+ targetuser +"'"+ ' found!'
        output_list.append(x)
    elif sourceuser in smn_dict[targetuser] or targetuser in smn_dict[sourceuser]:
        x='ERROR: A relation between '+"'"+ sourceuser +"'"+ ' and '+"'"+ targetuser + "'"+' already exists!!'
        output_list.append(x)
    elif (sourceuser in smn_dict.keys()) and (targetuser in smn_dict.keys()):
        smn_dict[sourceuser].append(targetuser)
        smn_dict[targetuser].append(sourceuser)
        x= 'Relation between '+ "'"+ sourceuser +"'" + ' and ' +"'"+ targetuser + "'"+ ' has been added successfully'
        output_list.append(x)
def DEF(sourceuser,targetuser):
    if not (sourceuser in smn_dict.keys()) and (targetuser in smn_dict.keys()):
        x = 'ERROR: Wrong input type! for "DEF"! -- No user named ' + "'" + sourceuser + "'" + ' found!!'
        output_list.append(x)
    elif not (targetuser in smn_dict.keys()) and (sourceuser in smn_dict.keys()):
        x = 'ERROR: Wrong input type! for "DEF"! -- No user named ' +"'"+ targetuser +"'"+' found!!'
        output_list.append(x)
    elif targetuser in smn_dict.keys() and sourceuser in smn_dict.keys() and not sourceuser in smn_dict[targetuser]:
        x = 'ERROR: No relation between '+"'"+ sourceuser + "'"+' and '+ "'"+ targetuser + "'"+ ' found!!'
        output_list.append(x)
    elif (not (sourceuser in smn_dict.keys())) and (not (targetuser in smn_dict.keys())):
        x = 'ERROR: Wrong input type! for "DEF"! -- No user named ' + "'" + sourceuser + "'" + ' and ' + "'" + targetuser + "'" + ' found!'
        output_list.append(x)
    elif sourceuser in smn_dict.keys() and targetuser in smn_dict.keys() and sourceuser in smn_dict[targetuser]:
        smn_dict[sourceuser].remove(targetuser)
        smn_dict[targetuser].remove(sourceuser)
        x = 'Relation between '+ "'"+ sourceuser + "'"+' and '+ "'"+ targetuser + "'"+ ' has been deleted successfully'
        output_list.append(x)
def CF(username):
    if username in smn_dict.keys():
        number= len(smn_dict[username])
        x='User '+"'"+ username + "'"+' has '+ str(number)+' friends'
        output_list.append(x)
    else:
        x='ERROR: Wrong input type! for "CF"! -- No user named '+"'"+ username +"'"+' found!'
        output_list.append(x)
def FPF(username,maximum_distance):
    possible_friend = []
    if not username in smn_dict.keys():
        x='ERROR: Wrong input type! for "FPF"! -- No user named '+"'"+ username +"'"+' found!'
        output_list.append(x)
    elif username in smn_dict.keys() and maximum_distance == "1":
        possible_friend= smn_dict[username]
        possible_friend.sort()
        count= len(possible_friend)
        x='User '+"'"+ username + "'"+ ' has '+ str(count) + ' possible friends when maximum distance is 1'
        output_list.append(x)
        y= 'These possible friends: ' + "{"+str(possible_friend)[1:-1]+"}"
        output_list.append(y)
    elif username in smn_dict.keys() and maximum_distance == "2":
        set1 = set(smn_dict[username])
        for user in smn_dict[username]:
            set1.update(set(smn_dict[user]))
        possible_friend = list(set1)
        possible_friend.sort()
        possible_friend.remove(username)
        count = len(possible_friend)
        x = 'User ' + "'" + username + "'" + ' has ' + str(count) + ' possible friends when maximum distance is 2'
        output_list.append(x)
        y = 'These possible friends: ' + "{"+str(possible_friend)[1:-1]+"}"
        output_list.append(y)
    elif username in smn_dict.keys() and maximum_distance == "3":
        set1 = set(smn_dict[username])
        for user in smn_dict[username]:
            set1.update(set(smn_dict[user]))
        sety= set()
        for user in set1:
            sety.update(set(smn_dict[user]))
        possible_friend = list(sety)
        possible_friend.sort()
        possible_friend.remove(username)
        count = len(possible_friend)
        x = 'User ' + "'" + username + "'" + ' has ' + str(count) + ' possible friends when maximum distance is 3'
        output_list.append(x)
        y = 'These possible friends: ' + "{"+str(possible_friend)[1:-1]+"}"
        output_list.append(y)
    else:
        x= "ERROR: Maximum distance is out of range!!"
        output_list.append(x)

def SF(username,mutual_degree):
    if not username in smn_dict.keys():
        x= 'Error: Wrong input type! for "SF"! -- No user named '+ "'" + username + "'" + ' found!!'
        output_list.append(x)
    elif int(mutual_degree) <=1 or int(mutual_degree) > 4:
        x='Error: Mutually Degree cannot be less than or equal 1 or greater than 4'
        output_list.append(x)
    elif username in smn_dict.keys() and (int(mutual_degree) >1 and int(mutual_degree) <= 4) :
        ref_list = smn_dict[username]
        suggest_friend=[]
        x = 'Suggestion List for '+ "'" + username + "'" + ' (when MD is '+ str(mutual_degree)+ '):'
        output_list.append(x)
        total_friend = []
        set1 = set()
        for name in ref_list:
            total_friend.extend(smn_dict[name])
        for name in ref_list:
            set1.update(set(smn_dict[name]))
        set1.remove(username)
        list1= list(set1)
        list1.sort()
        for name in list1:
            mutual= total_friend.count(name)
            if mutual== 2 and int(mutual_degree)<=2:
                y = "'" +username+ "'"+ ' has 2 mutual friends with '+ "'" +name+"'"
                output_list.append(y)
                suggest_friend.append(name)
            elif mutual==3 and int(mutual_degree)<=3:
                y = "'" + username + "'" + ' has 3 mutual friends with ' + "'" + name + "'"
                output_list.append(y)
                suggest_friend.append(name)
            elif mutual==4 and int(mutual_degree)<=4:
                y = "'" + username + "'" + ' has 4 mutual friends with ' + "'" + name + "'"
                output_list.append(y)
                suggest_friend.append(name)
            elif mutual>4 and int(mutual_degree)<4:
                y = "'" + username + "'" + ' has more than 4 mutual friends with ' + "'" + name + "'"
                output_list.append(y)
                suggest_friend.append(name)
        suggest_friend.sort()
        z ='The suggested friends for '+ "'"+username+"' :" + str(suggest_friend)[1:-1]
        output_list.append(z)
for i in range(len(command_list)):
    if command_list[i][0]== "ANU":
        ANU(command_list[i][1])
    elif command_list[i][0]== "DEU":
        DEU(command_list[i][1])
    elif command_list[i][0] == "ANF":
        ANF(command_list[i][1],command_list[i][2])
    elif command_list[i][0] == "DEF":
        DEF(command_list[i][1],command_list[i][2])
    elif command_list[i][0] == "CF":
        CF(command_list[i][1])
    elif command_list[i][0] == "FPF":
        FPF(command_list[i][1],command_list[i][2])
    elif command_list[i][0] == "SF":
        SF(command_list[i][1], command_list[i][2])
    else:
        break
with open("output.txt","w") as output:
    output.write("Welcome to Assignment 3"+"\n"+"-------------------------------"+"\n")
    for i in range(len(output_list)):
        output.write(output_list[i]+"\n")