from contextlib import contextmanager

@contextmanager
def file_reader(path):
    try:
        # __enter__() logic
        file = open(path, 'r')
        yield file
    except Exception as e:
        print(f"Error! {e}")
    finally:
        # __exit__() logic
        print("Closing file")
        file.close()

if __name__ == "__main__":
    with file_reader("generator.py") as fr:
        for line in fr:
            print(repr(line))

