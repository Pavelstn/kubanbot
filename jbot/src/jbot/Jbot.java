/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package jbot;

import com.gargoylesoftware.htmlunit.FailingHttpStatusCodeException;
import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.*;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author pavel
 */
public class Jbot {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            // TODO code application logic here
            final WebClient webClient = new WebClient();
            webClient.setJavaScriptEnabled(false);
            final HtmlPage page = webClient.getPage("http://forums.kuban.ru/f1274");
            //final List<?> links = page.getByXPath("//a");
            // final HtmlAnchor link = (HtmlAnchor) page.getByXPath("//a[@class='normal222']").get(0);

           // final List<HtmlAnchor> links = (List<HtmlAnchor>) page.getByXPath("//a");
            
           //final List<HtmlAnchor> links = (List<HtmlAnchor>) page.getByXPath("//*[@id='thread_title_288267\\d']");
            final List<HtmlAnchor> links = (List<HtmlAnchor>) page.getByXPath("//*[contains(@id,'thread_title_')]");
            
          //  final DomNodeList<DomNode> links  = page.querySelectorAll("normal222");
            
            
           // final List<HtmlAnchor> links = page.getHtmlElementById("some_div_id");
           
           System.out.println("____________________________________");
            for (int i = 0; i < links.size(); i++) {
                System.out.println(links.get(i).getHrefAttribute() );
            }


            
            //System.out.println(link.getHrefAttribute());
            System.out.println("____________________________________");
            webClient.closeAllWindows();
        } catch (IOException ex) {
            System.out.println("error");
        }



    }
}
