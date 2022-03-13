function doGet(e) {

 var params = e.parameter;

 var SpreadSheet = SpreadsheetApp.openById("1YXhl2c_Oe3MJyUhIgQeHBMJV1oRyS1GmJmBDpKp2fvk");
 var Sheet = SpreadSheet.getSheets()[0];
 var LastRow = Sheet.getLastRow();

 Sheet.getRange(LastRow+1, 1).setValue(params.name);

 for (var i = 1; i <= 18; i++) {
  Sheet.getRange(LastRow+1, 1+i).setValue(params["q" + i.toString()]);
 }

 return ContentService.createTextOutput(params.thank);
}
