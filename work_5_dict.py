# TAsk_1
names = input("Name: ")

def famliy(names):
    if names == "Darth Vader":
        return 'Luke, I am your father.'
    elif names == "Leia":
        return "Luke, I am your sister."
    elif names == "Han":
        return "Luke, I am your brather."
    else: return "bilmadim endi🤷🤷🤷"

print(famliy(names))



# Task_2
def get_budgets(lst):
    result = 0
    for x in lst:
        # result += x["budget"]
        result += x.get("budget")
    return result

print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]))



# Task_3
def get_student_names(students, list):
    for x in students.values():
        list.append(x)
    return list

print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}, []))



# TAsk_4
def resalt(dict, resalt1):
  for x in dict:
    for i in x.values():
      if type(i) == int:
        resalt1 = resalt1 + i
  return resalt1

print(resalt([
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
], 0))



# Task_5
# CHIQMADI AFSUSKI



# TASK_6
def mapping(harflar):
    a = {}
    for harf in harflar:
        a[harf] = harf.upper()
    return a
print(mapping(["a", "v", "y", "z"]))



# Task_7
def LETTERS(person, nums, list, list2, resalt):
    s = " ".join(person).split()
    for x in s:
        if x in nums:
            list.append(x)
        else:
            list2.append(x)
    resalt.update({"LETTERS": len(list2), 'DIGITS': len(list)})
    return resalt
print(LETTERS("H3ll0 Wor1d", ['1', '2', '3', '4', '5', '6', '7', '8', '9',], [], [], {}))



# TAsk_8
def sport(object, num, rer):
    for x in object.values():
        rer = rer + x
        rresalt = rer - int(num)
    return rresalt
print(sport({"basketball": 12, "football": 10, "tennis": 20}, input("Num: "), 0))



# TAsk_9
# Chiqmagan



# TAsk_10
# chiqmadi

