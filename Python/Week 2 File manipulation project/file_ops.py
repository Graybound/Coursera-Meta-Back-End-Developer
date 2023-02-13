def read_file(file_name):
   
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            print(data)
            return data
    except Excteption as e:
        pass  # print("Error in 'read_file' function; \n",e)


def read_file_into_list(file_name):
  
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
            data_list = data
            return data_list
    except Excteption as e:
        pass  # print("Error in 'read_file_into_list' function; \n",e)


def write_first_line_to_file(file_contents, output_filename):
    
    try:
        content_list = file_contents.split('\n')
        first_line = content_list[0]
        with open(output_filename, 'w') as file:
            file.write(first_line)

    except Exception as e:
        pass  # print("Error in 'write_first_line_to_file' function; \n",e)


def read_even_numbered_lines(file_name):
   
    try:
        with open(file_name, 'r+') as file:
            data = file.readlines()
            data_list = data
            count = 0
            even_lines_data = []
            for line in data_list:
                count += 1
                if (count % 2) == 0:
                    even_lines_data.append(line)
                else:
                    pass
            return even_lines_data

    except Exception as e:
        pass  # print("Error in 'read_even_numbered_lines' function; \n", e)


def read_file_in_reverse(file_name):
   
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
            data_list = data
            data_list.reverse()
            print(data_list)
            return data_list

    except Exception as e:
        pass  # print("Error in 'read_file_in_reverse' function; \n",e)

def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
