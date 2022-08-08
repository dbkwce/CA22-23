import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Vector;
import java.awt.Color;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

class Image {
    public static BufferedImage getBufferedImage(int[][] imagePixels, int width, int height) {
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int value = imagePixels[y][x];
                Color c = new Color(value, value, value, 255);
                image.setRGB(x, y, c.getRGB());
            }
        }
        return image;
    }

    public static void writeImage(int[][] imagePixels, int width, int height, String outPath) {
        BufferedImage image = getBufferedImage(imagePixels, width, height);
        File ImageFile = new File(outPath);
        try {
            ImageIO.write(image, "jpg", ImageFile);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

public class Decompress {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        InputStream file = new FileInputStream("NumberOfCodeBlocks.txt");
        InputStream buffer = new BufferedInputStream(file);
        ObjectInput input = new ObjectInputStream(buffer);

        InputStream file2 = new FileInputStream("QuantizedCode.txt");
        InputStream buffer2 = new BufferedInputStream(file2);
        ObjectInput input2 = new ObjectInputStream(buffer2);
        Vector<Integer> NumberOfCodeBlock = (Vector<Integer>) input.readObject();
        Vector<Vector<Integer>> CodeBook = (Vector<Vector<Integer>>) input2.readObject();
        input.close();
        input2.close();
        
        int width = 0;
        int height = 0;

        int vectorWidth = 0;
        int vectorHeight = 0;
        ArrayList<String> temp = new ArrayList<>();
        try {
            File myObj = new File("DataInput.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                temp.add(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        int index = 0;
        for (int i = 0; i < temp.size(); i++) {
            index = temp.get(i).indexOf(":");
            if (temp.get(i).contains("VectorWidth"))
                vectorWidth = Integer.parseInt(temp.get(i).substring(index + 1));
            else if (temp.get(i).contains("VectorHegiht"))
                vectorHeight = Integer.parseInt(temp.get(i).substring(index + 1));
            else if (temp.get(i).contains("Widthimg"))
                width = Integer.parseInt(temp.get(i).substring(index + 1));
            else if (temp.get(i).contains("codeBlockSize")) {
            } else
                height = Integer.parseInt(temp.get(i).substring(index + 1));

        }

        int[][] DecompressImage = new int[height][width];

        for (int i = 0; i < NumberOfCodeBlock.size(); i++) {
            int x = i / (width / vectorHeight);
            int y = i % (width / vectorHeight);
            x *= vectorHeight;
            y *= vectorWidth;
            int v = 0;
            for (int j = x; j < x + vectorHeight; j++) {
                for (int k = y; k < y + vectorWidth; k++) {
                    if (j < height & k < width)
                    DecompressImage[j][k] = CodeBook.get(NumberOfCodeBlock.get(i)).get(v++);
                }
            }
        }
        Image.writeImage(DecompressImage, width, height, "CompressedImage.jpg");
    }
}
