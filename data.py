import csv

########## FIRST-TEST ##########
class DataTestCreateAForum:
    def __init__(self, dictionary):
        self.test_case = dictionary["test_case"]
        self.url = dictionary["url"]
        self.username = dictionary["username"]
        self.password = dictionary["password"]
        self.course_name = dictionary["course_name"]
        self.forum_name = dictionary["forum_name"]
        self.forum_description = dictionary["forum_description"]
       

# Read data from .csv file
csv_file = "testcase-create-a-forum.csv"
dataTest_create_a_forum = []

with open(csv_file) as f:
    reader = csv.DictReader(f)

    for row in reader:
        dataTest_create_a_forum = dataTest_create_a_forum + [DataTestCreateAForum(row)]

########## SECOND-TEST ##########

class DataTestAddDiscuss:
    def __init__(self, dictionary):
        self.test_case = dictionary["test_case"]
        self.url = dictionary["url"]
        self.username = dictionary["username"]
        self.password = dictionary["password"]
        self.course_name = dictionary["course_name"]
        self.discuss_subject = dictionary["discuss_subject"]
        self.discuss_message = dictionary["discuss_message"]

# Read data from .csv file
csv_file = "testcase-add-a-discuss.csv"
dataTest_add_a_discuss = []

with open(csv_file) as f:
    reader = csv.DictReader(f)

    for row in reader:
        dataTest_add_a_discuss = dataTest_add_a_discuss + [DataTestAddDiscuss(row)]