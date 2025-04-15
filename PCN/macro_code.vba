
'--- Macro: RCPSORT ---
' This macro trims and cleans the raw pricing data from RCP Input sheet
' and transfers it to usable columns for processing.
Sub RCPSORT()
    Dim wsInputData As Worksheet
    Dim wsRCPInput As Worksheet
    Dim lastRow As Long

    ' Set worksheet references
    Set wsRCPInput = ThisWorkbook.Sheets("RCP Input")
    Set wsInputData = ThisWorkbook.Sheets("Input Data")

    ' Find the last row with data in column AE
    lastRow = wsRCPInput.Cells(wsRCPInput.Rows.Count, "AE").End(xlUp).Row

    ' Apply TRIM formula to remove extra spaces from AE to AG
    With wsRCPInput
        .Range("AE27:AE" & lastRow).FormulaR1C1 = "=TRIM(RC[-29])"
        .Range("AF27:AF" & lastRow).FormulaR1C1 = "=TRIM(RC[-29])"
        .Range("AG27:AG" & lastRow).FormulaR1C1 = "=TRIM(RC[-29])"

        ' Copy cleaned data and paste it as values into column B
        .Range("AE27:AG" & lastRow).Copy
        .Range("B27").PasteSpecial Paste:=xlPasteValues
        Application.CutCopyMode = False
    End With

    ' Activate Input Data sheet after cleanup
    wsInputData.Activate
End Sub

'--- Macro: Import ---
' This macro transfers the daily updated RCP data from the raw import area
' into the main processing range in the Input Data sheet
Sub Import()
    Dim wsRCPInput As Worksheet
    Dim wsInputData As Worksheet

    ' Set references to the RCP Input and Input Data sheets
    Set wsRCPInput = ThisWorkbook.Sheets("RCP Input")
    Set wsInputData = ThisWorkbook.Sheets("Input Data")

    ' Clear the old input data
    wsInputData.Range("A26:J786").ClearContents

    ' Copy new data from RCP Input and paste as values
    wsRCPInput.Range("A26:J786").Copy
    wsInputData.Range("A26:J786").PasteSpecial Paste:=xlPasteValues
    Application.CutCopyMode = False
End Sub
