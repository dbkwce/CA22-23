package com.example.huffman_coding;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.util.Objects;

public class Main extends Application
{
    @Override
    public void start(Stage primaryStage) throws Exception {
        try {
            AnchorPane root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("user-interface.fxml")));
            Scene scene = new Scene(root, 342, 459);
            primaryStage.setScene(scene);
            primaryStage.setTitle("Huffman coding");
            primaryStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
