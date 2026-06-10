def save_code_to_file(

    filename,

    code
):

    with open(filename, "w") as f:

        f.write(code)

    return "File saved successfully"

def read_file(filename):

    with open(filename, "r") as f:

        return f.read()