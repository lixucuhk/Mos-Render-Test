function doGet(e) {

 var params = e.parameter;

 var SpreadSheet = SpreadsheetApp.openById("1YXhl2c_Oe3MJyUhIgQeHBMJV1oRyS1GmJmBDpKp2fvk");
 var Sheet = SpreadSheet.getSheets()[0];
 var LastRow = Sheet.getLastRow();

 Sheet.getRange(LastRow+1, 1).setValue(params.name);

for (var i = 1; i <= 1; i++) {
    for (var j = 0; j <= 1; j++){
        Sheet.getRange(LastRow+1, 1+(i-1)*6+j+1).setValue(params["g" + i.toString()+'-q'+ j.toString()]);
    }
}

 return ContentService.createTextOutput(params.thank);
}
