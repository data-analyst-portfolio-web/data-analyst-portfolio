
'--- Macro: RCPSORT ---
Sub RCPSORT()
    Dim wsInputData As Worksheet
    Dim wsRCPInput As Worksheet
    Dim lastRow As Long

    ' Set worksheet references
    Set wsRCPInput = ThisWorkbook.Sheets("RCP Input")
    Set wsInputData = ThisWorkbook.Sheets("Input Data")

    ' Find the last row with data in column AE
    lastRow = wsRCPInput.Cells(wsRCPInput.Rows.Count, "AE").End(xlUp).Row

    ' Trim columns AE to AG and copy to column B
    With wsRCPInput
        .Range("AE27:AE" & lastRow).FormulaR1C1 = "=TRIM(RC[-29])"
        .Range("AF27:AF" & lastRow).FormulaR1C1 = "=TRIM(RC[-29])"
        .Range("AG27:AG" & lastRow).FormulaR1C1 = "=TRIM(RC[-29])"
        .Range("AE27:AG" & lastRow).Copy
        .Range("B27").PasteSpecial Paste:=xlPasteValues
        Application.CutCopyMode = False
    End With

    wsInputData.Activate
End Sub

'--- Macro: Import ---
Sub Import()
    Dim wsRCPInput As Worksheet
    Dim wsInputData As Worksheet

    Set wsRCPInput = ThisWorkbook.Sheets("RCP Input")
    Set wsInputData = ThisWorkbook.Sheets("Input Data")

    wsInputData.Range("A26:J786").ClearContents
    wsRCPInput.Range("A26:J786").Copy
    wsInputData.Range("A26:J786").PasteSpecial Paste:=xlPasteValues
    Application.CutCopyMode = False
End Sub
