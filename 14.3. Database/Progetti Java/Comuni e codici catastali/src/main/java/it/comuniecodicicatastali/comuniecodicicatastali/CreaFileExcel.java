package it.comuniecodicicatastali.comuniecodicicatastali;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;

import org.apache.poi.EncryptedDocumentException;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;

public class CreaFileExcel {

	private static String fileInputStr = "Elenco comuni italiani.xls";
	private static String fileOutputStr = "Comuni e codici catastali.xlsx";

	private static TreeMap<String, String> comuniECodiciCatastali = new TreeMap<String, String>();

	public static void creaFile() {

		try {

			FileInputStream fileInput = new FileInputStream(new File(fileInputStr));
			FileInputStream fileOutput = new FileInputStream(new File(fileOutputStr));

			Workbook workbookInput = WorkbookFactory.create(fileInput);
			Workbook workbookOutput = WorkbookFactory.create(fileOutput);

			Sheet sheetInput = workbookInput.getSheetAt(0);
			Sheet sheetOutput = workbookOutput.getSheetAt(0);

			int rowInput = 1, columnComune = 6, columnCodice = 19, rowOutput = 0;

			for (int i = 0; i < 7904; i++) {
				Row r = sheetInput.getRow(rowInput++);
				comuniECodiciCatastali.put(r.getCell(columnComune).getStringCellValue(),
						r.getCell(columnCodice).getStringCellValue());
				sheetOutput.createRow(i);
			}

			for (Map.Entry<String, String> entry : comuniECodiciCatastali.entrySet()) {

				Row r = sheetOutput.getRow(rowOutput++);
				r.createCell(0).setCellValue(entry.getKey());
				r.createCell(1).setCellValue(entry.getValue());

			}

			FileOutputStream output = new FileOutputStream(fileOutputStr);
			workbookOutput.write(output);
			workbookInput.close();
			workbookOutput.close();
			fileInput.close();
			fileOutput.close();
			output.close();

		} catch (IOException | EncryptedDocumentException | InvalidFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
