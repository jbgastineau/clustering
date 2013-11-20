'''
Created on 1 nov. 2013

@author: jean-baptiste Gastineau
'''
import math
""" not used anymore
workclass = dict([(' Private', 20), (' Self-emp-not-inc', 5), (' Self-emp-inc', 10), (' Federal-gov', 18), (' Local-gov', 10),
                  (' State-gov', 8),(' Without-pay', 10),(' Never-worked', 0), ])
marital_status = dict([(' Married-civ-spouse', 20), (' Divorced', 0), (' Never-married', 10), (' Separated', 0), (' Widowed', 10),
                       (' Married-spouse-absent', 8),(' Married-AF-spouse', 10)])
occupation = dict([(' Tech-support',3), (' Craft-repair', 5), (' Other-service',5) , (' Sales', 15), (' Exec-managerial', 20),
                   (' Prof-specialty', 10), (' Handlers-cleaners', 2) , (' Machine-op-inspct',12) , (' Adm-clerical',7),
                   (' Farming-fishing',6), (' Transport-moving', 10), (' Priv-house-serv', 8), (' Protective-serv',6),
                   (' Armed-Forces',12)])
relationship = dict([(' Wife',17), (' Own-child', 5) , (' Husband',20) , (' Not-in-family',0), (' Other-relative',10),
                     (' Unmarried', 13)])
race = dict([(' White',20), (' Asian-Pac-Islander',18), (' Amer-Indian-Eskimo',5), (' Other',5), (' Black',5 )])
sex = dict([(' Female',0), (' Male',10)])
# native_country = dict([(' United-States', 51), (' Cambodia', 926), (' England',), Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
salary = dict ([(' >50K',1 ), (' <=50K', 0)])  """


def read_file (file_name) :
    ins = open( file_name, "r" )
    raw_data = []
    i = 0;
    for line in ins:
        line = line.rstrip('\n')
        fields = line.split(",")
        fields.append(i)
        i=i+1 
        raw_data.append(fields)
    ins.close()
    return raw_data

# this procedure only make use of a dictionary containing values for
# each attribute. Not used parameters are set to zero.
def Note_attributes (attributes,dictionnary) :
     
    attributes[0] = int(attributes[0]) ## age ( continuous)
    attributes[1] = dictionnary[attributes[1]] ## workclass (string)
    attributes[2] = 0 ## fnlwght (continuous)
    attributes[3] = 0 ## education (string)
    attributes[4] = int(attributes[4]) ## education (number)
    attributes[5] = dictionnary[attributes[5]] ## marital-status (string)
    attributes[6] = dictionnary[attributes[6]] ## occupation (string)
    attributes[7] = dictionnary[attributes[7]] ## relationship (string)
    attributes[8] = dictionnary[attributes[8]] ## race (string)
    attributes[9] = dictionnary[attributes[9]] ## sex (string)
    attributes[10] = int(attributes[10]) # capital-gain (continuous)
    attributes[11] = int(attributes[11]) # capital-loss ( continuous)
    attributes[12] = int(attributes[12]) # hours-per-week (continuous)
    attributes[13] = dictionnary[attributes[13]] # native country (string)
    attributes[14]= 0  # this parameter is non taken into account, just for test purpose
    return attributes


# this procedures creates automatically the good non normalized note to 
# be given to every successful attribute of the data, according to the question :
# will the sample earn more than $ 50K ? A dictionary that associate some string 
# values to notes is automatically created.
def get_attributes_notes(data):
    fields_notes={}
    for fields in data :
        if len(fields) == 16:
            for i in range(14) :
                if fields[i] in fields_notes:
                    if fields[len(fields)-1] == " >50K":
                        fields_notes[fields[i]] +=1
                else :
                    if fields[len(fields)-1] == " >50K":
                        fields_notes[fields[i]] = 1
                    else :
                        fields_notes[fields[i]] = 0  
                        
    return fields_notes
                         
      

#Notation and normalization of the data.
def split_note_data (data,dictionnary):
    
    for attributes in data :
        if '?' not in attributes and len(attributes) == 15:
            Note_attributes(attributes,dictionnary) 
            if ( attributes[14] == " >50K"):
                attributes[14] = 1
            else:
                attributes[14] = 0
    
    # computing the mean values
    means = []
    sums = []
    for i in range(len(data[0])) :
        mean = 0
        for j in range(len(data)) :
            mean = mean + data[j][i]
        sums.append(mean)
        mean = mean / len(data)
        means.append(mean)
    
    # computing the standard deviations
    sds = []
    for i in range(len(data[0])) :
        sd = 0
        for j in range(len(data)) :
            sd = sd +(data[j][i] - means[i])**2
        sd = math.sqrt(sd/ len(data))    
        sds.append(sd)
    
    # normalizing the data
    for i in range(len(data[0])) :
        for j in range(len(data)) :
            if sds[i]==0 :
                data[j][i] = 0;
            else :
                data[j][i] = (data[j][i] - means[i]) / sds[i]
    
    ##return data          



## main function
raw_data = read_file("../../data/adult.data.txt")
dictionnary = get_attributes_notes(raw_data)
print dictionnary
print "\n"
#standardize_data =  
split_note_data(raw_data,dictionnary)
print dictionnary

# at this stage of the script, standardize_data is ready to be used by a
# clustering algorithm.

