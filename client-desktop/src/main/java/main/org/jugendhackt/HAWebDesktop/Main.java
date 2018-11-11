package main.org.jugendhackt.HAWebDesktop;

import main.org.jugendhackt.HAWebDesktop.Gui.*;
import main.org.jugendhackt.HAWebDesktop.communication.Websocket;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static final ChatGui chatGui = new ChatGui();
    static final String conn = "ws://localhost:8888/ws";
    public static Websocket websocket;
    public static JPanel chatpanel = chatGui.getChatpane();
    public static JPanel homeworkpanel = new HOMEWORKGui().getHomeworkPanel();
    public static JPanel knowhowpanel = new KNOWHOWGui().getKnowhowPanel();
    public static List<Message> messages;
    public static JPanel mainpanel = new MainGui().MainGui();

    public static void main(String[] args) throws InterruptedException {
        messages = new ArrayList<>();
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (UnsupportedLookAndFeelException e) {
            e.printStackTrace();
        }


        //init();
        //Thread.sleep(1000);
        new Gui();



    }

    public static void init() {
        try {
            System.out.println("init()");
            websocket = new Websocket();
            websocket.createWebsocket(conn);
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
