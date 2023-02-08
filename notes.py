import os
import json
from datetime import datetime
#Функция для сохранения заметок в формате JSON.
def save_notes_json(filename, notes):
    with open(filename, 'w') as f:
        json.dump(notes, f)
        
#Функция для чтения заметок из файла.
def read_notes_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

# Функция чтения списка заметок из формата json
def list_notes_json(notes):
    for noteL in notes:
        print(f"[{noteL['id']}]{noteL['title']}\n {noteL['body']}")
    print('Список заметок прочитан!')
        
#Функция для добавления новой заметки.
def add_note(notes):
    note = {'id': (len(notes)+1), 'title': input('Title: '), 'body': input('Body: '), 'date': str(datetime.now())}
    notes.append(note)
    print('Заметка добавлена!')
    return notes
    
#Функция для редактирования заметки.  
def edit_note(notes): 
    idx = int(input('Введите ID заметки для редактирования: '))
    for note in notes: 
        if note['id'] == idx: 
            note['title'] = input('Новый заголовок: ') 
            note['body'] = input('Новый текст: ') 
            print('Заметка отредактирована!')
            return notes 
    print('Заметка не найдена.') 
    return notes  
    
#Функция для удаления заметки.  
def delete_note(notes): 
    idx = int(input('Введите ID заметки для удаления: ')) 
    for i in range(len(notes)): 
        if notes[i]['id'] == idx: 
            del notes[i]
            print('Заметка удалена!')
            return notes  
    print('Заметка не найдена.')  
    return notes  
    
#Основное меню.  
def menu(): 
    filename = "notes.json"  
    notes = read_notes_json(filename)  
    while True:  
        print("""Заметки 
        1. Добавить заметку 
        2. Редактировать заметку 
        3. Список заметок
        4. Удалить заметку 
        0. Выход""")  
        choice = int(input("Введите команду: "))  
        if choice == 1:   #add note  
            notes = add_note(notes) 
            save_notes_json(filename, notes) 
        elif choice == 2: #edit note  
            notes = edit_note(notes) 
            save_notes_json(filename, notes) 
        elif choice == 3: #list note  
            list_notes_json(notes) 
        elif choice == 4: #delete note  
            notes = delete_note(notes)
            save_notes_json(filename, notes)  
        elif choice == 0: #quit 
            save_notes_json(filename, notes)  
            break  
        else:  
            print("Неверная команда!")
            
menu()