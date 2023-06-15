import os

absolute_path = os.path.dirname(__file__)
print("** absolute_path :", absolute_path)

f= open("c:/Users/priya/exercise/python_exercise/basic/qs_100/projectPandas/write.txt")
content = f.read()
print("\n** file content :\n", content)