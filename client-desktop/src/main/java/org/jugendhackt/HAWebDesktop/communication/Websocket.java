package org.jugendhackt.HAWebDesktop.communication;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

import java.net.URI;
import java.net.URISyntaxException;

public class Websocket {

    public static void main (String[] args) throws URISyntaxException {
        sendWebsocket();
    }

    public static void sendWebsocket() throws URISyntaxException {
        WebSocketClient mWs = new WebSocketClient( new URI( "ws://172.22.42.72:8888/ws" ))
        {
            @Override
            public void onMessage( String message ) {
                System.out.println(message);
            }

            @Override
            public void onOpen( ServerHandshake handshake ) {
                System.out.println( "opened connection" );
            }

            @Override
            public void onClose( int code, String reason, boolean remote ) {
                System.out.println( "closed connection" );
            }

            @Override
            public void onError( Exception ex ) {
                ex.printStackTrace();
            }

        };
        //open websocket
        mWs.connect();

        String message = "{type: \"chat\", message: \"Hi\"}";
        //send message
        mWs.send(message);
    }


}
