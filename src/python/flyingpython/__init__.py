
PDF_COMMAND = 'java -cp bin/pdfgen.jar com.floledermann.pdf.PDFRenderer'

def html_to_pdf(html):
    p = subprocess.Popen(settings.PDF_COMMAND, 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stdin=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    
    import sys, codecs, locale   
        
    p2 = codecs.getwriter('utf-8')(p.stdin)    
    p2.write(html)
    p2.close()

    pdf = p.stdout.read()
    p.stdout.close()

    err = p.stderr.read()
    p.stderr.close()
    
    if p.wait() != 0:
        if not err:
            err = 'Error launching PDF renderer'

        raise Exception(err)

    return pdf
