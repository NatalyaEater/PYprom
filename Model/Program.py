import Model.Classnote as Note


def write_file(array, mode):
    file = open("notes.csv", 'w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close

def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Заметок нет')
    finally:
        return array
    
def check_note(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text
    
def add():
    number=1
    title = check_note(input('Введите Название заметки: '), number)
    body = check_note(input('Введите Содержание заметки: '), number)
    note = Note.Note(title=title, body=body)
    array = read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('Заметка добавлена.')


def show(num):
    logic = True
    array = read_file()
    for notes in array:
        if num == 1:
            logic = False
            print(Note.Note.map_note(notes))
    if logic == True:
        print('Заметок нет')

def edit_show(num):
    number=1
    id = input('Введите id заметки: ')
    array = read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if num == 1:
                title = check_note(input('Введите Название заметки: '), number)
                body = check_note(input('Введите Содержание заметки: '), number)
                note = Note.Note(title=title, body=body)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена.')
            if num == 2:
                array.remove(notes)
                print('Заметка удалена.')
    if logic == True:
        print('Введите верный id')
    write_file(array, 'a')
    