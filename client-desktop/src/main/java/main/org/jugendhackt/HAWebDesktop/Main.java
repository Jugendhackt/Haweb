package main.HAWebDesktop;

import main.HAWebDesktop.Gui.Gui;
import main.HAWebDesktop.communication.Websocket;

import javax.swing.*;

public class Main {
static Websocket websocket;
static final String conn = "ws://http://172.22.42.72:8888/ws";
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
            websocket.createWebsocket(conn);
        }catch (Exception e) {

        }

        new Gui();

    }

}
