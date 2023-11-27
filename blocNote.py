from abc import ABC, abstractmethod

class Note:
    @abstractmethod
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

class NoteText(Note):
    def __init__(self, id, title, content):
        super().__init__(id, title, content)
    
class NoteImage(Note):
    def __init__(self, id, title, content, image, format):
        super().__init__(id, title, content)
        self.image = image
        self.format = format

    def get_format(self):
        return self.format
    
    
class NoteImagePNG(NoteImage):
    def __init__(self, id, title, content, image, format):
        super().__init__(id, title, content, image, format)


class NoteImageJPG(NoteImage):
    def __init__(self, id, title, content, image, format):
        super().__init__(id, title, content, image, format)


class NoteAudio(Note):
    def __init__(self, id, title, content, audio):
        super().__init__(id, title, content)
        self.audio = audio

class NoteVideo(Note):
    def __init__(self, id, title, content, video):
        super().__init__(id, title, content)
        self.video = video

class BlocNotes:
    def __init__(self):
        self.notes = []
        self.next_id = 1

    def ajouter_note(self, title, content):
        note = Note(self.next_id, title, content)
        self.notes.append(note)
        self.next_id += 1
    
    def ajouter_note_image(self, title, content, image, format):
        note = NoteImage(self.next_id, title, content, image, format)
        self.notes.append(note)
        self.next_id += 1
    
    def ajouter_note_audio(self, title, content, audio):
        note = NoteAudio(self.next_id, title, content, audio)
        self.notes.append(note)
        self.next_id += 1
    
    def ajouter_note_video(self, title, content, video):
        note = NoteVideo(self.next_id, title, content, video)
        self.notes.append(note)
        self.next_id += 1
    

    def modifier_note(self, id, new_content):
        for note in self.notes:
            if note.id == id:
                note.content = new_content
                break

    def supprimer_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                break

    def lire_note(self, id):
        for note in self.notes:
            if note.id == id:
                print(f"ID : {note.id}")
                print(f"Titre : {note.title}")
                print(f"Contenu : {note.content}")
                if isinstance(note, NoteImage):
                    print(f"Format : {note.get_format()}")
                elif isinstance(note, NoteAudio):
                    print(f"Audio : {note.audio}")
                elif isinstance(note, NoteVideo):
                    print(f"Vidéo : {note.video}")
                print()
                break
        else:
            print("Note introuvable.")

    def lire_notes(self):
        if self.notes:
            print("Bloc-notes personnel :")
            for note in self.notes:
                print(f"ID : {note.id}")
                print(f"Titre : {note.title}")
                print(f"Contenu : {note.content}")
                if isinstance(note, NoteImage):
                    print(f"Format : {note.get_format()}")
                elif isinstance(note, NoteAudio):
                    print(f"Audio : {note.audio}")
                elif isinstance(note, NoteVideo):
                    print(f"Vidéo : {note.video}")
                print()
        else:
            print("Aucune note trouvée.")

# Exemple d'utilisation
bloc_notes = BlocNotes()

while True:
    print("Que souhaitez-vous faire ?")
    print("1. Ajouter une note")
    print("2. Modifier une note")
    print("3. Supprimer une note")
    print("4. Lire une note")
    print("5. Lire toutes les notes")
    print("6. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        ##Choix du type de note
        print("1. Note textuelle")
        print("2. Note image")
        print("3. Note audio")
        print("4. Note vidéo")
        choix_type = input("Votre choix : ")
        if choix_type == "1":
            title = input("Titre de la note : ")
            content = input("Contenu de la note : ")
            bloc_notes.ajouter_note(title, content)
        elif choix_type == "2":
            title = input("Titre de la note : ")
            content = input("Contenu de la note : ")
            image = input("Chemin de l'image : ")
            ##Choix du format de l'image
            choix_format = input("Format de l'image : ")
            bloc_notes.ajouter_note_image(title, content, image, choix_format)
        elif choix_type == "3":
            bloc_notes.ajouter_note_image(title, content, image, choix_format)
        elif choix_type == "3":
            title = input("Titre de la note : ")
            content = input("Contenu de la note : ")
            audio = input("Chemin de l'audio : ")
            bloc_notes.ajouter_note_audio(title, content, audio)
        elif choix_type == "4":
            title = input("Titre de la note : ")
            content = input("Contenu de la note : ")
            video = input("Chemin de la vidéo : ")
            bloc_notes.ajouter_note_video(title, content, video)
        else:
            print("Choix invalide. Veuillez réessayer.")
    elif choix == "2":
        id = int(input("ID de la note à modifier : "))
        new_content = input("Nouveau contenu de la note : ")
        bloc_notes.modifier_note(id, new_content)
    elif choix == "3":
        id = int(input("ID de la note à supprimer : "))
        bloc_notes.supprimer_note(id)
    elif choix == "4":
        id = int(input("ID de la note à lire : "))
        bloc_notes.lire_note(id)
    elif choix == "5":
        bloc_notes.lire_notes()
    elif choix == "6":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
