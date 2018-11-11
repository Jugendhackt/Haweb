package org.jugendhackt.HAWebMC.communication;

import org.bukkit.entity.Player;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;
import org.jugendhackt.HAWebMC.Main;

import java.net.URI;
import java.net.URISyntaxException;

public class Websocket {
    public WebSocketClient mWs;
    public Player target;
    public Websocket(String path, Player player) throws URISyntaxException {
        target = player;
         mWs = new WebSocketClient(new URI(path) )
        {
            @Override
            public void onMessage( String message ) {
                JSONObject jsonobj = new JSONObject(message);
                JSONObject mess = jsonobj.getJSONObject("message");
                Message m = new Message(mess.getString("text"), mess.getString("user"), mess.getString("time"));
                target.sendMessage(Main.PREFIX + "§6" + m.sender + "§7: §r" + m.message);
            }
            @Override
            public void onOpen( ServerHandshake handshake ) {
                target.sendMessage(Main.PREFIX + "§r Serververbindung zu " + path + " aufgebaut!");
            }
            @Override
            public void onClose( int code, String reason, boolean remote ) {
                target.sendMessage(Main.PREFIX + "§r Serververbindung zu " + path + " geschlossen!");
            }
            @Override
            public void onError( Exception ex ) {
                target.sendMessage(Main.PREFIX + "§r Ein fehler ist aufgetreten!");
            }
        };
    }
    public boolean sendmessage(String type, String mess) {
        if(mWs.isOpen()) {
            try {
                String message = "{\"type\": \"" + type + "\", \"message\": \"" + mess + "\"}";
                mWs.send(message);
                return true;
            } catch (Exception e) {
                return false;
            }
        } else {
            return false;
        }
    }
    public boolean isOpen() {
            return mWs.isOpen();
    }
    public Player getTarget() {
        return target;
    }
    public void open() {
        mWs.connect();
    }
    public void close() {
        mWs.close();
    }
}
