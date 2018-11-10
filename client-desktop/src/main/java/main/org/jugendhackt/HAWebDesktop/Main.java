package main.org.jugendhackt.HAWebDesktop;

import main.org.jugendhackt.HAWebDesktop.Gui.Gui;
import main.org.jugendhackt.HAWebDesktop.communication.Websocket;

import javax.swing.*;

public class Main {
static Websocket websocket;
static final String conn = "ws://172.22.42.72:8888/ws";
    public static void main(String[] args) {
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

        try {
            websocket = new Websocket();
            websocket.createWebsocket(conn);
        }catch (Exception e) {
            e.printStackTrace();
        }

        new Gui();

    }

}
