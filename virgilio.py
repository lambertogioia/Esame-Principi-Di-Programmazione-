import os


class Virgilio:

    class CantoNotFoundError(Exception):
        """ Eccezione sollevata quando il canto non è compreso tra 1 e 34 """
        pass

    def __init__(self, directory):
        self.directory = os.path.abspath(directory)  # trasformazione in un percorso assoluto
        # print("Percorso trovato con successo")

    # ES.1, 13, 14, 15, 16, 17

    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):
        """ Legge il contenuto di un canto"""

        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer")

        if not 1 <= canto_number <= 34:
            raise Virgilio.CantoNotFoundError("canto_number must be between 1 and 34")

        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:  # Gestione encoding per caratteri speciali
                lines = file.readlines()
            if num_lines is not None:
                lines = lines[:num_lines]  # slicing(nuova lista contiene parte dell'orginile)
            if strip_lines:
                # lines = [line.strip() for line in lines]
                clean_lines = []
                for line in lines:
                    clean_line = line.strip()
                    clean_lines.append(clean_line)  # ??giusto
                lines = clean_lines
            return lines
        except Exception as e:
            return f"error while opening {file_path}: {e} "

    # ES.2

    def count_verses(self, canto_number):
        """ Conta il numero di versi(righe) in un canto """

        verses_number = self.read_canto_lines(canto_number)
        return len(verses_number)

    # ES.3

    def count_tercets(self, canto_number):
        """ Conta il numero di terzine(gruppi di 3 versi) nel caso il numero di versi non è divisibile 
        per 3 non considerare i versi in eccesso e arrotondare per difetto"""

        verses_number = self.count_verses(canto_number)

        return verses_number//3

    # ES.4

    def count_word(self, canto_number: int, word: str) -> int:
        """ Restituisce il numero di occorrenze di una parola completa solo di una lettera o carattere."""

        if len(word) == 0:
            return 0
        # lo faccio diventare una stringa perchè prima era una lista
        contenuto_canto = "".join(self.read_canto_lines(canto_number))
        return contenuto_canto.count(word)

    # ES.5

    def get_verse_with_word(self, canto_number, word):
        """ Restituisce il primo verso del canto scelto contenente la parola scelta"""

        canto_verses = self.read_canto_lines(canto_number)
        for verse in canto_verses:
            if word in verse:
                return verse

        return None

    # ES.6

    def get_verses_with_word(self, canto_number, word):
        """ Il metodo restituisce una lista di tutti i versi del canto scelto in cui è presenta la parola word"""

        canto_verses = self.read_canto_lines(canto_number)
        found_verses = []
        for verse in canto_verses:
            if word in verse:
                found_verses.append(verse)
        return found_verses

    # ES.7

    def get_longest_verse(self, canto_number):
        """Il metodo restituisce il verso più lungo del Canto scelto
        se ci sono versi di uguale lunghezza restituisce il primo incontrato."""

        canto_verses = self.read_canto_lines(canto_number)
        longest_verse = ""
        for verse in canto_verses:
            stripped_verse = verse.strip()
            # Per sostituirsi al primo più lungo dovrà essere maggiore perchè la condizione di sostituzione è strettamente maggiore
            if len(stripped_verse) > len(longest_verse):
                longest_verse = stripped_verse

        return longest_verse

    # ES.8

    def get_longest_canto(self):
        """  Restituisce un dizionario due coppie chiave valore nelle quali verranno memorizzati
         rispettivamente il numero del canto più lungo e la sua lunghezza in versi. """

        longest_canto = {"canto_number": None, "canto_len": 0}

        for canto_number in range(1, 35):  # Itera su tutti i canti (da 1 a 34)
            num_versi = self.count_verses(canto_number)
            if num_versi > longest_canto["canto_len"]:
                longest_canto["canto_number"] = canto_number
                longest_canto["canto_len"] = num_versi

        return longest_canto

    # ES.9, 18

    def count_words(self, canto_number, words):
        """ Metodo restituisce un dizionario dove ogni coppia chiave-valore
         ha come chiave la parola e come valore il numero di volte che essa si presenta nel canto. """

        if not isinstance(words, list):
            raise TypeError("words deve essere uno lista")

        words_count = {}
        for word in words:
            words_count[word] = self.count_word(canto_number, word)
        return words_count

    # ES.10

    def get_hell_verses(self):
        """ Restituisce una lista contenente tutti i versi di tutti i canti
        dal primo verso all'ultimo"""

        all_verses = []
        for canto_number in range(1, 35):
            verses = self.read_canto_lines(canto_number)
            all_verses.extend(verses)
        return all_verses

    # ES.11

    def count_hell_verses(self):
        """ Restituisce il numero totale dei versi dell'inferno """

        tot_hell_verses = len(self.get_hell_verses())
        return tot_hell_verses

    # ES.12

    def get_hell_verse_mean_len(self):
        """ Restituisce una media della lunghezza di tutti i versi dell'inferno, 
        media conteggiata sulla base dei caratteri contenuti nei versi inclusi gli spazi."""

        all_verses = self.get_hell_verses()

        hell_lenght = 0
        avarage_lenght = 0
        for verse in all_verses:
            # Il metodo strip() può essere utilizzato su un elemento di una lista, a condizione che l'elemento sia una stringa.
            verse.strip()
            hell_lenght += len(verse)

        avarage_lenght = hell_lenght / len(all_verses)
        return avarage_lenght
