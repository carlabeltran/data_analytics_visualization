Attribute VB_Name = "Module1"
  Sub CellsAndRanges():
    
    ' Inserting Data Via Cells
    Cells(2, 1).Value = "Pawn"
    Cells(2, 2).Value = "Pawn"
    Cells(2, 3).Value = "Pawn"
    Cells(2, 4).Value = "Pawn"
    Cells(2, 5).Value = "Pawn"
    Cells(2, 6).Value = "Pawn"
    Cells(2, 7).Value = "Pawn"
    Cells(2, 8).Value = "Pawn"
    
    Cells(1, 1).Value = "Rook"
    Cells(1, 2).Value = "Knight"
    Cells(1, 3).Value = "Bishop"
    Cells(1, 4).Value = "Queen"
    Cells(1, 5).Value = "King"
    Cells(1, 6).Value = "Bishop"
    Cells(1, 7).Value = "Knight"
    Cells(1, 8).Value = "Rook"
    

    ' Inserting Data Via Ranges
    
    Range("A7", "H7").Value = "Pawn"
    Range("A8").Value = "Rook"
    Range("B8").Value = "Knight"
    Range("C8").Value = "Bishop"
    Range("D8").Value = "King"
    Range("E8").Value = "Queen"
    Range("F8").Value = "Bishop"
    Range("G8").Value = "Knight"
    Range("H8").Value = "Rook"

  End Sub
