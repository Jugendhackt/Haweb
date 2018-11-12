// This is an special build get the newest at https://github.com/antonk123/haweb
package main.org.jugendhackt.HAWebDesktop.communication;

import main.org.jugendhackt.HAWebDesktop.Util;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

import java.net.URI;
import java.net.URISyntaxException;

public class Websocket {
    public static WebSocketClient mWs;

// new URI( "ws://172.22.42.160:8888/ws" )
    public void createWebsocket(String path) throws URISyntaxException {

         mWs = new WebSocketClient(new URI(path) )
        {
            @Override
            public void onMessage( String message ) {
                System.out.println(message);
                Util.messageRecived(message);
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

    }

public boolean sendmessage(String type, String mess) {
if(mWs.isOpen()) {
    try {
        String message = "{\"type\": \"" + type + "\", \"message\": \"" + mess + "\"}";
        //send message
        mWs.send(message);
        return true;
    } catch (Exception e) {
        return false;
    }
} else {
    return false;
}


}
public boolean isConnected() {
        return mWs.isOpen();
}
}
