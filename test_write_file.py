from functions.write_file import write_file

print(f"Result for 'wait this isn't lorem ipsum':\n{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}")
print(f"Result for 'lorem ipsum dolor sit amet':\n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}")
print(f"Result for 'this should not be allowed':\n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}")