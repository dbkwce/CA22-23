module com.example.vector_quantization {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;


    opens com.example.vector_quantization to javafx.fxml;
    exports com.example.vector_quantization;
}