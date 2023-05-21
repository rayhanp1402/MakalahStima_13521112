from note import Note
from noteDictionary import notes

upperNoteNumber = 17 # This should correspond to the highest integer in the noteDictionary
lowerNoteNumber = -2 # This as well, this should be the lowest integer

cantusFirmus = [1, 6, 5, 10] # This can be modified as you like

result = [[]]
resultCounter = 0


def dfs(cantusFirmus, parentNote, childNote, level):
    # parentNote is an instance of Note, childNote is an integer

    currentNote = Note(childNote)
    currentNote.setParent(parentNote)
    
    interval = abs(currentNote.noteType - cantusFirmus[level]) % 12 # This calculates the half-steps of the current harmonic interval
    if(interval == 1 or interval == 2 or interval == 5 or interval == 6 or interval == 10 or interval == 11): # No Dissonant Harmonic Intervals
        return  # Cutoff
    
    steps = currentNote.noteType - parentNote.noteType  # This calculates the half-steps of the melodic interval between current and previous note
    if(steps == 0 and level > 0):
        if(interval == 0 or interval == 6 or interval == 7): # No Direct Motion to a Perfect Consonance
            return  # Cutoff

    if(level == len(cantusFirmus) - 1):
        constructCounterpoint(currentNote)
    else:
        level += 1

        for i in range(lowerNoteNumber, upperNoteNumber + 1):   # Iteration of neighbors
            dfs(cantusFirmus, currentNote, i, level)


def constructCounterpoint(note):
    global result
    global resultCounter
    
    while note.parent is not None:
        result[resultCounter].append(notes[note.noteType])
        note = note.parent

    result[resultCounter].reverse()
    result.append([])
    resultCounter += 1


def printResult():
    file_path = "output/result.txt"
    file = open(file_path, 'w')

    file.write("There are/is " + str(len(result)) + " voice leading(s) possible\n")
    file.write("Possible Voice Leadings:\n")
    for i in range(len(result)):
        file.write(str(result[i]) + "\n")

    file.close()


def main():
    rootNote = Note(1)
    for i in range(lowerNoteNumber, upperNoteNumber + 1):
        dfs(cantusFirmus, rootNote, i, 0)
    result.pop()
    printResult()


main()