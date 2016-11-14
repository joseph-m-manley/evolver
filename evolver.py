#!/bin/sh

import random
import string

class Mutator:
    def __init__(self):
        random.seed()

    def mutate(self, data, p):
        for each in range(0, p):
            charToMutate = random.randrange(0, len(l))
            data[charToMutate] = random.choice(string.ascii_letters)
        return data


class FileManager:
    def __init__(self, input, output):
        self.readPath = input
        self.writePath = output

    def get(self):
        text = ''
        with open(self.readPath, 'r') as f:
            text = f.read()
        return text

    def take(self, text):
        with open(self.writePath, 'w') as f:
            f.write(text)
        

class Evolver:
    def __init__(self, randomizer, fileManager):        
        self.fileManager = fileManager
        self.randomizer = randomizer

    def prepare(self):
        self.code = self.fileManager.get()
        self.percentToMutate = len(self.code) // 100

    def evolve(self):
        result = self.randomizer.mutate(list(self.code), self.percentToMutate)
        self.code =  "".join(result)

    def finish(self):
        self.fileManager.take(self.code)


def main():
    organism = Evolver(FileManager("Original.txt", "Mutated.txt"), Mutator())
    
    organism.prepare()

    organism.evolve()
    organism.evolve()
    organism.evolve()

    organism.finish()


if __name__ == "__main__":
    main()
