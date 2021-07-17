package it.provinceecomuni.provinceecomuni;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProvinceEComuniApplication {

	public static void main(String[] args) {
		SpringApplication.run(ProvinceEComuniApplication.class, args);
		CreaFileExcel.creaFile();
	}

}
