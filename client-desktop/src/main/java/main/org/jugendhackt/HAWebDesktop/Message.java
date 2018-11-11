package main.org.jugendhackt.HAWebDesktop;

public class Message {
    String message, sender, timestamp;
    public Message(String msg, String s, String t) {
        message = msg;
        sender = s;
        timestamp = t;
    }
    public String getMessage() {
        return message;
    }
    public String getSender() {
        return sender;
    }
    public String getTimestamp() {
        return timestamp;
    }
}
