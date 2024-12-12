//Arquivo para esteira no apps Script


// Enter Spreadsheet ID here
var SS = SpreadsheetApp.openById(''); //coloque as chaves da planilha aqui 
var str = "";
//KAUAN AFONSOOOOOOOOOO
 
function doPost(e) 
{
 
  var parsedData;
  var result = {};
   
  try
  { 
    parsedData = JSON.parse(e.postData.contents);
  } 
  catch(f)
  {
    return ContentService.createTextOutput("Error in parsing request body: " + f.message);
  }
    
  if (parsedData !== undefined)
  {
    var flag = parsedData.format;
    if (flag === undefined){
      flag = 0;
    }
     
    var sheet = SS.getSheetByName(parsedData.sheet_name);
    var dataArr = parsedData.values.split(",");
          
    var date_now = Utilities.formatDate(new Date(), "America/Sao_Paulo", "dd/MM/yyyy");
    var time_now = Utilities.formatDate(new Date(), "America/Sao_Paulo", "hh:mm:ss a");
     
    var esteira1 = dataArr [0];
    var esteira2 = dataArr [1];
    var esteira3 = dataArr [2];
     
     
    switch (parsedData.command) {
       
      case "insert_row":
          
         sheet.insertRows(2);
          
         sheet.getRange('A2').setValue(date_now);
         sheet.getRange('B2').setValue(time_now);
         sheet.getRange('C2').setValue(esteira1);  
         sheet.getRange('D2').setValue(esteira2);  
         sheet.getRange('E2').setValue(esteira3);  
          
         str = "Success";
         SpreadsheetApp.flush();
         break;
          
      case "append_row":
          
         var publish_array = new Array();
          
         publish_array [0] = date_now;
         publish_array [1] = time_now;
         publish_array [2] = esteira1;  
         publish_array [3] = esteira2;  
         publish_array [4] = esteira3;  
          
         sheet.appendRow(publish_array);
          
         str = "Success";
         SpreadsheetApp.flush();
         break;     
  
    }
     
    return ContentService.createTextOutput(str);
  }
   
  else
  {
    return ContentService.createTextOutput("Error! Request body empty or in incorrect format.");
  }
}