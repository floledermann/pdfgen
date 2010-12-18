import subprocess
import codecs
import sys
import os


def get_jar_path():
    """Return the full path to the PDFGen Java archive."""
    #return resource_filename(__name__, "pdfgen.jar")
    return os.path.join(sys.prefix, 'bin/pdfgen/pdfgen.jar')

PDF_COMMAND = 'java -cp %s com.floledermann.pdf.PDFRenderer' % get_jar_path()

def html_to_pdf(html):
    p = subprocess.Popen(PDF_COMMAND, 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stdin=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
            
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
