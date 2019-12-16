# Very VBA

* <https://www.reddit.com/r/ProgrammerHumor/comments/dxts0b/my_code_vs_the_computer/>

## 01-Ins_HelloWorld

```bash
Sub HelloWorld():
  MsgBox ("Hello World")
End Sub
```

## 02-Stu_HelloVBA

```bash
Sub ShowMessages():
    MsgBox ("This is message 1.")
    MsgBox ("This is message 2.")
    MsgBox ("This is message 3.")
End Sub
```

## 03-Ins_ButtonClicks

```bash
' Subroutine for Button 1
Sub Button1_Click()
    MsgBox ("You clicked Button 1!")
End Sub

' Subroutine for Button 2
Sub Button2_Click()
    MsgBox ("You clicked Button 2!")
End Sub
```

##  04-Stu_ChooseYourButton

```bash
Sub Button1_Click():
    MsgBox ("You chose button 1. You lose.")
End Sub

Sub Button2_Click():
    MsgBox ("You chose button 2. You win.")
End Sub
```

## 05-Ins_CellsAndRanges

```bash
Sub CellsAndRanges():
  
  ' Inserting Data Via Cells
  Cells(2, 1).Value = "Cat"
  Cells(2, 2).Value = "In"
  Cells(2, 3).Value = "The"
  Cells(2, 4).Value = "Hat"

  ' Inserting Data Via Ranges
  Range("F1").Value = "I"
  Range("F2").Value = "Am"
  Range("F3").Value = "Sam"

  ' Inserting Data Across Ranges
  Range("F5:F7") = 5

End Sub
```

## 06-Stu_ChessBoard 

```bash
Sub PopulateTopChessBoard():
    Range("A2: H2") = "Pawn"
    Range("A1: H1") = "Rook"
    Range("B1: G1") = "Knight"
    Range("C1: F1") = "Bishop"
    Range("D1") = "Queen"
    Range("E1") = "King"
End Sub

Sub PopulateBottomChessBoard():
    Cells(7, 1) = "Pawn"
    Cells(7, 2) = "Pawn"
    Cells(7, 3) = "Pawn"
    Cells(7, 4) = "Pawn"
    Cells(7, 5) = "Pawn"
    Cells(7, 6) = "Pawn"
    Cells(7, 7) = "Pawn"
    Cells(7, 8) = "Pawn"
    
    Cells(8, 1) = "Rook"
    Cells(8, 8) = "Rook"
    
    Cells(8, 2) = "Knight"
    Cells(8, 7) = "Knight"
    
    Cells(8, 3) = "Bishop"
    Cells(8, 6) = "Bishop"
    
    Cells(8, 4) = "King"
    
    Cells(8, 5) = "Queen"

        ' Setting cell color formatting
  ' ---------------------------------------
  For i = 1 To 8
    For j = 1 To 8
        If i Mod 2 = 0 Then
            If j Mod 2 <> 0 Then
                Cells(i, j).Interior.ColorIndex = 1
            End If
        Else
            If j Mod 2 = 0 Then
            Cells(i, j).Interior.ColorIndex = 1
            End If
        End If
    Next j
  Next i
  
  ' Setting text color
  ' ---------------------------------------
  Range("a1:h2").Font.ColorIndex = 3
  Range("a1:h2").Font.Bold = True
  
  Range("a7:h8").Font.ColorIndex = 5
  Range("a7:h8").Font.Bold = True
  
  ' Setting cell height and width
  Range("a1:h8").RowHeight = 60
  Range("a1:h8").ColumnWidth = 20
End Sub
```

## 07-Ins_Variables

```bash
Sub Variables():

    ' Basic String Variable
    ' ----------------------------------------
    Dim name As String
    name = "Gandalf"

    MsgBox (name)

    ' Basic String Concatenation (Combination)
    ' ----------------------------------------
    Dim title As String
    title = "The Great"

    Dim fullname As String
    fullname = name + " " + title

    MsgBox (fullname)

    ' Basic Integer, Double, Long Variables
    ' ----------------------------------------
    Dim age1 As Integer
    Dim age2 As Integer
    age1 = 5
    age2 = 10

    Dim price As Double
    Dim tax As Double
    price = 19.99
    tax = 0.05

    Dim lightspeed As Long
    lightspeed = 299792458

    ' Basic Numeric manipulation
    ' ----------------------------------------
    MsgBox (age1 + age2)
    Cells(1, 1).Value = price * (1 + tax)

    ' String, Numeric Combination (Casting)
    ' ----------------------------------------
    MsgBox ("I am " + Str(age1) + " years old.")

    ' Booleans
    ' ----------------------------------------
    Dim money_grows_on_trees As Boolean
    money_grows_on_trees = False

End Sub
```

## 08-Stu_TotalCalculator

```bash
Sub Calculator():
    Dim Price As Double
    Dim Tax As Double
    Dim Quantity As Double
    Dim Total As Double
    
    Price = Range("B2").Value
    Tax = Range("C2").Value
    Quantity = Range("D2").Value
    
    Total = Price * (1 + Tax) * Quantity
    
    Range("E2").Value = Round(Total, 2)
    
    MsgBox ("Your total is $" + Str(Total))
    
End Sub
```

#  09-Ins_Arrays

```bash
Sub SimpleArrays():
    
    ' Basic Array Example
    ' ------------------------------------------
    ' Create the Ingredients Array
    Dim Ingredients(5) As String

    ' Add Ingredients to the Array
    Ingredients(0) = "Chocolate Bar"
    Ingredients(1) = "Peanut Butter"
    Ingredients(2) = "Jelly"
    Ingredients(3) = "Macaroni"
    Ingredients(4) = "Potato Salad"
    Ingredients(5) = "Dragonfruit"

    ' Retrieve specific elements of the array
    MsgBox (Ingredients(4))
    MsgBox (Ingredients(0))

End Sub
```

# 10-Ins_Splitting

```bash
Sub SimpleArrays():
    
    ' String Splitting Example
    ' ------------------------------------------
    Dim Words() As String
    Dim Shakespeare As String
    Shakespeare = "To be or not to be. That is the question"

    ' Break apart the Shakespeare quote into individual words
    Words = Split(Shakespeare, " ")

    ' Print individual word
    MsgBox (Words(5))

End Sub
```

## 11-Stu_SentenceBreaker

```bash
Sub SentenceBreaker()

    ' Retrieve the user sentence and store in variable
    Dim Sentence As String
    Sentence = Cells(1, 2).Value
    MsgBox (Sentence)

    ' Retrieve the user word numbers and store in variables
    Dim num1 As Integer
    Dim num2 As Integer
    Dim num3 As Integer

    num1 = Cells(4, 1).Value
    num2 = Cells(5, 1).Value
    num3 = Cells(6, 1).Value

    MsgBox (num1)
    MsgBox (num2)
    MsgBox (num3)

    ' Split the user's sentence into words
    Dim SentenceArray() As String
    SentenceArray = Split(Sentence, " ")

    ' Use the word numbers to retrieve the specific words in the sentence
    ' Remember to offset by the 0 index
    Cells(4, 2).Value = SentenceArray(num1 - 1)
    Cells(5, 2).Value = SentenceArray(num2 - 1)
    Cells(6, 2).Value = SentenceArray(num3 - 1)
    

End Sub
```

##  12-Ins_Conditionals

```bash
Sub Conditionals():

    ' Simple Conditional Example
    ' ------------------------------------------
    If Range("A2").Value > Range("B2").Value Then
        MsgBox ("Num 1 is greater than Num 2")
    End If

    ' Simple Conditional with If, Else, and Elseif
    ' ------------------------------------------
    If Range("A5").Value > Range("B5").Value Then
        MsgBox ("Num 3 is greater than Num 4")

    ElseIf Range("A5").Value < Range("B5").Value Then
        MsgBox ("Num 4 is greater than Num 3")

    Else
        MsgBox ("Num 3 and Num 4 are equal")

    End If

    ' Conditional with Operators (And)
    ' ------------------------------------------
    If (Range("A8").Value > Range("C8").Value And Range("B8").Value > Range("C8").Value) Then
        MsgBox ("Both Num 5 and Num 6 are greater than Num 7")
    End If

    ' Conditional with Operators (OR)
    ' ------------------------------------------
    If (Range("A8").Value > Range("C8").Value Or Range("B8").Value > Range("C8").Value) Then
        MsgBox ("Either Num 5 and/or Num 6 is greater than Num 7")
    End If

End Sub
```

##  13-Stu_ChooseYourStory

```bash
Sub ChooseJourney():

Dim journey_value As Integer

journey_value = Range("E1").Value

If journey_value = 1 Then
    MsgBox ("You choose to enter the wooded forest of doom!")

ElseIf journey_value = 2 Then
    MsgBox ("You choose to enter the fiery volcano of doom!")

ElseIf journey_value = 3 Then
    MsgBox ("You choose to enter the terrifying jungle of doom!")

ElseIf journey_value = 4 Then
    MsgBox ("You choose to enter the mystery jungle of doom!")

Else
    MsgBox ("Try following directions!")
    
End If
    
End Sub
```
