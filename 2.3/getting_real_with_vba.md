# Getting real with vba

## 01-Stu_StarsCounter

* <https://dedicatedexcel.com/how-to-find-the-last-row-with-excel-vba/>

```bash
Sub StarCounter()

    Dim Total As Integer
    Dim NumberRows As Integer
    
    NumberRows = Range("A1").End(xlDown).Row
    
    For i = 2 To NumberRows
        Total = 0
        For j = 4 To 8
        
            If Cells(i, j).Value = "Full-Star" Then
                Total = Total + 1
                Cells(i, 9).Value = Total
            End If
            
        Next j
    
    Next i
              
End Sub
```

```bash
Sub CalculateTotal():
    Dim number_stars As Integer
    Dim last_row As Integer
    
    last_row = Cells(Rows.Count, 1).End(xlUp).Row
    
    For i = 2 To last_row
        
        number_stars = 0
        
        For j = 4 To 8
        
            If Cells(i, j).Value = "Full-Star" Then
                number_stars = number_stars + 1
            End If
        Next j
        
        Cells(i, 9).Value = number_stars
        
    Next i
                     
End Sub
```

## 02-Ins_Formatter

```bash
  Sub formatter()

  ' Set the Font color to Red
  Range("A1").Font.ColorIndex = 3

  ' Set the Cell Colors to Red
  Range("A2:A5").Interior.ColorIndex = 3

  ' Set the Font Color to Green
  Range("B1").Font.ColorIndex = 4

  ' Set the Cell Colors to Green
  Range("B2:B5").Interior.ColorIndex = 4

  ' Set the Color Index to Blue
  Range("C1").Font.ColorIndex = 5

  ' Set the Cell Colors to Blue
  Range("C2:C5").Interior.ColorIndex = 5

  ' Set the Color Index to Magenta
  Range("D1").Font.ColorIndex = 7

  ' Set the Cell Colors to Magenta
  Range("D2:D5").Interior.ColorIndex = 7

  ' See this website for color guides: ttp://dmcritchie.mvps.org/excel/colors.htmh
End Sub
```

## 03-Stu_Gradebook

```bash
Sub Calculate_Grade()

    Dim grade As Integer
    Dim pass As String
    Dim fail As String
    Dim warning As String
    Dim letter_grade As String
    
    grade = Range("B2").Value
    pass = "pass"
    fail = "fail"
    warning = "warning"
    
    
    If grade >= 90 Then
        Range("D2").Value = "A"
        Range("C2").Value = pass
        Range("C2").Interior.ColorIndex = 4
    ElseIf grade >= 80 And grade <= 89 Then
        Range("D2").Value = "B"
        Range("C2").Value = pass
        Range("C2").Interior.ColorIndex = 4
    ElseIf grade >= 70 And grade <= 79 Then
        Range("D2").Value = "C"
        Range("C2").Value = warning
        Range("C2").Interior.ColorIndex = 6
    ElseIf grade < 70 Then
        Range("D2").Value = "F"
        Range("C2").Value = fail
        Range("C2").Interior.ColorIndex = 3
    End If
    

End Sub


Sub Reset()
    
    Range("B13").Value = Range("B2").Value
    Range("C13").Value = Range("C2").Value
    Range("D13").Value = Range("D2").Value
    
    
    Range("B2").Value = ""
    Range("C2").Value = ""
    Range("D2").Value = ""
    Range("C2").ClearFormats
End Sub
```

## 04-Stu_Checkerboard

```bash
' even rows --> odd columns will be black, even columsn will be red
' odd rows --> odd columns will be red, even columns will be black

Sub BuildCheckerboard()
    For i = 1 To 8
    
        If i Mod 2 = 0 Then
        
            For j = 1 To 8
            
                If j Mod 2 = 0 Then
                
                    Cells(i, j).Interior.ColorIndex = 3
                    
                Else
                
                    Cells(i, j).Interior.ColorIndex = 1
                    
                End If
                    
            Next j
            
        Else
        
    
            For j = 1 To 8
            
                If j Mod 2 = 0 Then
                
                    Cells(i, j).Interior.ColorIndex = 1
                    
                Else
                
                    Cells(i, j).Interior.ColorIndex = 3
                    
                End If
                    
            Next j
    
        End If
    Next i

End Sub
```

## 05-Ins_NextCells

```bash
Sub NextCells()

  ' Set a variable for specifying the column of interest
  Dim column As Integer
  column = 1

  ' Loop through rows in the column
  For i = 2 To 6

    ' Searches for when the value of the next cell is different than that of the current cell
    If Cells(i + 1, column).Value <> Cells(i, column).Value Then

      ' Message Box the value of the current cell and value of the next cell
      MsgBox (Cells(i, column).Value & " and then " & Cells(i + 1, column).Value)

    End If

  Next i

End Sub
```

## 06-Stu_CreditCardChecker

```bash
Sub CreditCardChecker():
    Dim last_row As Integer
    Dim current_column As Integer
    Dim brand As String
    Dim number_brands As Integer
    Dim total_charged As Integer
    
    last_row = Cells(Rows.Count, 1).End(xlUp).Row
    current_column = 1
    brand = ""
    number_brands = 0
    total_charged = 0

    For i = 2 To last_row
    
        brand = Cells(i, current_column).Value
        total_charged = total_charged + Cells(i, 3).Value
    
        If Cells(i + 1, current_column).Value <> brand Then
            number_brands = number_brands + 1
            Cells(number_brands + 1, 7) = brand
            Cells(number_brands + 1, 8) = total_charged
            total_charged = 0
        End If
        
    Next i
        

End Sub
```

```bash
Sub CalculateTotal()

    Dim number_rows As Integer
    Dim credit_total As Double
    Dim brand As String
    Dim number_brands As Integer
    
    number_rows = Range("A2").End(xlDown).Row
    
    number_brands = 0
    credit_total = 0
    brand = ""
    
    For i = 2 To number_rows
    
        If i = 2 Then
            brand = Cells(2, 1).Value
            credit_total = credit_total + Cells(2, 3).Value

        
        ElseIf Cells(i + 1, 1).Value = Cells(i, 1).Value Then
        
            brand = Cells(i, 1).Value
            credit_total = credit_total + Cells(i, 3).Value
            
        Else
        
            number_brands = number_brands + 1
            Cells(1 + number_brands, 7).Value = brand
            Cells(1 + number_brands, 8).Value = credit_total
            credit_total = Cells(i + 1, 3).Value
            brand = Cells(i + 1, 1).Value
            
        End If
        
    Next i

End Sub
```

## 07-Stu_WellsFargo_Pt1

* <https://stackoverflow.com/questions/19323343/get-a-worksheet-name-using-excel-vba/19323571>
* <https://www.thespreadsheetguru.com/the-code-vault/2014/5/7/insert-single-or-multiple-excel-columns-with-vba>
* <https://stackoverflow.com/questions/11926972/excel-vba-finding-the-last-column-with-data>
* <https://support.microsoft.com/en-us/help/142126/macro-to-loop-through-all-worksheets-in-a-workbook>

```bash
Sub WellsFargo():
    Dim active_sheet_name As String
    Dim active_sheet_name_array() As String
    Dim state As String
    Dim last_row As Integer
    Dim header_array() As String
    Dim currency_value As Double
    Dim last_column As Integer
    
    For Each Worksheet In Worksheets

        sheetname = Worksheet.Name
        MsgBox (sheetname)
        active_sheet_name_array = Split(sheetname, "_")
        state = active_sheet_name_array(0)
        last_row = Worksheet.Cells(Rows.Count, 1).End(xlUp).Row
        
        Worksheet.Columns("A:A").Insert Shift:=xlToRight
        
        last_column = Worksheet.Cells(1, Columns.Count).End(xlToLeft).Column
        
        For i = 1 To last_row
        
            If i = 1 Then
                Worksheet.Cells(i, 1).Value = "State"
            Else
                Worksheet.Cells(i, 1).Value = state
            End If
            
        Next i
        
        For j = 3 To last_column
        
        header_array = Split(Worksheet.Cells(1, j).Value, " ")
        Worksheet.Cells(1, j).Value = header_array(3)
            
        Next j
        
        For i = 2 To last_row
        
            For j = 3 To last_column
            
                Worksheet.Cells(i, j).NumberFormat = "$#,##0.00"
                
            
            Next j
            
        Next i
        
    Next Worksheet
    
End Sub
```

```bash
Sub WellsFargo()
    Dim worksheet_name As String
    Dim name_array() As String
    Dim number_rows As Integer
    Dim header_year_arry() As String
    
    worksheet_name = ActiveWorkbook.Worksheets(1).Name
    
    name_array = Split(worksheet_name, "_")
    
    worksheet_name = name_array(0)
    
    MsgBox (worksheet_name)
    
    ' Columns("A:A").Insert Shift:=xlToRight
    
    number_rows = 32
    
    Range("A1").Value = "State"
    
    For i = 2 To number_rows
    
        Cells(i, 1).Value = worksheet_name
        
    Next i
    
    For i = 3 To 7
    
        header_year_array = Split(Cells(1, i).Value, " ")
    
        Cells(1, i).Value = header_year_array(3)
        
    Next i
    
    For i = 2 To number_rows
    
        For j = 3 To 7
        
            Cells(i, j).Value.Style = "Currency"
            
        Next j
        
    Next i
        

End Sub
```