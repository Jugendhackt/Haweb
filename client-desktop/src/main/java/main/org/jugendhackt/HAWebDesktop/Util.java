package main.org.jugendhackt.HAWebDesktop;

import main.org.jugendhackt.HAWebDesktop.Gui.Gui;
import org.json.JSONObject;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

public class Util {
    public static boolean openWebpage(URI uri) {
        Desktop desktop = Desktop.isDesktopSupported() ? Desktop.getDesktop() : null;
        if (desktop != null && desktop.isSupported(Desktop.Action.BROWSE)) {
            try {
                desktop.browse(uri);
                return true;
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return false;
    }

    public static boolean openWebpage(URL url) {
        try {
            return openWebpage(url.toURI());
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        return false;
    }

    public static JButton makeTopBarClick(JButton button, final int actionPane) {
            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    Gui.frame.getContentPane().removeAll();
                    Gui.frame.getContentPane().add(getPanel(actionPane));
                    Gui.frame.repaint();
                    Gui.frame.getContentPane().revalidate();
                    Gui.frame.setVisible(true);


                }
            });

        return button;
    }

    public static JPanel getPanel(int actionPane) {
        if(actionPane == Gui.HOME) {
            return Main.mainpanel;
        }
        if(actionPane == Gui.KNOWHOW) {
            return Main.knowhowpanel;
        }
        if(actionPane == Gui.HOMEWORK) {
            return Main.homeworkpanel;
        }
        if(actionPane == Gui.CHAT) {
            return Main.chatpanel;
        }
        return null;
    }


    public static void messageRecived(String json) {
        String msg;
        JSONObject jsonobj = new JSONObject(json);
        if(jsonobj.getString("type").equals("chat")) {
            System.out.println("Nachricht!");
            JSONObject mess = jsonobj.getJSONObject("message");
            msg = "(";
            msg = msg + mess.getString("time") + ") ";
            msg = msg + mess.getString("user") + ": ";
            msg = msg + mess.getString("text");
            System.out.println(msg);
            Message m = new Message(mess.getString("text"), mess.getString("user"), mess.getString("time"));
            Main.chatGui.addMessage(m);
        }
    }
}
