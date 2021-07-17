package it.provinceecomuni.provinceecomuni;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.TreeSet;
import java.util.Vector;

import org.apache.poi.EncryptedDocumentException;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;

public class CreaFileExcel {

	private static String file = "Province e comuni.xlsx";
	
	private static Vector<String> righeFile = new Vector<String>();
	private static TreeSet<String> province = new TreeSet<String>();
	private static TreeSet<String> comuniPerProvincia = new TreeSet<String>();

	public static void creaFile() {

		try {
			
			Scanner fileInput = new Scanner(new BufferedReader(new FileReader("comuni_italiani.txt")));
			FileInputStream fileOutput = new FileInputStream(new File(file));
			
			Workbook workbook = WorkbookFactory.create(fileOutput);
			
			Sheet sheet = workbook.getSheetAt(0);
			
			int row = 0, column = 0;
			
			fileInput.nextLine();
			
			while(fileInput.hasNext())
				righeFile.add(fileInput.nextLine());
			
			for(String riga : righeFile) {
				
				province.add(riga.substring(riga.lastIndexOf(',') + 1));
				
			}

			for(int i = 0; i < 318; i++)
				sheet.createRow(i);
			
			for(String provincia : province) {
				
				for(String riga : righeFile) {
					
					if(riga.contains(provincia)) {
						int primaVirgola = riga.indexOf(',');
						comuniPerProvincia.add(riga.substring(primaVirgola + 1, riga.indexOf(',', primaVirgola + 1)));
					}
					
				}
				
				Row riga = sheet.getRow(row++);
				Cell cella = riga.createCell(column);
				cella.setCellValue(provincia);
				
				for(String comune : comuniPerProvincia) {
					Row r = sheet.getRow(row++);
					Cell c = r.createCell(column);
					c.setCellValue(comune);
				}
				
				row = 0;
				column++;
				
				System.out.println(provincia);
				System.out.println(comuniPerProvincia);
				
				comuniPerProvincia.clear();
				
			}
			
			FileOutputStream output = new FileOutputStream(file);
			workbook.write(output);
			workbook.close();
			fileInput.close();
			fileOutput.close();
			output.close();

		} catch (IOException | EncryptedDocumentException | InvalidFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
