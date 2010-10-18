package com.floledermann.pdf;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

import org.xhtmlrenderer.pdf.ITextRenderer;

import com.lowagie.text.DocumentException;


/*
 * Created on 03.02.2010
 */

public class PDFRenderer {

    /**
     * @param args
     */
    public static void main(String[] args) throws IOException, DocumentException {

        OutputStream out = null;
        String inputURL = null;
        String inputText = null;
        
        if (args.length >= 2) {
            out = new FileOutputStream(args[1]);
        }
        else {
            out = System.out;
        }
        
        if (args.length >= 1) {
            inputURL = args[0];
            if (!inputURL.startsWith("http://")) {
                // convert local file to url
                inputURL = new File(inputURL).toURI().toURL().toString();
            }
        }
        else {
            // read from stdin
            ByteArrayOutputStream inputBytes = new ByteArrayOutputStream(1024);
            int len;
            byte buf[] = new byte[1024];
            while ((len=System.in.read(buf))>0) {
                inputBytes.write(buf, 0, len);
            }
            // TODO: add command line attribute for encoding
            inputText = inputBytes.toString("UTF8");
            
        }
        
        ITextRenderer renderer = new ITextRenderer();
        if (inputURL != null) {
            renderer.setDocument(inputURL);
        }
        else {
            renderer.setDocumentFromString(inputText);
        }
        renderer.layout();
        renderer.createPDF(out);
        
        out.close();

    }

}
