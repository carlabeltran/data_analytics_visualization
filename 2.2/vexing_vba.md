# Vexing VBA

```bash
Sub CalculateTotal():
    Dim Budget As Double
    Dim Price As Double
    Dim Fees As Double
    Dim Total As Double
    
    Budget = Range("C3").Value
    Price = Range("F3").Value
    Fees = Range("H3").Value
    
    Total = Price * (1 + Fees)
    
    Range("L3").Value = Round(Total, 2)
    
    If Total > Budget Then
        MsgBox ("You are over budget.")
        Price = Budget / (1 + Fees)
        Range("F3").Value = WorksheetFunction.RoundDown(Price, 0)
        Range("L3").Value = Price * (1 + Fees)
    ElseIf Total < Budget Then
        MsgBox ("You are under budget.")
    End If
End Sub
```

```bash
Sub forLoop()

    Dim i As Integer
    Dim helloMessage As String
    helloMessage = "hello"
    
    ' loop through numbers 1 to 20
    For i = 1 To 20
        ' iterate through rows
        Cells(i, 1).Value = 7
        
        ' iterate through columns:
        Cells(1, i).Value = helloMessage
        
        ' use the iterator variable;
        Cells(i + 1, 2).Value = i * i
    Next i
    
End Sub
```

```bash
Sub forLoop()

    Dim i As Integer
    Dim food As String
    Dim sentence As String
    
    food = "Chicken Nuggets"
    sentence = "I will eat."
    
    For i = 1 To 10
        Cells(i, 1).Value = "I will eat."

        Cells(i, 2).Value = i + 10
        
        Cells(i, 3).Value = food
    Next i
    
End Sub
```

```bash
Sub modulo()

    ' Remainder of 0
    Cells(2, 1).Value = 4 Mod 2
    
    ' Remainder of 1
    Cells(3, 1).Value = 5 Mod 4
    
    ' Remainder of 3
    Cells(4, 1).Value = 11 Mod 8
    
    ' Remainder of 2
    Cells(5, 1).Value = 23 Mod 7
    
    ' Remainder of 5
    Cells(6, 1).Value = 24 Mod 19

End Sub
```

```bash
Sub conditional_loops()

    ' Create a for loop from 1 to 10
    For i = 1 To 10

        ' Use the modulus function to determine if a number is divisible by 2 (even number)
        If Cells(i, 1).Value Mod 2 = 0 Then

            ' Enter "Even Row" the adjacent cell
            Cells(i, 2).Value = "Even Row"
            
        ' If the number is not divisible by 2 (odd number)
        Else

            ' Enter "Even Row" the adjacent cell
            Cells(i, 2).Value = "Odd Row"
            
        ' Close the If/Else Statement
        End If

    Next i

End Sub
```

```bash
Sub FizzBuzz()
    Dim number As Integer
    
    For i = 1 To 99
        number = Cells(i + 1, 1)
        
        If number Mod 3 = 0 And number Mod 5 = 0 Then
            Cells(i + 1, 2).Value = "FizzBuzz"
        ElseIf number Mod 3 = 0 Then
            Cells(i + 1, 2).Value = "Fizz"
        ElseIf number Mod 5 = 0 Then
            Cells(i + 1, 2).Value = "Buzz"
        Else
            Cells(i + 1, 2).Value = ""
        End If
    Next i
End Sub
```

```bash
Sub FindLottoWinners()
    Dim first As Long
    Dim second As Long
    Dim third As Long
    Dim lottoNumber As Long
    Dim wild_ball_1 As Long
    Dim wild_ball_2 As Long
    Dim wild_ball_3 As Long
    
    first = 3957481
    second = 5865187
    third = 2817729
    
    wild_ball_1 = 2275339
    wild_ball_2 = 5868182
    wild_ball_3 = 1841402
    
    
    For i = 2 To 1001
        lottoNumber = Cells(i, 3)
        
        If lottoNumber = first Then
            Range("F2").Value = Cells(i, 1).Value
            Range("G2").Value = Cells(i, 2).Value
            Range("H2").Value = Cells(i, 3).Value
            MsgBox ("Congratulations, " + Cells(i, 1).Value + " " + Cells(i, 2).Value + " You are the first place winner!")
        
        ElseIf lottoNumber = second Then
            Range("F3").Value = Cells(i, 1).Value
            Range("G3").Value = Cells(i, 2).Value
            Range("H3").Value = Cells(i, 3).Value
            
        ElseIf lottoNumber = third Then
            Range("F4").Value = Cells(i, 1).Value
            Range("G4").Value = Cells(i, 2).Value
            Range("H4").Value = Cells(i, 3).Value
            
        End If
        
    Next i

        
    For i = 2 To 1001
        lottoNumber = Cells(i, 3).Value
        If lottoNumber = wild_ball_1 Or lottoNumber = wild_ball_2 Or lottoNumber = wild_ball_3 Then
            Range("F5").Value = Cells(i, 1).Value
            Range("G5").Value = Cells(i, 2).Value
            Range("H5").Value = Cells(i, 3).Value
            
            Exit For
        End If
    
    Next i
        
End Sub
```

```bash
' Nested For Loop

Sub ClassScanner()
    
    Dim TargetStudent As String
    
    ' Loop through the rows
    For i = 1 To 3

        ' Loop through the columns
        For j = 1 To 5

            ' Print the Student Name
            MsgBox ("Row: " & i & " Column: " & j & " | " & Cells(i, j).Value)

        Next j

    Next i

End Sub
```

```bash
Sub BugHunt()
    Dim number_hornets As Integer
    Dim bugs_available As Integer
    Dim number_hornets_replaced As Integer
    
    number_hornets = 0
    bugs_available = Range("K2").Value
    bees_available = Range("Q2").Value
    number_hornets_replaced = 0
    
    
    For i = 1 To 6
    
        For j = 1 To 7
        
            If Cells(i, j).Value = "Hornets" Then
                number_hornets = number_hornets + 1
                
                If bugs_available > 0 Then
                    bugs_available = bugs_available - 1
                    Cells(i, j).Value = "Bugs"
                    Range("k2").Value = bugs_available
                    number_hornets_replaced = number_hornets_replaced + 1
                ElseIf bees_available > 0 Then
                    bees_available = bees_available - 1
                    Cells(i, j).Value = "Bees"
                    Range("Q2").Value = bees_available
                    number_hornets_replaced = number_hornets_replaced + 1
                End If
            End If
            
        Next j
        
    Next i
    
    If number_hornets_replaced < number_hornets Then
        MsgBox ("Oh no! We still have hornets!")
    End If
    
    MsgBox ("Number of hornets found: " & number_hornets)

End Sub
```