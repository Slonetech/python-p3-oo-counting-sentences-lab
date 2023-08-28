class MyString:
    def __init__(self, value="string."):
        self.value = value
    @property
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        self.value.count('.') + self.value.count('?') + self.value.count('!')

