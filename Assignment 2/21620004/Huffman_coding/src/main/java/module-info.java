module com.example.huffman_coding {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.huffman_coding to javafx.fxml;
    exports com.example.huffman_coding;
}