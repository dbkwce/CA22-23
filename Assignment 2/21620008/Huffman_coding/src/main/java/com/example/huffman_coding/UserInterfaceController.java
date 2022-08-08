package com.example.huffman_coding;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

import java.net.URL;
import java.util.ResourceBundle;

public class UserInterfaceController implements Initializable
{

    @FXML
    public TextField txt_source_path;

    @FXML
    public TextField txt_destn_path;

    @FXML
    public Button btn_encode;

    @FXML
    public Button btn_decode;

    @FXML
    public Label label_msg;




    public void btnEncodeClicked()
    {
        String source_file_path = txt_source_path.getText();
        String destn_file_path = txt_destn_path.getText();

        Zipper.encodeZip(source_file_path,destn_file_path);
        label_msg.setText("Done");
        label_msg.setVisible(true);

    }

    public void btnDecodeClicked()
    {
        String source_file_path = txt_source_path.getText();
        String destn_file_path = txt_destn_path.getText();

        Zipper.decodeZip(source_file_path,destn_file_path);
        label_msg.setText("Done");
        label_msg.setVisible(true);
    }


    @Override
    public void initialize(URL location, ResourceBundle resources) {
        label_msg.setVisible(false);
    }
}
