import os

def box(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def write_notes(filename, content):
    with open('notes.txt', 'w') as f:
        f.write(content)
        f.close()
    print("[SUCCESS] Notes successfully saved to 'notes.txt'.\n")

def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    else:
        print('No notes file exists')

box('STUDENTS NOTES MANAGEMENT SYSTEM')

while True:
    print('Select an operation:\n1. Write/Save Notes\n2. View Saved Notes\n3. Exit')
    choice = int(input('Enter choice (1-3): '))
    if choice == 3:
        print('Thank you for using the notes Management System. Goodbye!')
        break
    if choice == 1:
        notes = input('Enter Notes To Save: ')
        write_notes('notes.txt', notes)
    if choice == 2:
        print('---Notes Content---\n')
        print(f'{read_notes('notes.txt')}\n')

